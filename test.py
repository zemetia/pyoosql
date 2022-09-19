from ClassHandler import *

class Person(Table):
    def __init__(self, halo = "halo"):
        ## Record default value ##
        super().__init__()
        self.id = variable("INT", 0, {"AUTO INCREMENT", "UNIQUE"})
        self.salam = variable("VARCHAR(50)", halo)
        self.umur = variable("INT", 50)
        self.ada = variable("BOOL", None)

testController = persistClass(Person)

testController.select()
