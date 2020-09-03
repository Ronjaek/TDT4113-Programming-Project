"""Funksjonene kalkulatoren skal støtte"""
import numbers
import numpy


class Function:

    def __init__(self, func):
        """Instansen bindes opp mot funksjonen som gir som input"""
        self.func = func

    def execute(self, element, debug=True):
        """sjekker at den mottar et tall"""

        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)

        if debug is True:
            print("Function: " + self.func.__name__
                  + "({:f}) = {:f}".format(element, result))

        return result


"""
exponential_func = Function(numpy.exp)
sin_func = Function(numpy.sin)
print(exponential_func.execute(sin_func.execute(0)))
"""
