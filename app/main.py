class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if person.get("wife") is not None:
            person_name = person["wife"]
            curent_person = Person.people[person_name]
            curent_person.husband = Person.people[person["name"]]
        elif person.get("husband") is not None:
            person_name = person["husband"]
            curent_person = Person.people[person_name]
            curent_person.wife = Person.people[person["name"]]
    return list(Person.people.values())
