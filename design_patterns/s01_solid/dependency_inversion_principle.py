# Dependency Inversion Principle
from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): ...

class Relationships(RelationshipBrowser):  # Low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )

        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research: # High-level -> depend on abstract or interface
    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of("Tho"):
            print(f"Tho has a child called {p}.")


parent = Person("Tho")
child1 = Person("Khoi")
child2 = Person("Quan")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)


Research(relationships)
