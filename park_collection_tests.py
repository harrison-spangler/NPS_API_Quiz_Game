import unittest
import json
from park_collection import ParkCollection

class test_park_collection(unittest.TestCase):
    def test_len_park_list(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            self.assertEqual(park_collection.len_park_list(), 5)

    def test_most_amenities(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            most_amenities = park_collection.most_activities()
            self.assertEqual(most_amenities, "Acadia National Park")

    def test_most_topics(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            most_topics = park_collection.most_topics()
            self.assertEqual(most_topics, "Acadia National Park")

    def test_sort_parks(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            sorted_parks = park_collection.sort_parks()
            for i in range(len(sorted_parks) - 1):
                self.assertLessEqual(sorted_parks[i].fullName, sorted_parks[i + 1].fullName)

    def test_search_park_by_name_found(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            park_name = "Acadia National Park"
            park = park_collection.search_park_by_name(park_name)
            self.assertIsNotNone(park)
            self.assertEqual(park.fullName, park_name)

    def test_search_park_by_name_not_found(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park_collection = ParkCollection(nps_json)
            park_name = "Non-existent Park"
            park = park_collection.search_park_by_name(park_name)
            self.assertIsNone(park)