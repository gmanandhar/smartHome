from api.models import db,ma
#User Model
class UserMapping(db.Model):
    umId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publicId = db.Column(db.String(200))
    sId = db.Column(db.Integer)
    read = db.Column(db.Boolean, default=False, server_default="false")
    write = db.Column(db.Boolean, default=False, server_default="false")
    delete = db.Column(db.Boolean, default=False, server_default="false")
    createdDate = db.Column(db.String(80))
    createdBy = db.Column(db.String(80))
    updatedDate = db.Column(db.String(80))
    updatedBy = db.Column(db.String(80))

    def __init__(self, publicId, sId, read, write, delete, createdDate, createdBy, updatedDate, updatedBy):
        self.publicId = publicId
        self.sId = sId
        self.read = read
        self.write = write
        self.delete = delete
        self.createdDate = createdDate
        self.createdBy = createdBy
        self.updatedDate = updatedDate
        self.updatedBy = updatedBy

class UserMappingSchema(ma.Schema):
  class Meta:
    fields = ('publicId','sId','read','write','delete','createdDate','createdBy','updatedDate','updatedBy')

# Init schema
userMap_schema = UserMappingSchema()
userMaps_schema = UserMappingSchema(many=True)