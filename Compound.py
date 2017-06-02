
from collections import defaultdict

class Compound(object):
    names = {"C": "Carbon", "Fe": "Iron", "O": "Oxygen", "S":"Sulfur", "H":"Hydrogen"}

    def __init__(self, text): #this method counts the number of elements in each compound
        self.text = text
        self.elements = defaultdict(lambda: 0)
        self.parse()

    def parse(self):
        element = ""
        num = ""
        for c, c_next in zip(self.text, self.text[1:]+"$"): #iterates through a string using a character and the one after
            if c.isalpha():
                element+= c
                if c_next.isupper() or c_next == "$": #checks if the next character is a new element or if it is at the end
                    self.elements[element] += 1 #adds 1 to a counter, helps count the number of each element
                    element = ""; num = ""
            elif c.isdigit():
                num += c
                if c_next == "$" or not c_next.isdigit(): #checks to see if the next character is at the end or not a digit
                    self.elements[element] += int(num) #sets counter equal to the character to help count each element
                    element = ""; num = ""
            else:
                raise ValueError #if compound has a character that isn't a letter or digit, raise a ValueError

    def __add__(self, other):
        if other is None:
            return self
        return Compound(self.text + other.text)

    def __str__(self):
        return "".join([f"{self.names[k]}: {v}\n" for (k,v) in self.elements.items()])

    def __eq__(self, other):
        for k,v in self.elements.items():
            if other.elements[k] != v:
                return False
        return True

def is_balanced(cmpd1, cmpd2, cmpd3, cmpd4=None):
    return (cmpd1 + cmpd2) == (cmpd3 + cmpd4)


if __name__ == "__main__":
    cmpd1 = Compound("C2H5O2")
    cmpd2 = Compound("CO2")
    cmpd3 = Compound("C3H3O4")
    cmpd4 = Compound("H2")
    print(
        f"{cmpd1.text} + {cmpd2.text} => {cmpd3.text} + {cmpd4.text} is balanced"
        if is_balanced(cmpd1, cmpd2, cmpd3, cmpd4) else
        f"{cmpd1.text} + {cmpd2.text} => {cmpd3.text} + {cmpd4.text} is not balanced"
    )
