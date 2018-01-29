from google.appengine.ext import ndb

class Shipment(ndb.Model):
    name = ndb.StringProperty()
    tracking_id = ndb.StringProperty()
    carrier = ndb.StringProperty()
    #description = ndb.StringProperty()

    def to_dict(self):
        return {
            "tracking_id": str(self.tracking_id),
            "carrier": str(self.carrier),
            "name": str(self.name)
        }