class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[0, 0]] * len(position)

        # Make array with both pos and speed
        for i in range(len(position)):
            cars[i] = [position[i], speed[i]]
        
        # Sort the array by position
        cars.sort(key=lambda x: x[0], reverse = True)

        # Calculate time to target for each car
        for i in range(len(cars)):
            cars[i].append((target - cars[i][0])/cars[i][1])

        # cars[[position, speed, hrstotarget]]

        # Figure out number of fleets by checking if the time to target is the current limiting fator, and if something else becomes limiter, add a fleet and update limiting speed.
        limitingtime = 0
        fleets = 0

        for i in range(len(cars)):
            if cars[i][2] > limitingtime:
                fleets += 1
                limitingtime = cars[i][2]

        return fleets