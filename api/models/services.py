from api.models import db,ma

#Services Model
class Services(db.Model):
    sId = db.Column(db.Integer, primary_key=True)
    serviceName = db.Column(db.String(100))
    pinIn = db.Column(db.Integer)
    pinOut = db.Column(db.Integer)
    createdDate = db.Column(db.String(100))
    createdBy = db.Column(db.String(100))
    updatedDate = db.Column(db.String(100))
    updatedBy = db.Column(db.String(100))

    def __init__(self,serviceName,pinIn,pinOut,createdDate, createdBy, updatedDate, updatedBy):
        self.serviceName = serviceName
        self.pinIn = pinIn
        self.pinOut = pinOut
        self.createdDate = createdDate
        self.createdBy = createdBy
        self.updatedDate = updatedDate
        self.updatedBy = updatedBy

# Product Schema
class ServicesSchema(ma.Schema):
  class Meta:
    fields = ('serviceName','pinIn','pinOut','createdDate', 'createdBy', 'updatedDate', 'updatedBy')

# Init schema
service_schema = ServicesSchema()
services_schema = ServicesSchema(many=True)