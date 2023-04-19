# Get input of the athlete's first name, last name, location, and times for each discipline
first_name = input("first name: ")
last_name = input("last name: ")
location = input("location: ")
# For swim, cycle and run, translate the input into int
swim_time = int(input("swim time（s): "))
cycle_time = int(input("cycle time(s): "))
run_time = int(input("run time(s): "))

# Create a data_of_Triathlon class to record information about an athlete's performance in a triathlon competition.
class data_of_Triathlon:
    # The __init__ method is called when an instance of the class is created
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        # Initialise the attributes of the object using the values supplied as inputs
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        # Calculate the total time by adding the times for each discipline
        self.total_time = swim_time + cycle_time + run_time

# Using the provided values, create an instance of the data_of_Triathlon class.
athlete_data = data_of_Triathlon(first_name, last_name, location, swim_time, cycle_time, run_time)
# Print the athlete's details with f'string
print(f'{athlete_data.first_name} {athlete_data.last_name} locate in {athlete_data.location}. Swim: {athlete_data.swim_time}s Cycle: {athlete_data.cycle_time}s Run: {athlete_data.run_time}s Total: {athlete_data.total_time}s')