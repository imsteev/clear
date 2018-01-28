class Carrier(object):
    def __init__(self):
        pass
    
    def track(self, id):
        pass

class UPS(Carrier):
    name = "UPS"

    def __init__(self):
        super(UPS,self).__init__()
    
    def track(self, id):
        pass

class Fedex(Carrier):
    name = "Fedex"

    def __init__(self):
        super(Fedex,self).__init__()
    
    def track(self, id):
        pass

class USPS(Carrier):
    name = "USPS"

    def __init__(self):
        super(USPS, self).__init__()
    
    def track(self, id):
        pass