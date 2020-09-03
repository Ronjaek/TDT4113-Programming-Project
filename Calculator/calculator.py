"""Hovedklassen i programmet"""
import numpy
import numbers
import re
from function import Function
from operator_ import Operator
from queue import Queue
from stack import Stack


class Calculator:

    def __init__(self):
        """gir kalkulatoren tilgang til regneartene og funksjonene"""

        # definerer funksjonene ved å linke dem til Python funksjoner
        self.functions = {"EXP": Function(numpy.exp),
                          "LOG": Function(numpy.log),
                          "SIN": Function(numpy.sin),
                          "COS": Function(numpy.cos),
                          "SQRT": Function(numpy.sqrt)}

        # definerer tilgjengelige operasjonenr, kobler de til Python funksjoner
        self.operators = {"PLUSS": Operator(numpy.add, 0),
                          "GANGE": Operator(numpy.multiply, 1),
                          "DELE": Operator(numpy.divide, 1),
                          "MINUS": Operator(numpy.subtract, 0)}

        # definerer output-queue
        self.output_queue = Queue()

    def rpn(self):
        """Regneoppgavene kommer inn som en køen output_queue"""

        operator_stack = Stack()

        for i in range(self.output_queue.size()):

            # går gjennom hvert element i køen ved å popé dem av en etter en
            element = self.output_queue.pop()

            if isinstance(element, numbers.Number):
                # hvis elementet er et tall skal det pushes på stacken
                operator_stack.push(element)

            elif isinstance(element, Function):
                # hvis funksjon- popé av stacken og evaluere funksjonen med elementet
                result = element.execute(operator_stack.pop())
                # legger så resultatet til i stacken
                operator_stack.push(result)

            elif isinstance(element, Operator):

                #popér to elementer av stacken
                element2 = operator_stack.pop()  # det som popes først er siste tall
                element1 = operator_stack.pop()  # det som popes sist er det første

                result = element.execute(element1, element2)

                # pusher det nye resultatet tilbake på stacken
                operator_stack.push(result)

            else:
                # dersom verdien er verken tall, operator eller funksjon
                print("Something is wrong with your RPN-queue")
                break
        if not (self.output_queue.size() == 0 and operator_stack.size() == 1):
            print("Something is wrong - output_queue should have been empty and operator stack should have one item")

        return operator_stack.pop()  # returnerer siste elementet på stacken

    def normal_calculator(self, elements):
        """får en streng som input, og oversetter til RPN"""

        # bruker shinting-yard algoritmen
        output_queue = Queue()  # oppretter en output queue som metoden skal returnere
        operator_stack = Stack()  # en stack for mellom-lagring for at ordningen av elementer skal bli riktig

        for element in elements:

            if isinstance(element, numbers.Number):

                output_queue.push(element)  # legger til tallet i ouput_queue
                print("numb", output_queue)

            # sjekker om er av type Functiton, kaller ikke på klassen Function()
            elif isinstance(element, Function):

                operator_stack.push(element)  # legger det til i operator_stack
                print("func", operator_stack)

            elif element == "(":

                operator_stack.push(element)  # pushes på operator_stack
                print("(", operator_stack)

            elif element == ")":

                # iterer gjennom operator_stack og legger til elementene i output-køen
                while operator_stack.peek() != "(" and operator_stack.size() != 0:
                    operator = operator_stack.pop()
                    output_queue.push(operator)
                operator_stack.pop()  # fjerner "(" og gjør ingenting med ")"
                print(")", "oper: ", operator_stack, "out:", output_queue)

            elif isinstance(element, Operator):

                # må sortere de fire regneartene på riktig sted
                while operator_stack.size() != 0:
                    # bruker peek for å sjekke om topp-elementet skal flyttes over til output_stack eller ikke
                    if isinstance(operator_stack.peek(), Operator):
                        if operator_stack.peek().strength < element.strength:
                            break  # stopper dersom styrken er mindre
                    if operator_stack.peek() == "(" or operator_stack.peek() == ")":
                        # stopper while-løkken dersom man kommer til en parantes
                        break

                    temp = operator_stack.pop()
                    output_queue.push(temp)

                # tar til slutt å pusher elementet på operator_stack
                operator_stack.push(element)
                print("operator", operator_stack)

        # popér av hvert element på operator_stack og pusher den på output_queue
        for i in range(operator_stack.size()):

            element = operator_stack.pop()
            output_queue.push(element)

        print("the ouput", output_queue, output_queue.is_empty())
        print("the operator", operator_stack, operator_stack.is_empty())

        self.output_queue = output_queue  # setter self.output_queue til den som er laget her
        print(self.output_queue)

    def text_parser(self, text):
        """Mottar en tekststreng, og skal produsere en rpn ut ifra den"""

        # starter med å fjerne mellomrom og gjør den til uppercase
        text = text.replace(" ", "").upper()

        # metoden skal returnere en liste
        return_list = []

        # en nyttig shortcut i re.search -> kan lete etter flere sub-strenger samtidig
        functions = "|".join(["^" + func for func in self.functions.keys()])
        operators = "|".join(["^" + oper for oper in self.operators.keys()])
        paranthesis = "^[()]"
        nums = "^[-1234567890.]+"

        while text != "":

            check = re.search(nums, text)  # sjekker om det er et nummer
            print(check==None)
            if check != None:  # hvis check er None er det ingen match
                # check.__getitiem__(0) er teksten som matcher
                return_list.append(float(check.__getitem__(0)))  # gjør om tallet til float
                print(text)
                text = text[len(check.__getitem__(0))::]
                print("after", text)
                continue

            check = re.search(paranthesis, text)  # sjekker om det er en parantes
            if check != None:
                return_list.append(check.__getitem__(0))  # lar derimot parantesen forbli en streng
                print(text)
                text = text[1::]
                print("after", text)
                continue

            check = re.search(operators, text)  # sjekker om det er en operator
            print(check==None)
            if check != None:
                print(check.__getitem__(0))
                return_list.append(self.operators[check.__getitem__(0)])  # eks: append(self.operators["GANGE"])
                print(text)
                text = text[len(check.__getitem__(0))::]
                print("after", text)
                continue

            check = re.search(functions, text)  # sjekker om det er en function
            if check != None:
                return_list.append(self.functions[check.__getitem__(0)])  # eks: append(self.functions["EXP"])
                print(text)
                text = text[len(check.__getitem__(0))::]
                print(text)
                continue

            print("her skjer lite...")

        return return_list

    def test(self):

        text = input("Skriv inn en uttrykk som skal regnes ut: ")
        print(text)
        return_list = self.text_parser(text)
        print(return_list)
        self.normal_calculator(return_list)
        result = self.rpn()
        return result


calc = Calculator()
calc.test()


"""
# sjekker om instansieringen virker
calc = Calculator()
print(calc.functions["EXP"].execute(
    calc.operators["+"].execute(
        1, calc.operators["*"].execute(2, 3))))
"""

"""
# tester RPN
calc = Calculator()
calc.output_queue.push(1)
calc.output_queue.push(2)
calc.output_queue.push(3)
calc.output_queue.push(calc.operators["*"])
calc.output_queue.push(calc.operators["+"])
calc.output_queue.push(calc.functions["EXP"])
print(calc.rpn())
"""

"""
# tester fra "vanlig" notasjon til RPN
calc = Calculator()
e = calc.functions["EXP"]
add = calc.operators["+"]
multiply = calc.operators["*"]
test_list = [e, "(", 1, add, 2, multiply, 3, ")"]
calc.normal_calculator(test_list)
"""

"""
# tester tekst-parseren
calc = Calculator()
# text_input = "((15 DELE (7 MINUS (1 PLUSS 1))) GANGE 3) MINUS (2 PLUSS (1 PLUSS 1))"
text_input = "EXP(1 PLUSS 2 GANGE 3)"
return_list = calc.text_parser(text_input)
print(return_list)
calc.normal_calculator(return_list)
result = calc.rpn()
print(result)
"""
