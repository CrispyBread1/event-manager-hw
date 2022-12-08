class Event():

    def __init__(self, date, event_name, number_of_guests, room_location, description):
        self.event_name = event_name 
        self.description = description
        self.date = date
        self.number_of_guests = number_of_guests
        self.room_location = room_location
        self.recurringt = False

    def recurring(self):
        self.recurringt = True
