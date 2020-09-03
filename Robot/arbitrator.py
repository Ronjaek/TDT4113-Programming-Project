import random
class Arbitrator:
    """This class decides which behavior that wins"""

    def choose_action(self, behaviors):
        winner = None
        maximum_weight = 0.0
        for behavior in behaviors:
            if behavior.weight > maximum_weight:
                maximum_weight = behavior.weight
                winner = behavior

        """Check all active behaviors and pick a winner"""
        """weight_range_array = []
        winner = None
        maximum_weight = 0.0
        for behavior in behaviors:
            old_max = maximum_weight
            maximum_weight += behavior.weight

            array_range = [old_max, maximum_weight]
            weight_range_array.append(array_range)

        number = random.uniform(0.0, maximum_weight)

        for array in weight_range_array:
            if number >= array[0] and number <= array[1]:
                print("The number is in behavior", weight_range_array.index(array))
                winner = behaviors[weight_range_array.index(array)]"""

        return winner.motor_recommendations, winner.halt_request
