from api.models import db,ma

#User Model
class Status(db.Model):
    stsId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publicId = db.Column(db.String)
    sId = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    currentDate = db.Column(db.String(80))
    futureDate = db.Column(db.String(80))

    def __init__(self, publicId, sId, status, currentDate, futureDate):
        self.publicId = publicId
        self.sId = sId
        self.status = status
        self.currentDate = currentDate
        self.futureDate = futureDate

class StatusSchema(ma.Schema):
  class Meta:
    fields = ('publicId', 'sId','status', 'currentDate', 'futureDate')

# Init schema
status_schema = StatusSchema()
statuss_schema = StatusSchema(many=True)