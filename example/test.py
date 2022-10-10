from ClassHandler import *

class Person(Table):
    def __init__(self, halo = "halo", umur):
        ## Record default value ##
        super().__init__()
        self.id = variable(Type.INTEGER(), 0, {"AUTO INCREMENT", "UNIQUE"})
        self.salam = variable("VARCHAR(50)", halo)
        self.umur = variable("INT", umur)
        self.ada = variable("BOOL", None)

testController = persistClass(Person)

testController.select()
