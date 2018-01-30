from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()

    is_authenticated = True
    is_active = True
    is_anonymous = False
    
    def get_id(self):
        return unicode(self.username)

