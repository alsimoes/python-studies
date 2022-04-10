from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strenght: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strenght)


person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(person2)
print(person3)
print(person1 > person2)
