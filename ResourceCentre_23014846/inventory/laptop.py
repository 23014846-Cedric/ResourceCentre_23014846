class Laptop(): 
    # Refactor (E): Extract duplicate attributes and methods.
    # There are several common attributes and methods in 
    # Camera.py and Laptop.py. Extract these common attributes 
    # and methods into a super class, named item.py 
    def __init__(self, assetTag, description, os): 
        self._assetTag = assetTag 
        self._description = description 
        self._dueDate = "" 
        self._isAvailable = True 
        self._os = os 
        
    def getAssetTag(self): 
        return self._assetTag 
    
    def getDescription(self): 
        return self._description 
    
    def getDueDate(self): 
        return self._dueDate 
    
    def getIsAvailable(self): 
        if self._isAvailable: 
            return "Yes"
        else: 
            return "No" 
        
    def getOS(self): 
        return self._os 
    
    def setDueDate(self, dueDate): 
        self._dueDate = dueDate 
        
    def setIsAvailable(self, isAvailable): 
        self._isAvailable = isAvailable