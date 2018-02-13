import requests
import xmltodict
import json

class USPSClient(object):
    USERID = None
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
<TrackFieldRequest USERID="%s">
  <Revision>1</Revision>
  <ClientIp>111.0.0.1</ClientIp>
  <SourceId>source</SourceId>
  <TrackID ID="%s" />
</TrackFieldRequest>"""

    def __init__(self, client_id):
        self.USERID = client_id

    def track(self, tracking_id):
        endpoint = "http://production.shippingapis.com/ShippingAPI.dll"
        headers = {'Content-Type': 'application/xml'}
        data = { 
            "API": 'TrackV2',
            'XML': self.xml % (self.USERID, tracking_id)
        }

        r = requests.post(endpoint, data=data, headers=headers)
        output = xmltodict.parse(r.content)

        return json.dumps(output)
