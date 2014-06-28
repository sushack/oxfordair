class Pollutant:
    def __init__(self, id, name, unit):
        self.id = id
        self.name = name
        self.unit = unit

class PollutantCollection:
    def __init__(self):
        self.pollutants = []

    def add_pollutant(self, pollutant):
        self.pollutants.append(pollutant)

    def objects(self):
        return self.pollutants

class Site:
    def __init__(self, id, name, available_pollutants):
        self.id = id
        self.name = name
        self.available_pollutants = available_pollutants

class SiteCollection:
    def __init__(self):
        self.sites = []

    def add_site(self, site):
        self.sites.append(site)

    def objects(self):
        return self.sites


class PollutantData:
    def __init__(self, pollutant, site, timestamp, value):
        self.pollutant = pollutant
        self.site = site
        self.timestamp = timestamp
        self.value = value

class PollutantDataCollection:
    def __init__(self):
        self.pollutant_data = []

    def add_pollutant_data(self, pollutant_data):
        self.pollutant_data.append(pollutant_data)

    def objects(self):
        return self.pollutant_data

    def find(self, site=None, pollutant=None):
        ret = pollutant_data
        if site is not None:
            ret = filter(lambda x: x.site == site, ret)
        if pollutant is not None:
            ret = filter(lambda x: x.pollutant == pollutant, ret)
        return ret
