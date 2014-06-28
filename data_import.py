import datetime
import csv

from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection, Site, SiteCollection

def make_simple_id_from_name(name):
    return name.lower().replace(" ", "_")

def make_pollutant_id_from_name(name):
    if name == "Nitric oxide":
        return "NO"
    elif name == "Nitrogen dioxide":
        return "NO2"
    elif name == "Nitrogen oxides as nitrogen dioxide":
        return "NOx"
    elif name == "PM<sub>10</sub> particulate matter (Hourly measured)":
        return "PM10"
    elif name == "Non-volatile PM<sub>10</sub> (Hourly measured)":
        return "nvPM10"
    elif name == "Non-volatile PM<sub>2.5</sub> (Hourly measured)":
        return "nvPM25"
    elif name == "PM<sub>2.5</sub> particulate matter (Hourly measured)":
        return "PM25"
    elif name == "Volatile PM<sub>10</sub> (Hourly measured)":
        return "vPM10"
    elif name == "Volatile PM<sub>2.5</sub> (Hourly measured)":
        return "vPM25"
    else:
        raise Exception("Unknown pollutant %s", name)


class SingleSiteCSVParser:
    def __init__(self, csv_file, site_collection, pollutant_collection, pollutant_data_collection):
        self.site_name = None
        self.site = None
        self.pollutants = []
        self.site_collection = site_collection
        self.pollutant_collection = pollutant_collection
        self.pollutant_data_collection = pollutant_data_collection

        self.parse_csv(csv_file)

    def parse_csv(self, csv_file):
        with open(csv_file, 'rb') as f:
            data = csv.reader(f, delimiter=',')
            for row in data:
                self.parse_row(row)

            self.site_collection.add_site(self.site)

            # Add pollutants to collection if they are not already there
            for pollutant in self.pollutants:
                if pollutant not in self.pollutant_collection.objects():
                    pollutant_collection.add_pollutant(pollutant)

    def parse_row(self, row):
        # Skip the first lines of the header
        if len(row) < 3:
            return

        # Get the site name line
        if row[0] == '' and row[2] != '':
            self.site_name = row[2]
            return

        # Parse schema line
        if row[0] == "Date":
            self._parse_schema_line(row)
            return

        self.site = Site(make_simple_id_from_name(self.site_name), self.site_name, [self.pollutants])

        timestamp = self._parse_timestamp(row[0], row[1])

        # Create data objects
        for idx, pollutant in enumerate(self.pollutants):
            try:
                value = int(row[2 + 3 * idx])
                if value < 0:
                    value = 0
            except ValueError:
                value = None

            if pollutant.unit is None:
                unit = row[4 + 3 * idx]
                if unit != "":
                    if unit == "ugm-3 (TEOM FDMS)":
                        unit = "ugm-3"
                    pollutant.unit = unit

            if value is not None:
                #print "%s at %s: %d %s" % (pollutant.id, str(timestamp), value, pollutant.unit)
                data = PollutantData(pollutant, self.site, timestamp, value)
                self.pollutant_data_collection.add_pollutant_data(data)

    def _parse_timestamp(self, date, time):
        # Time parsing is a bit complicated by the fact that the CSV uses 01-01-2014 24:00 instead of 02-01-2014 00:00
        if time != "24:00":
            # Parse date time from two first columns: "01-01-2014 01:00"
            return datetime.datetime.strptime(date + " " + time, "%d-%m-%Y %H:%M")
        else:
            return datetime.datetime.strptime(date, "%d-%m-%Y") + datetime.timedelta(days=1)

    def _parse_schema_line(self, row):
        i = 2
        while i < len(row):
            name = row[i]
            id = make_pollutant_id_from_name(name)
            _pollutant = Pollutant(id, name, None)
            self.pollutants.append(_pollutant)
            i += 3

if __name__ == '__main__':
    site_collection = SiteCollection()
    pollutant_collection = PollutantCollection()
    pollutant_data_collection = PollutantDataCollection()
    SingleSiteCSVParser("data/OX_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
    SingleSiteCSVParser("data/OX8_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)

    print len(site_collection.objects())
    print len(pollutant_collection.objects())
    print len(pollutant_data_collection.objects())
