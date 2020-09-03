"""pakker inn regneoperasjonene"""
import numbers


class Operator:

    def __init__(self, operator, strength):
        """Instansen bindes opp mot funksjonen som gir som input"""
        self.operator = operator
        self.strength = strength

    def get_strength(self):
        """Returnerer styrken til en operator"""
        return self.strength

    def execute(self, element1, element2):
        """sjekker at den mottar et tall"""

        # sjekker først at elementene som tas inn er tall
        if not (isinstance(element1, numbers.Number) and isinstance(element2, numbers.Number)):
            raise TypeError("Cannot execute func if element is not a number")

        result = self.operator(element1, element2)

        return result


"""
add_op = Operator(operator=numpy.add, strength=0)
multiply_op = Operator(operator=numpy.multiply, strength=1)
print(add_op.execute(1, multiply_op.execute(2, 3)))
"""
