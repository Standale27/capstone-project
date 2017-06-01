
from collections import defaultdict

class Compound(object):
    names = {"C": "Carbon", "Fe": "Iron", "O": "Oxygen", "S":"Sulfur", "H":"Hydrogen"}

    def __init__(self, text): #this method counts the number of elements in each compound
        self.elements = defaultdict(lambda: 0)
        element = ""
        num = ""
        for c, c_next in zip(text, text[1:]+"$"): #iterates through a string using a character and the one after
            if c.isalpha():
                element+= c
                if c_next.isupper() or c_next == "$": #checks if the next character is a new element or if it is at the end
                    self.elements[element] += 1 #adds 1 to a counter, helps count the number of each element
                    element = ""; num = ""
            else: #if c is a number
                num += c
                if c_next == "$" or not c_next.isdigit(): #checks to see if the next character is at the end or not a digit
                    self.elements[element] = int(num) #sets counter equal to the character to help count each element
                    element = ""; num = ""
        if num is not "":
            self.elements[element] = int(num)

    def __add__(self, other):
        pass

    def __str__(self):
        return "".join([f"{self.names[k]}: {v}\n" for (k,v) in self.elements.items()])

def is_balanced(cmpd1, cmpd2, cmpd3):
    pass


if __name__ == "__main__":
    while True:
        user_string = input("Enter Compound Formula:")
        cmpd = Compound(user_string)
        print(cmpd)
