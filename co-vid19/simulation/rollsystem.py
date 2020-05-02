from peep import Peep
from peep import HomebodyPeep
from peep import SemiHomiePeep
from peep import OutGoerPeep

from location import Location
from location import Home
from location import Store
from location import Work
from location import Park
from location import Party
from location import PeepTown


class RollSystem:
    def __init__(self, n_peeps, n_rolls):
        self.n_count = 0
        self.n_peeps = n_peeps
        self.n_rolls = n_rolls
        self.homebodypeeps = []
        self.semihomiespeeps = []
        self.outgoerpeeps = []

        self.verb = False

        self.infection_toll_total = 0

        self.death_toll_total = 0
        self.death_toll_homebodypeeps = 0
        self.death_toll_semihomiespeeps = 0
        self.death_toll_outgoerpeeps = 0

        self.per_homebodypeeps_dead = 0.0
        self.per_semihomiespeeps_dead = 0.0
        self.per_outgoerpeeps_dead = 0.0

        self.per_homebodypeeps_live = 0.0
        self.per_semihomiespeeps_live = 0.0
        self.per_outgoerpeeps_live = 0.0

        self.initialize_homebodypeeps(self.n_peeps)
        self.initialize_semihomiepeeps(self.n_peeps)
        self.initialize_outgoerpeeps(self.n_peeps)
        self.initialize_peeptown()


    def reset_n_count(self):
        if(self.n_count != 0):
            self.n_count = 0


    def initialize_homebodypeeps(self, n_homebodies):
        self.reset_n_count()
        for i in range(n_homebodies):
            if(self.verb): print(i)
            self.n_count = self.n_count + 1
            self.homebodypeeps.append(HomebodyPeep(is_infected=False, number=self.n_count, is_alive=True, n_supplies=14, current_position="Home"))


    def initialize_semihomiepeeps(self, n_semihomies):
        for i in range(n_semihomies):
            if(self.verb): print(i)
            self.n_count = self.n_count + 1
            self.semihomiespeeps.append(SemiHomiePeep(is_infected=False, number=self.n_count, is_alive=True, n_supplies=14, current_position="Home"))


    def initialize_outgoerpeeps(self, n_outgoers):
        for i in range(n_outgoers):
            if(self.verb): print(i)
            self.n_count = self.n_count + 1
            self.outgoerpeeps.append(OutGoerPeep(is_infected=False, number=self.n_count, is_alive=True, n_supplies=14, current_position="Home"))


    def initialize_peeptown(self):
        self.peepTown = PeepTown()
    

    def update_location_info(self):
        self.peepTown.peepHome.location_info_updater()
        self.peepTown.groceryStore.location_info_updater()
        self.peepTown.cityPark.location_info_updater()
        self.peepTown.businessCenter.location_info_updater()
        self.peepTown.nightClub.location_info_updater()
        self.peepTown.hospital.location_info_updater()
    
    
    def print_single_location_info(self, store, printing=False):
        store.print_info(printing)


    def location_roll_not_infected(self, location, peep, printing=False):
        if(location.name == "Home"):
            if(location.is_cured_peep_roll() == True):
                peep.is_infected = False

        elif(location.name == "Hospital"):
            if(location.is_cured_peep_roll(peep.infection_rate) == True):
                peep.infected = False

                if(location.is_infected == True):
                    if(location.is_infects_peep_roll()):
                        peep.is_infected = True

        else:
            if(location.is_infected == False):
                location.location_infection_roll()
                if(location.is_infected == True):
                    self.print_single_location_info(location, printing)

    def location_roll_is_infected(self, location, peep, printing=False):
        if(location.is_infected == True):
            peep.is_infected = location.is_infects_peep_roll(peep.infection_rate)


    def peep_roll_handler(self, peep):
        # Handles the peep during a roll
        if(peep.is_infected == True):
            if(peep.current_position == "Home"):
                self.location_roll_not_infected(self.peepTown.peepHome, peep)
            elif(peep.current_position == "Store"):
                self.location_roll_not_infected(self.peepTown.groceryStore, peep)
            elif(peep.current_position == "Work"):
                self.location_roll_not_infected(self.peepTown.businessCenter, peep)
            elif(peep.current_position == "Park"):
                self.location_roll_not_infected(self.peepTown.cityPark, peep)
            elif(peep.current_position == "Party"):
                self.location_roll_not_infected(self.peepTown.nightClub, peep)
            elif(peep.current_position == "Hospital"):
                self.location_roll_not_infected(self.peepTown.hospital, peep)

        elif(peep.is_infected == False):
            if(peep.current_position == "Home"):
               pass
            elif(peep.current_position == "Store"):
                self.location_roll_is_infected(self.peepTown.groceryStore, peep)
            elif(peep.current_position == "Work"):
                self.location_roll_is_infected(self.peepTown.businessCenter, peep)
            elif(peep.current_position == "Park"):
                self.location_roll_is_infected(self.peepTown.cityPark, peep)
            elif(peep.current_position == "Party"):
                self.location_roll_is_infected(self.peepTown.nightClub, peep)
            elif(peep.current_position == "Hospital"):
                self.location_roll_is_infected(self.peepTown.hospital, peep)                

        if(peep.is_already_infected == False):
            if(peep.is_infected == True):
                peep.roll_sickness()


    def death_toll_handler_homebodys(self, current_peep):
        if(current_peep.is_alive == False):
            self.death_toll_homebodypeeps = self.death_toll_homebodypeeps + 1
    

    def death_toll_handler_semihomies(self, current_peep):
        if(current_peep.is_alive == False):
            self.death_toll_semihomiespeeps = self.death_toll_semihomiespeeps + 1


    def death_toll_handler_outgoers(self, current_peep):
        if(current_peep.is_alive == False):
            self.death_toll_outgoerpeeps = self.death_toll_outgoerpeeps + 1


    def infection_toll_handler(self, current_peep):
        if(current_peep.is_already_infected == False):
            if(current_peep.is_infected == True):
                self.infection_toll_total = self.infection_toll_total + 1
                current_peep.is_already_infected = True


    def run_roll(self):
        for _ in range(self.n_rolls):
            # print(f'Roll Number: {i}')
            for peep in range(self.n_peeps):
                # start off with the location rolls
                self.update_location_info()
                
                current_homie_peep = self.homebodypeeps[peep]
                if(current_homie_peep.is_alive):
                    current_homie_peep.roll()
                    current_homie_peep.print_info()
                    self.peep_roll_handler(current_homie_peep)
                    self.death_toll_handler_homebodys(current_homie_peep)
                    self.infection_toll_handler(current_homie_peep)
                    
                current_semi_peep = self.semihomiespeeps[peep]
                if(current_semi_peep.is_alive):
                    current_semi_peep.roll()
                    current_semi_peep.print_info()
                    self.peep_roll_handler(current_semi_peep)
                    self.death_toll_handler_semihomies(current_semi_peep)
                    self.infection_toll_handler(current_semi_peep)

                current_outgo_peep = self.outgoerpeeps[peep]
                if(current_outgo_peep.is_alive):
                    current_outgo_peep.roll()
                    current_outgo_peep.print_info()
                    self.peep_roll_handler(current_outgo_peep)
                    self.death_toll_handler_outgoers(current_outgo_peep)
                    self.infection_toll_handler(current_outgo_peep)

        self.print_location_info()


    def get_total_statistics(self):
        self.death_toll_total = self.death_toll_homebodypeeps + self.death_toll_semihomiespeeps + self.death_toll_outgoerpeeps
        self.per_homebodypeeps_dead = (self.death_toll_homebodypeeps / self.n_peeps)
        self.per_semihomiespeeps_dead = (self.death_toll_semihomiespeeps / self.n_peeps)
        self.per_outgoerpeeps_dead = (self.death_toll_outgoerpeeps / self.n_peeps)

        self.per_homebodypeeps_live = 1.0 - self.per_homebodypeeps_dead
        self.per_semihomiespeeps_live = 1.0 - self.per_semihomiespeeps_dead
        self.per_outgoerpeeps_live = 1.0 - self.per_outgoerpeeps_dead

        self.print_total_statistics()


    def print_location_info(self):
        self.peepTown.peepHome.print_info(True)
        self.peepTown.groceryStore.print_info(True)
        self.peepTown.cityPark.print_info(True)
        self.peepTown.businessCenter.print_info(True)
        self.peepTown.nightClub.print_info(True)
        self.peepTown.hospital.print_info(True)


    def print_total_statistics(self):
        print("===========================")
        print(f'Statistics')
        print(f'- Number of Infected Peeps: {self.infection_toll_total}')

        print(f'- Death Toll: {self.death_toll_total}')
        print(f'- Death Toll HBP: {self.death_toll_homebodypeeps}')
        print(f'- Death Toll SHP: {self.death_toll_semihomiespeeps}')
        print(f'- Death Toll OGP: {self.death_toll_outgoerpeeps}')

        print(f'- Percentage of HBP dead: {self.per_homebodypeeps_dead}')
        print(f'- Percentage of SHP dead: {self.per_semihomiespeeps_dead}')
        print(f'- Percentage of OGP dead: {self.per_outgoerpeeps_dead}')

        print(f'- Percentage of HBP live: {self.per_homebodypeeps_live}')
        print(f'- Percentage of SHP live: {self.per_semihomiespeeps_live}')
        print(f'- Percentage of OGP live: {self.per_outgoerpeeps_live}')

        print('')

    
    def run_program(self):
        self.run_roll()
        self.get_total_statistics()