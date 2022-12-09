class Event():

    def __init__(self, date, event_name, number_of_guests, room_location, descriptionn, recurring):
        self.event_name = event_name 
        self.description = descriptionn
        self.date = date
        self.number_of_guests = number_of_guests
        self.room_location = room_location
        self.recurring = recurring

    # def recurring(self):
    #     self.recurring = True
