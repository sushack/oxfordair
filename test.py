import unittest

from models import Pollutant, PollutantCollection, PollutantData, PollutantDataCollection
from models import Site, SiteCollection

#st_ebbes = Site("stebbes", "St Ebbes", no2)
#site_collection.add_site(st_ebbes)


class TestModels(unittest.TestCase):

    def setUp(self):
        self.pollutants_collection = PollutantCollection()
        site_collection = SiteCollection()
        pollutant_data_collection = PollutantDataCollection()

    def test_add_pollutant(self):
        no2 = Pollutant("no2", "Nitrogen Dioxide", "ug/m3")
        self.pollutants_collection.add_pollutant(no2)
        self.assertEqual(len(self.pollutants_collection.objects()), 1)
        self.assertEqual(self.pollutants_collection.objects()[0], no2)

if __name__ == '__main__':
    unittest.main()
