import pandas as pd
import numpy as np
import random



class Peep:
    def __init__(self, is_infected, number, is_alive):
        self.is_infected = is_infected # determine if the peep is infected
        self.number = number # the peep name/numbers
        self.is_alive = True # the peep starts out as alive
        self.sickness_level = 999
        self.n_supplies = 0
        self.is_already_infected = False
        self.is_printing_info = False
        self.behavior = "base"


    def roll_sickness(self):
        if(self.is_infected):
            self.sickness_level = random.randint(5, 21)


    def subtract_sickness(self):
        if(self.is_alive):
            if(self.is_infected):
                if(self.sickness_level < 0):
                    self.kill_peep()
                else:
                    self.sickness_level = self.sickness_level - 1


    def subtract_supplies(self):
        if(self.is_alive):
            self.n_supplies = self.n_supplies - 1

            if(self.n_supplies < 0):
                self.kill_peep()

    
    def go_home(self):
        # tells the peep to go home
        self.current_position = "Home"

    
    def go_to_hospital(self):
        # tells the peep to go to the Hospital
        self.current_position = "Hospital"
        self.n_supplies = 5


    def is_needing_supplies(self):
        if(self.n_supplies == 0):
            return True
        else:
            return False


    def is_needing_hospital(self):
        if(self.is_infected):
            if(self.sickness_level <= 5):
                return True
            else:
                return False
        else:
            return False

    
    def print_info(self, printing=False):
        if(self.is_printing_info == True or printing):
            print("")


    def kill_peep(self):
        print("X.X    X.X    X.X    X.X")
        self.is_alive = False
        self.is_printing_info = False
        self.print_info(True)



class HomebodyPeep(Peep):
    def __init__(self, is_infected, number, is_alive, n_supplies, current_position):
        super().__init__(is_infected, number, is_alive)
        self.n_supplies = 14 # Homebody peeps alwyas start off with the max amount of supplies
        self.current_position = "Home" # homebody peeps always start off at home
        self.infection_rate = 2 # times a two factor for homebody peeps bc they always buy max supplies
        self.behavior = "HomebodyPeep"
        self.max_supplies = 14


    def print_info(self, printing=False):
        if(self.is_printing_info == True or printing):
            print("===========================")
            print(f'Information for Peep: {self.number}')
            print(f'- Behavior: {self.behavior}')
            print(f'- Is alive: {self.is_alive}')
            print(f'- Is infected: {self.is_infected}')
            print(f'- Number of supplies: {self.n_supplies}')
            print(f'- Sickness Level: {self.sickness_level}')
            print(f'- Current position: {self.current_position}')
            print(f'- Infection Rate: {self.infection_rate}')
            print('')


    def go_to_store(self):
        # tells the peep to go to the store
        # The homebody peep buys 14 supplies
        # The homebody peeps contagion rate is doubled
        self.current_position = "Store"
        self.n_supplies = self.n_supplies + self.max_supplies


    def roll(self):
        if(self.is_alive):
            self.subtract_supplies()
            self.subtract_sickness()

        if(self.is_alive):
            if(self.is_infected == False):
                if(self.current_position == "Home"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()

                elif(self.current_position == "Store"):
                    self.go_home()
                
                elif(self.current_position == "Hospital"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()


            elif(self.is_infected == True):
                if(self.current_position == "Home"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()

                elif(self.current_position == "Store"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    else:
                        self.go_home()
                
                elif(self.current_position == "Hospital"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()



class SemiHomiePeep(Peep):
    def __init__(self, is_infected, number, is_alive, n_supplies, current_position):
        super().__init__(is_infected, number, is_alive)
        self.current_position = "Home"
        self.n_supplies = random.randint(1,15)
        self.rolls_to_work = 5
        self.infection_rate = 1
        self.behavior = "SemiHomiePeep"


    def print_info(self, printing=False):
        if(self.is_printing_info == True or printing):
            print("===========================")
            print(f'Information for Peep: {self.number}')
            print(f'- Behavior: {self.behavior}')
            print(f'- Is alive: {self.is_alive}')
            print(f'- Is infected: {self.is_infected}')
            print(f'- Number of supplies: {self.n_supplies}')
            print(f'- Sickness Level: {self.sickness_level}')
            print(f'- Current position: {self.current_position}')
            print(f'- Infection Rate: {self.infection_rate}')
            print('')


    def go_home(self):
        # tells the peep to go home
        self.current_position = "Home"


    def go_to_store(self):
        # tells the peep to go to the store
        self.current_position = "Store"
        self.n_supplies = self.n_supplies + random.randint(7,15)


    def go_to_park(self):
		# tells the peep to go to the park
        self.current_position = "Park"


    def go_to_work(self):
        # tells the peep to go to work for a roll
        self.current_position = "Work"
        self.went_to_work = True
        self.rolls_to_work = self.rolls_to_work - 1


    def is_work_roll(self):
        if(self.rolls_to_work > 0):
            return True
        else:
            return False


    def is_needing_supplies(self):
        if(self.n_supplies == 0):
            return True
        else:
            return False


    def roll(self):
        if(self.is_alive):
            self.subtract_supplies()
            self.subtract_sickness()

        if(self.is_alive):            
            if(self.is_infected == False):
                if(self.current_position == "Home"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_to_park()
                elif(self.current_position == "Store"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()
                elif(self.current_position == "Work"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()
                elif(self.current_position == "Park"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()
                elif(self.current_position == "Hospital"):
                    if(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()

            elif(self.is_infected == True):
                if(self.current_position == "Home"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                elif(self.current_position == "Store"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()
                elif(self.current_position == "Work"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()
                elif(self.current_position == "Park"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()
                elif(self.current_position == "Hospital"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()


class OutGoerPeep(Peep):
    def __init__(self, is_infected, number, is_alive, n_supplies, current_position):
        super().__init__(is_infected, number, is_alive)
        self.current_position = "Home"
        self.n_supplies = random.randint(1,15)
        self.rolls_to_work = 3
        self.infection_rate = 1
        self.behavior = "OutGoerPeep"

        self.randomly_infect()


    def randomly_infect(self):
        # a random number of these unlucky boys will be infected
        rand = random.randint(1,100)
        if(rand == 10):
            self.is_infected = True
            self.roll_sickness()


    def print_info(self, printing=False):
        if(self.is_printing_info == True or printing):
            print("===========================")
            print(f'Information for Peep: {self.number}')
            print(f'- Behavior: {self.behavior}')
            print(f'- Is alive: {self.is_alive}')
            print(f'- Is infected: {self.is_infected}')
            print(f'- Number of supplies: {self.n_supplies}')
            print(f'- Sickness Level: {self.sickness_level}')
            print(f'- Current position: {self.current_position}')
            print(f'- Infection Rate: {self.infection_rate}')
            print('')


    def go_home(self):
        # tells the peep to go home
        self.current_position = "Home"


    def go_to_store(self):
        # tells the peep to go to the store
        self.current_position = "Store"
        self.n_supplies = self.n_supplies + random.randint(7,15)
    

    def go_to_work(self):
        # tells the peep to go to work for a roll        
        self.current_position = "Work"
        self.went_to_work = True
        self.rolls_to_work = self.rolls_to_work - 1
        

    def go_to_park(self):
		# tells the peep to go to the park
        self.current_position = "Park"


    def go_to_party(self):
        # tells the peep to go to a party
        self.current_position = "Party"


    def is_work_roll(self):
        if(self.rolls_to_work > 0):
            return True
        else:
            return False


    def is_needing_supplies(self):
        if(self.n_supplies == 0):
            return True
        else:
            return False


    def roll(self):
        if(self.is_alive):
            self.subtract_supplies()
            self.subtract_sickness()
            
        if(self.is_alive):            
            if(self.is_infected == False or self.is_infected == True):
                if(self.current_position == "Home"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        if(random.randint(1,3) == 1):
                            self.go_to_park()
                        else:
                            self.go_to_party()
                    
                elif(self.current_position == "Store"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()

                elif(self.current_position == "Work"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    else:
                        self.go_home()

                elif(self.current_position == "Park"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()

                elif(self.current_position == "Party"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()
                
                elif(self.current_position == "Hospital"):
                    if(self.is_needing_hospital()):
                        self.go_to_hospital()
                    elif(self.is_needing_supplies()):
                        self.go_to_store()
                    elif(self.is_work_roll()):
                        self.go_to_work()
                    else:
                        self.go_home()