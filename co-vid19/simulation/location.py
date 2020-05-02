import pandas as pd
import numpy as np
import random



class Location:
    def __init__(self):
        self.is_infected = False # determine if the location is infected
        self.n_rolls_with_virus = 0 # number of days since a location has the virus
        self.max_rolls_with_virus = 30
        self.location_infection_rate = 0
        self.location_cure_rate = 0
        self.name = ""


    def location_info_updater(self):
        if(self.is_infected == True):
            if(self.n_rolls_with_virus < self.max_rolls_with_virus):
                self.n_rolls_with_virus = self.n_rolls_with_virus + 1
            else:
                self.n_rolls_with_virus = 0
                self.is_infected = False


    def location_infection_roll(self):
        if(self.is_infected == True):
            pass
        else:
            irate = 2 + 1
            result = random.randint(1, irate)
            if(result == 1):
                self.is_infected = True
    

    def print_info(self, printing=False):
        if(printing):
            print("===========================")
            print(f'Information for Location: {self.name}')
            print(f'- Is infected: {self.is_infected}')
            print(f'- Number of rolls with virus: {self.n_rolls_with_virus}')
            print('')



class Home(Location):
    def __init__(self):
        super().__init__()
        self.name = "Home"
        self.location_cure_rate = 100
    

    def is_cured_peep_roll(self):
        if(self.is_infected):
            result = random.randint(1, self.location_cure_rate)
            if(result == 1):
                # 1 in 100 chance the peep gets cured at this location
                # peep took some meds and is feeling better
                # return that this peep is cured
                return True
            else:
                return False
        else:
            return False

            

class Store(Location):
    def __init__(self):
        super().__init__()
        self.name = "Store"
        self.location_infection_rate = 6


    def is_infects_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = self.location_infection_rate/infection_rate + 1
            result = random.randint(1, irate)
            if(result == self.location_infection_rate/2):
                return True
            else:
                return False
        else:
            return False



class Work(Location):
    def __init__(self):
        super().__init__()
        self.name = "Work"
        self.location_infection_rate = 8


    def is_infects_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = self.location_infection_rate/infection_rate + 1
            result = random.randint(1, irate)
            if(result == 1):
                # 1 in 10 or 1 in 20 chance the peep gets infected at this location
                # return that this peep is infected
                return True
            else:
                return False
        else:
            return False



class Park(Location):
    def __init__(self):
        super().__init__()
        self.name = "Park"
        self.location_infection_rate = 10


    def is_infects_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = 20/infection_rate + 1
            result = random.randint(1, irate)
            if(result == 1):
                # 1 in 10 or 1 in 20 chance the peep gets infected at this location
                # return that this peep is infected
                return True
            else:
                return False
        else:
            return False



class Party(Location):
    def __init__(self):
        super().__init__()
        self.name = "Party"
        self.location_infection_rate = 2


    def is_infects_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = self.location_infection_rate/infection_rate + 1
            result = random.randint(1, irate)
            if(result == 1):
                # 1 in 10 or 1 in 20 chance the peep gets infected at this location
                # return that this peep is infected
                return True
            else:
                return False
        else:
            return False



class Hospital(Location):
    def __init__(self):
        super().__init__()
        self.name = "Hospital"
        self.location_infection_rate = 50
        self.location_cure_rate = 10

    
    def is_infects_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = self.location_infection_rate/infection_rate + 1
            result = random.randint(1, irate)
            if(result == 1):
                # 1 in 50 or 1 in 25 chance the peep gets infected at this location
                # return that this peep is infected
                return True
            else:
                return False
        else:
            return False


    def is_cured_peep_roll(self, infection_rate):
        if(self.is_infected):
            irate = self.location_cure_rate/infection_rate + 1
            result = random.randint(1, irate)
            if(result == 1):
                # oeep gets cured at the hospital
                return True
            else:
                return False
        else:
            return False



class PeepTown():
    def __init__(self):
        self.peepHome = Home()
        self.groceryStore = Store()
        self.cityPark = Park()
        self.businessCenter = Work()
        self.nightClub = Party()
        self.hospital = Hospital()