from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int = field(default=16, init=False)
    children: list = field(default_factory=lambda: [])

    def is_minor(self):
        return self.age < 18


p1 = Person('Shola')
print(p1)
