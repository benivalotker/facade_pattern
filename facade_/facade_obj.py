from .system_obj import (
        DisplayUnit, 
        Memory, 
        ProcessingUnit
    )

# facade
class Computer:
    def __init__(self):
        self.processingUnit = ProcessingUnit()
        self.displayUnit = DisplayUnit()
        self.memory = Memory()
 
    def bootUp(self):
        self.processingUnit.process()
        self.memory.ioOperation()
        self.displayUnit.display()