class Address:
    """All the properties of an address"""

    street_address_line_1 = ""
    street_address_line_2 = ""
    city = ""
    state = ""
    zip = ""

    def set_address(self):
        self.set_street_address(self)

    def set_street_address(self):
        while True:
            sal1 = input("Street Address Line 1 (required): ")
            if sal1 == ':q':
                break
            elif sal1 != "":
                self.street_address_line_1 = sal1
                break
            else:
                print("\nStreet Address Line 1 is required. Type :q and the press enter quit entering the address.\n")

    def display(self):
        print(f"\n{self.street_address_line_1}\n")
