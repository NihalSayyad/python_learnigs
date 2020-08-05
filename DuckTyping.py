
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)