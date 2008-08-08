from google.appengine.ext import db

class Pledge(db.Model):
  name = db.StringProperty(required=True)
  postcode = db.StringProperty(required=True)
  date = db.DateTimeProperty(auto_now_add=True)
  email = db.EmailProperty()
  mp = db.StringProperty()
  constituency = db.StringProperty()
  message = db.TextProperty(required=True)