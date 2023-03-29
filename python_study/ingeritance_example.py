class ParentClass:
    def printHello(self):
        print("Hello, world !")


class ChildClass(ParentClass):
    def some_new_method(self):
        print("ParentClass objects don't have this method.")


class GrandchildClass(ChildClass):
    def another_new_method(self):
        print("Only GrandchildClass objects have this method.")


print("Create ParentClass object and call it's methods:")
parent = ParentClass()
parent.printHello()

print("Create ChildClass object and call it's methods:")
child = ChildClass()
child.printHello()
child.some_new_method()

print("Create GrandchildClass object and call it's methods:")
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.some_new_method()
grandchild.another_new_method()

print("An error:")
parent.some_new_method()
