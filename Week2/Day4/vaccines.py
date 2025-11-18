import random

class Human():
    def __init__(self, id_number: str, name: str, age: int, priority: bool):
        self.blood_type =  random.choice(["A", "B", "AB", "O"])
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
        self.sorted_humans = sorted(self.humans, key=lambda human: (human.priority, human.age), reverse=True)
        self.sorted= self.sorted_humans

    def add_person(self, person):
        try:
                if person.age > 60 or person.priority == True:
                   self.humans.insert(0, person)
                else:
                    self.humans.append(person)
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
            index1 = self.find_in_queue(person1)
            index2 = self.find_in_queue(person2)

            if index1 is None or index2 is None:
                print("Provide people in the list.")
                return
            else:
                self.humans[index2], self.humans[index1] = self.humans[index1], self.humans[index2]
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
                list_with_bloodtype.append(person.name)
            else:
                continue
        if not list_with_bloodtype:
                return f"Nobody has this blood type"
        return list_with_bloodtype
    
    def __lt__(self):
        self.humans.priority==True

    def sort_by_age(self):
        return self.sorted

if __name__=="__main__":
    human1 = Human(id_number="01", name="james", age=20, priority=True)
    human2 = Human(id_number="02", name="Kris", age=90, priority=False)
    human3 = Human(id_number="03", name="Will", age=50, priority=True)
    human4 = Human(id_number="04", name="Micheal", age=35, priority=False)

    queue = Queue(humans=[human1, human2, human3])
    print(queue.add_person(person=human4))
    print(queue.find_in_queue(human2))
    print(queue.swap(human2, human4))
    #
    print(queue.get_next())
    print(queue.get_next_blood_type("AB"))
    print(queue.sort_by_age())