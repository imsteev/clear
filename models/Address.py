class Address(object):
    def __init__(self, name, street1, zipcode, country, street2=None):
        self.name = name
        self.street1 = street1
        self.street2 = street2
        self.zipcode = zipcode
        self.country = country