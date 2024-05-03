class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware
    
    def update_firmware(self):
        print("Getting update from server")
        self._firmware += 1

# All attributes in Python are public by default which means they can be accessed and overridden
iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)


iphone.update_firmware()
print(iphone._firmware)