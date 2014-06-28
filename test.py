import unittest

from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection
from models import Site, SiteCollection
from data_import import SingleSiteCSVParser

class TestApplication(unittest.TestCase):

    def setUp(self):
        # adding some pollutants
        self.pollutant1 = Pollutant("no2", "Nitrogen Dioxide", "ug/m3")
        self.pollutant2 = Pollutant("o3", "Ozone", "ug/m3")

        # adding some sites
        self.site1 = Site("oxford_st_ebbes", "Oxford St Ebbes", [self.pollutant1, self.pollutant2])
        self.site2 = Site("oxford_high_st", "Oxford High Street", [self.pollutant1])
        
        # adding some pollutantData
        self.pdata1 = PollutantData(self.pollutant1, self.site1, "2014-06-28T10:00:00+00:00", "50")
        self.pdata2 = PollutantData(self.pollutant2, self.site1, "2014-06-28T10:00:00+00:00", "40")

        # data import init
        
        
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

    def test_should_objects_gives_all_sites(self):
        self.sites_collection = PollutantCollection()
        self.sites_collection.add_pollutant(self.site1)
        self.sites_collection.add_pollutant(self.site2)
        self.assertEqual(len(self.sites_collection.objects()), 2)

    def test_should_add_polutant_data_increase_objects(self):
        self.pdata_collection = PollutantDataCollection()
        self.pdata_collection.add_pollutant_data(self.pdata1)
        self.assertEqual(len(self.pdata_collection.objects()), 1)

    def test_should_objects_gives_all_pollutant_data(self):
        self.pdata_collection = PollutantDataCollection()
        self.pdata_collection.add_pollutant_data(self.pdata1)
        self.pdata_collection.add_pollutant_data(self.pdata2)
        self.assertEqual(len(self.pdata_collection.objects()), 2)

    # data import Tests
    def test_should_SingleSiteCSVParser_gives_an_array_of_pollutants(self):
        site_collection = SiteCollection()
        pollutant_collection = PollutantCollection()
        pollutant_data_collection = PollutantDataCollection()
        SingleSiteCSVParser("data/OX8_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
        self.assertEqual( len(pollutant_collection.objects()), 9  )

    def test_should_SingleSiteCSVParser_gives_an_array_of_pollutantsData(self):
        site_collection = SiteCollection()
        pollutant_collection = PollutantCollection()
        pollutant_data_collection = PollutantDataCollection()
        SingleSiteCSVParser("data/OX8_2014.csv", site_collection, pollutant_collection, pollutant_data_collection)
        self.assertEqual( len(pollutant_data_collection.objects()), 29340  )
        
if __name__ == '__main__':
    unittest.main()
