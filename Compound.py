from collections import defaultdict
import periodictable as pt

class Compound(object):
    names = {el.symbol: el for el in pt.elements}

    def __init__(self, text): #this method counts the number of elements in each compound
        self.coeff = int(text[0]) if len(text) > 0 and text[0].isdigit() else 1
        self.text = text if self.coeff == 1 else text[1:]
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

    def __add__(self, other): #creates a temporary Compound in which both dictionaries of 2 compounds are added
        if other is None:
            return self
        t = self.copy()
        new_t = defaultdict(lambda: 0) #need to resolve coefficients
        for key,value in other.elements.items():
            new_t[key] += other.coeff*value
        for key,value in t.elements.items():
            new_t[key] += t.coeff*value
        t.coeff = 1 #reset coefficient to 1 now that they've been resolved
        t.elements = new_t
        return t

    def __rmul__(self, c):
        t = self.copy()
        t.coeff *= c
        return t

    def copy(self):
        n = Compound('')
        n.text = self.text
        n.elements = self.elements
        n.coeff = self.coeff
        return n

    def list(self):
        return "".join([f"{self.names[k].name}: {v*self.coeff}\n" for (k,v) in self.elements.items()])

    def __str__(self):
        if self.coeff is not 1:
            return str(self.coeff)+self.text
        else:
            return self.text

    def __eq__(self, other):
        for k,v in self.elements.items():
            if other.coeff*other.elements[k] != self.coeff*v:
                return False
        return True

def is_balanced(cmpd1, cmpd2, cmpd3, cmpd4=None):
    return (cmpd1 + cmpd2) == (cmpd3 + cmpd4)

def lcm(cmpds): #https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b #this is done so both actions are performed simultaneously
            return a
    def lcm(t):
        if len(t) == 2:
            t0 = t[0].coeff
            t1 = t[1] if isinstance(t[1], float) else t[1].coeff
            return t0 * t1 / gcd(t0, t1)
        t0, *t_ = t
        return lcm([t0, lcm(t_)])
    return lcm(cmpds)

if __name__ == "__main__":
    input1 = input('Enter Compound 1: ')
    input2 = input('Enter Compound 2: ')
    input3 = input('Enter Compound 3: ')

    cmpd1 = Compound(input1)
    cmpd2 = Compound(input2)
    cmpd3 = Compound(input3)

    print("\nReactants:")
    print((cmpd1+cmpd2).list())
    print("Products:")
    print(cmpd3.list())

    print(
        f"{cmpd1} + {cmpd2} => {cmpd3} is balanced\n"
        if is_balanced(cmpd1, cmpd2, cmpd3) else
        f"{cmpd1} + {cmpd2} => {cmpd3} is not balanced\n"
        )
