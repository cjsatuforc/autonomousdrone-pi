from dronekit import VehicleMode
from sg.nus.iss.autonomousdrone.vehicle.vehicle import Vehicle

class FlightCommands:

    TIME_TO_COLLISION = 10

    def __init__(self):
        # Check for correct input
        vehicle = Vehicle()
        if isinstance(vehicle, Vehicle) is False:
            raise TypeError('Expected object of type Vehicle, got '+type(vehicle).__name__)
        self.__vehicle = vehicle

    def arm(self):
        self.__vehicle.mode = VehicleMode("STABILIZE")
        self.__vehicle.armed = True
        print "Armed!"
        return

    def disarm(self):
        if (None!=self.__vehicle and self.__vehicle.armed):
            self.__vehicle.armed = False
            return

    # Order the drone to land.
    def land(self):
        self.__vehicle.landing()
        return

    # Order the drone to maintain altitude
    def maintain_altitude(self):
        self.__vehicle.keep_altitude()
        return

    # Order the drone to fly to the left side
    def go_left(self):
        self.__vehicle.move_left()
        return

    # Order the drone to fly to the right side
    def go_right(self):
        self.__vehicle.move_right()
        return

    def go_back(self):
        self.__vehicle.move_backward()

    # Order the drone to ascend
    def go_up(self):
        self.__vehicle.move_up()
        return

    # Order the drone to decend
    def go_down(self):
        self.__vehicle.move_down()
        return

    def go_front(self):
        self.__vehicle.move_foreword()

    # Order the drone to slow down in order to give it enough time to perform avoidance maneuvers.
    def slow_down(self, distance):
        if isinstance(distance, float) is False and isinstance(distance, int) is False:
            raise TypeError('Expected variable of type float and got a variable of type ' + type(distance).__name__)
        elif distance <= 0:
            raise ValueError('Illegal value. Cannot be 0')

        #  # Calculating a new velocity for the drone to give it 10 seconds before colliding. 10 Seconds should be
        #  # a sufficient amount of time to avoid colliding with the detected object.
        #
        velocity = distance/self.TIME_TO_COLLISION
        self.__vehicle.set_groundspeed(velocity)
        return

    # Order the drone to change its destination to its dock.
    def go_back_to_base(self):
        print("Destination changed: going back home")
        self.__vehicle.get_back_to_station()
