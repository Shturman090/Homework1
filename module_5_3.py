class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for new_floor in range(new_floor + 1):
                if new_floor < 1:
                    continue
                print(new_floor)

    def __len__(self):
         return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

#_______________________________________________________________________________________
       #1
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

       #2
    def __lt__(self, value):
        return self.number_of_floors < value.number_of_floors

    def __le__(self, value):
        return self.number_of_floors <= value.number_of_floors

    def __gt__(self, value):
        return self.number_of_floors > value.number_of_floors

    def __ge__(self, value):
        return self.number_of_floors >= value.number_of_floors

    def __ne__(self, value):
        return self.number_of_floors != value.number_of_floors

       #3
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

       #4
    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        return self + value

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # module_5_2
print(h2)  # module_5_2

print(h1 == h2) # __eq__

h1 = h1 + 10 #__add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__