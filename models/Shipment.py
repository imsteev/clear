class Shipment(object):
    def __init__(self, trackingid, carrier, description=None):
        self.trackingid = trackingid
        self.carrier = carrier
        self.description = description
    
    def getTrackingId(self):
        return self.trackingid
