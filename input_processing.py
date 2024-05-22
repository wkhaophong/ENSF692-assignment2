# input_processing.py

# Warisa Khaophong, ENSF 692 P24

# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

# No global variables are permitted

class SensorMenuOption:
    """
    A class containing constants for sensor menu options.
    
    Attributes:
        TERMINATE (int): Constant for terminating the program.
        TRAFFIC_LIGHT (int): Constant for updating traffic light status.
        PEDESTRIAN (int): Constant for updating pedestrian status.
        VEHICLE (int): Constant for updating vehicle status.
    """
    TERMINATE = 0      
    TRAFFIC_LIGHT = 1
    PEDESTRIAN = 2
    VEHICLE = 3

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    # Must include a constructor that uses default values
    def __init__(self):
        self.traffic_light = "green"
        self.has_pedestrian = "no"
        self.has_vehicle = "no"
          
    def _validate_input(self, menu_input, status_input):
        """
        Validates the input for menu and status.

        Args:
            menu_input (int): The type of input (traffic light, pedestrian, vehicle).
            status_input (str): The status input for the sensor.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        if menu_input == SensorMenuOption.TRAFFIC_LIGHT and status_input in ["green", "yellow", "red"]:
            return True
        elif menu_input == SensorMenuOption.PEDESTRIAN and status_input in ["yes", "no"]:
            return True
        elif menu_input == SensorMenuOption.VEHICLE and status_input in ["yes", "no"]:
            return True
        return False

    def update_status(self, menu_input, status_input):
        """
        Updates the current sensor status based on provided inputs.

        Args:
            menu_input (int): The type of input (traffic light, pedestrian, vehicle).
            status_input (str): The status input for the sensor.
        """
        if not self._validate_input(menu_input, status_input):
            print("Invalid vision change.")
            return
        
        if menu_input == SensorMenuOption.TRAFFIC_LIGHT:
            self.traffic_light = status_input
        elif menu_input == SensorMenuOption.PEDESTRIAN:
            self.has_pedestrian = status_input
        elif menu_input == SensorMenuOption.VEHICLE:
            self.has_vehicle = status_input
    
    def get_action_message(self):
        """
        Generates an action message based on sensor status.

        Returns:
            str: Action message ("STOP", "Proceed", "Caution").
        """
        if self.traffic_light == "red" or self.has_pedestrian == "yes" or self.has_vehicle == "yes":
            return "STOP"
        elif self.traffic_light == "green" and self.has_pedestrian == "no" and self.has_vehicle == "no":
            return "Proceed"
        elif self.traffic_light == "yellow" and self.has_pedestrian == "no" and self.has_vehicle == "no":
            return "Caution"
  
def print_message(sensor):
    """
    Prints the action message and current status of the sensor.

    Args:
        sensor (Sensor): The sensor object containing current status.
    """
    action_message = sensor.get_action_message()
    print(f"\n{action_message}\n")
    print(f"Light = {sensor.traffic_light} , Pedestrian = {sensor.has_pedestrian} , Vehicle = {sensor.has_vehicle} .\n")

# Main function to run the program
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    
    while True:
        try:
            print("Are changes are detected in the vision input?")
            menu_input = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
            if menu_input in [SensorMenuOption.TRAFFIC_LIGHT, SensorMenuOption.PEDESTRIAN, SensorMenuOption.VEHICLE]:
                status_input = input("What change has been identified?: ")
                sensor.update_status(menu_input, status_input)
            elif SensorMenuOption.TERMINATE == 0:
                break
            else:
                raise ValueError
            print_message(sensor)
        except ValueError:
            print("You must select either 1, 2, 3, or 0", end="\n\n")

# No additional code should be included below this
if __name__ == '__main__':
    main()
