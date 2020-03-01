from api.models import db,ma

#Services Model
class Service(db.Model):
    svcId = db.Column(db.Integer, primary_key=True)
    svcName = db.Column(db.String(100))
    pinIn = db.Column(db.Integer)
    pinOut = db.Column(db.Integer)
    createdDate = db.Column(db.String(100))
    createdBy = db.Column(db.String(100))
    updatedDate = db.Column(db.String(100))
    updatedBy = db.Column(db.String(100))

    def __init__(self,svcName,pinIn,pinOut,createdDate, createdBy, updatedDate, updatedBy):
        self.svcName = svcName
        self.pinIn = pinIn
        self.pinOut = pinOut
        self.createdDate = createdDate
        self.createdBy = createdBy
        self.updatedDate = updatedDate
        self.updatedBy = updatedBy

# Product Schema
class ServicesSchema(ma.Schema):
  class Meta:
    fields = ('svcName','pinIn','pinOut','createdDate', 'createdBy', 'updatedDate', 'updatedBy')

# Init schema
service_schema = ServicesSchema()
services_schema = ServicesSchema(many=True)