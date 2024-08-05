import unittest
import json
from park import Park

class TestPark(unittest.TestCase):
    def test_total_activities(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park1 = Park(nps_json[0])
            total_activities = park1.total_activities()
            self.assertEqual(total_activities, 15)

            park2 = Park(nps_json[1])
            total_activities = park2.total_activities()
            self.assertEqual(total_activities, 46)

            park3 = Park(nps_json[2])
            total_activities = park3.total_activities()
            self.assertEqual(total_activities, 6)

            park4 = Park(nps_json[3])
            total_activities = park4.total_activities()
            self.assertEqual(total_activities, 2)

            park5 = Park(nps_json[4])
            total_activities = park5.total_activities()
            self.assertEqual(total_activities, 16)

    def test_total_topics(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park1 = Park(nps_json[0])
            total_topics = park1.total_topics()
            self.assertEqual(total_topics, 9)

            park2 = Park(nps_json[1])
            total_topics = park2.total_topics()
            self.assertEqual(total_topics, 31)

            park3 = Park(nps_json[2])
            total_topics = park3.total_topics()
            self.assertEqual(total_topics, 2)

            park4 = Park(nps_json[3])
            total_topics = park4.total_topics()
            self.assertEqual(total_topics, 4)

            park5 = Park(nps_json[4])
            total_topics = park5.total_topics()
            self.assertEqual(total_topics, 16)

    def test_latitude_longitude(self):
        with open("nps.json", 'r') as nps:
            nps_json = json.load(nps)
            park1 = Park(nps_json[0])
            latitude_longitude = park1.latitude_longitude()
            self.assertEqual(latitude_longitude, ('lat:37.5858662, long:-85.67330523'))

            park2 = Park(nps_json[1])
            latitude_longitude = park2.latitude_longitude()
            self.assertEqual(latitude_longitude, ('lat:44.409286, long:-68.247501'))

            park3 = Park(nps_json[2])
            latitude_longitude = park3.latitude_longitude()
            self.assertEqual(latitude_longitude, ('lat:42.2553961, long:-71.01160356'))

            park4 = Park(nps_json[3])
            latitude_longitude = park4.latitude_longitude()
            self.assertEqual(latitude_longitude, ('lat:38.9166, long:-77.026'))

            park5 = Park(nps_json[4])
            latitude_longitude = park5.latitude_longitude()
            self.assertEqual(latitude_longitude, ('lat:42.42170419, long:-103.753886'))

if __name__ == '__main__':
    unittest.main()