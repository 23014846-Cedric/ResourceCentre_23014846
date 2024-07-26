from inventory.item import item
class Camera(item):
# Refactor (E): Extract duplicate attributes and methods.
# There are several common attributes and methods in
# Camera.py and Laptop.py. Extract these common attributes
# and methods into a super class, named item.py
    def __init__(self, assertTag, description, opticalZoom):
        super().__init__(assertTag, description)
        self._opticalZoom = opticalZoom

    def getOpticalZoom(self):
        return self._opticalZoom
    def setDueDate(self, dueDate):
        self._dueDate = dueDate
    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable
        
    def __str__(self):
        return super().__str__()\
        +"{:<10}\n".format(self.getOpticalZoom())
        
    