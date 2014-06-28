import unittest

from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection
from models import Site, SiteCollection

class TestModels(unittest.TestCase):

    def setUp(self):
        # adding some pollutants
        self.pollutant1 = Pollutant("no2", "Nitrogen Dioxide", "ug/m3")
        self.pollutant2 = Pollutant("o3", "Ozone", "ug/m3")

        # adding some sites
        self.site1 = Site("oxford_st_ebbes", "Oxford St Ebbes", [self.pollutant1, self.pollutant2])

    def test_should_add_pollutant_increase_objects(self):
        self.pollutants_collection = PollutantCollection()
        self.pollutants_collection.add_pollutant(self.pollutant1)
        self.assertEqual(len(self.pollutants_collection.objects()), 1)
        self.assertEqual(self.pollutants_collection.objects()[0], self.pollutant1)

    def test_should_objects_gives_all_pollutants(self):
        self.pollutants_collection = PollutantCollection()
        self.pollutants_collection.add_pollutant(self.pollutant1)
        self.pollutants_collection.add_pollutant(self.pollutant2)
        self.assertEqual(len(self.pollutants_collection.objects()), 2)

    def test_should_add_site_increase_objects(self):
        self.sites_collection = SiteCollection()
        self.sites_collection.add_site(self.site1)
        self.assertEqual(len(self.sites_collection.objects()), 1)
        
if __name__ == '__main__':
    unittest.main()
