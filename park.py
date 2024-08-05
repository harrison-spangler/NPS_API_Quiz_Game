class Park:
    def __init__(self, nps_json):
        '''
        :param nps_json: The json I will get from the NPS API
        :self.fullName: Name of the park
        :self.location: Location of the park
        :self.code: Code of the park
        '''
        self.data = nps_json['data'][0]
        self.fullName = nps_json['data'][0][0]['fullName']
        if 'location' in nps_json['data'][0][0]:
            self.location = nps_json['data'][0][0]['location']['stateCode']
        else:
            self.location = nps_json['data'][0][0]['stateCode']
        self.code = nps_json['data'][0][0]['parkCode']

    def __str__(self):
        '''
        :return: String representation of the park object
        '''
        return ("Park: ", self.fullName, "Location: ", self.location, "Park code: ", self.code)

    def total_activities(self):
        '''
        :return: the amount of amenities at the park
        '''
        return len(self.data[0]['activities'])

    def total_topics(self):
        '''
        :return: The amount of accessibility options at the park
        '''
        return len(self.data[0]['topics'])

    def latitude_longitude(self):
        '''
        :return: The latitude and longitude of the park
        '''
        return self.data[0]['latLong']