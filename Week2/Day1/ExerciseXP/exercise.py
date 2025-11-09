class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def find_oldest_cat(cat1, cat2, cat3):
        list_of_cats = [cat1, cat2, cat3]
        ages = []
        for cat in list_of_cats:
            ages.append(cat.age)
        print(max(ages))
            

cat1 = Cat("James", 90)
cat2 = Cat("Rio", 65)
cat3 = Cat("Coffee", 5)

Cat.find_oldest_cat(cat1=cat1, cat2=cat2, cat3=cat3)