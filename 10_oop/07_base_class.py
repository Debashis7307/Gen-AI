class Chai:                                     # Base class
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):                   # Subclass -> code duplication
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        

# class GingerChai(Chai):            # Subclass -> explicitly calling the base class constructor
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):         # Subclass -> using super() to call the base class constructor
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level