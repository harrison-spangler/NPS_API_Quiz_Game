from park import Park


class ParkCollection:
    def __init__(self, nps_json):
        '''
        :param nps_json: The json file in which will be used
        create a list of Parks
        '''
        self.parks = []
        for park_json in nps_json:
            parks = Park(park_json)
            self.parks.append(parks)

    def len_park_list(self):
        '''
        :return: The amount of parks in the list of parks
        '''
        return len(self.parks)

    def most_activities(self):
        '''
        :return: The park with the most amenities
        '''
        most_activities_park = None
        max_activities = 0

        for park in self.parks:
            activities_count = park.total_activities()
            if activities_count > max_activities:
                max_activities = activities_count
                most_activities_park = park.fullName

        return most_activities_park

    def most_topics(self):
        '''
        :return: The park with the most topics
        '''
        most_topics_park = None
        max_topics = 0

        for park in self.parks:
            topics_count = park.total_topics()
            if topics_count > max_topics:
                max_topics = topics_count
                most_topics_park = park.fullName

        return most_topics_park

    def sort_parks(self):
        '''
        :return: The parks all sorted by the first letter of their names
        '''
        sorted_parks = sorted(self.parks, key=lambda park: park.fullName)
        return sorted_parks

    def search_park_by_name(self, park_name):
        '''
        :param park_name: The name of the park to search for
        :return: The Park object if found, otherwise None
        '''
        for park in self.parks:
            if park.fullName.lower() == park_name.lower():
                return park

        return None