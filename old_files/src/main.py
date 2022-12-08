'''
Placeholder Doc String
'''

import typing

#
# Demo imports from module and package
#
from gnome_basic import gnome_name as name

print(name)


class Pet:
    '''Docstring'''

    def __init__(self, name: str, animal: str):
        '''Docstring'''
        self.name = name
        self.animal = animal

    def who_am_i(self: "Pet") -> None:
        '''Docstring'''
        print("\n"+self.name+" is a "+self.animal+"\n\n")


pet1: Pet = Pet("Scooby", "Dog")
pet1.who_am_i()

pets: typing.List[Pet] = [pet1, Pet("Garfield", "Cat")]
names: typing.List[str] = [item.name for item in pets]
print(names)
