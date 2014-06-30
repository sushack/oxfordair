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

    def find(self, id=None, name=None):
        ret = self.pollutants
        if id is not None:
            ret = filter(lambda x: x.id == id, ret)
        if name is not None:
            ret = filter(lambda x: x.name == name, ret)
        return ret
    
    def get_by_id(self, id):
        for pollutant in self.pollutants:
            if pollutant.id == id:
                return pollutant
        return None

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

    def get_by_id(self, id):
        for site in self.sites:
            if site.id == id:
                return site
        return None


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
        ret = self.pollutant_data
        if site is not None:
            ret = filter(lambda x: x.site.id == site.id, ret)
        if pollutant is not None:
            ret = filter(lambda x: x.pollutant.id == pollutant.id, ret)
        return ret
