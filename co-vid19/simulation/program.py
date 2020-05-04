from rollsystem import RollSystem

if __name__ == "__main__":
    
    for _ in range(300):
        rollsystem = RollSystem(n_peeps=1000, n_rolls=1000)
        rollsystem.run_program()