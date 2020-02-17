from api.models import db, ma
#User Model
class User(db.Model):
    uId = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(100))
    contact = db.Column(db.Integer)
    email = db.Column(db.String(200),unique=True)
    username = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(200))
    token = db.Column(db.String(200))
    createdDate = db.Column(db.String(80))
    createdBy = db.Column(db.String(80))
    updatedDate = db.Column(db.String(80))
    updatedBy = db.Column(db.String(80))

    def __init__(self,fullName,contact,email,username,password,token,createdDate,createdBy,updatedDate,updatedBy):
        self.fullName = fullName
        self.contact = contact
        self.email = email
        self.username = username
        self.password = password
        self.token = token
        self.createdDate =createdDate
        self.createdBy = createdBy
        self.updatedDate = updatedDate
        self.updatedBy = updatedBy

class UserSchema(ma.Schema):
  class Meta:
    fields = ('fullName','contact','email','username','password','token','createdDate','createdBy','updatedDate','updatedBy')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)