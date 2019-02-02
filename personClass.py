class Person:
    # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def incrementAge(self):
      self.age += 1

  def changeName(self, new_name):
      self.name = new_name

  def equals(self, other):
      if self.name == other.name and self.age == other.age:
          return 1
      else:
          return 0



if __name__ == "__main__":
    p1 = Person("John", 21)

    print(p1.name)
    print(p1.age)

    p1.incrementAge();
    p1.changeName("Evan")

    print(p1.name)
    print(p1.age)


    p2 = Person("Evan", 22)
    print(p2.name)
    print(p2.age)

    print(p1.equals(p2))
