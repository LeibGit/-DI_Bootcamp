from random import choice

class Human():
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type=["A", "B", "AB", "O"]):
        self.blood_type = choice(blood_type)
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
    
    def __str__(self):
        return f"Human(id: {self.id_number}, name: {self.name}, age: {self.age}, priority: {self.priority})"

    def __repr__(self):
        return self.__str__()
    
class Queue():
    def __init__(self, humans):
        self.humans = humans

    def add_person(self, person):
        try:
            if person in self.humans:
                if person.age > 60 or person.priority == True:
                    self.humans.insert(0, person)
        except ValueError:
            print("Enter a person from the list")
        finally:
            return self.humans
    
    def find_in_queue(self, person):
        try:
            for index, p in enumerate(self.humans):
                if p == person:
                    return index
        except ValueError:
            print("Enter a person from the list")
    
    def swap(self, person1, person2):
        try:
            if person1 in self.humans and person2 in self.humans:
                self.humans[person1], self.humans[person2] = self.humans[person2], self.humans[person1]
        except ValueError:
            print("Enter people from the list") 
        finally:
            return self.humans
    
    def get_next(self):
        return self.humans[0]

    def get_next_blood_type(self, blood_type):
        list_with_bloodtype = []
        for person in self.humans:
            if person.blood_type == blood_type:
                list_with_bloodtype.append(person)
        return list_with_bloodtype[0]
    
    def sort_by_age(self):
        return self.humans.sort(key=lambda obJ: (obJ.priority, obJ.age))

if __name__=="__main__":
    human1 = Human(id_number="01", name="james", age=20, priority=True)
    human2 = Human(id_number="02", name="Kris", age=90, priority=False)
    human3 = Human(id_number="03", name="Will", age=50, priority=True)
    human4 = Human(id_number="04", name="Micheal", age=35, priority=False)

    queue = Queue(humans=[human1, human2, human3, human4])
    print(queue.add_person(person=Human(id_number="04", name="Micheal", age=35, priority=False)))
    print(queue.find_in_queue(human1))
    print(queue.get_next())
    print(queue.get_next_blood_type("AB"))
    print(queue.sort_by_age())