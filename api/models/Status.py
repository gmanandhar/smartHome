from api.models import db,ma

#User Model
class Status(db.Model):
    stsId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uId = db.Column(db.Integer)
    sId = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    currentDate = db.Column(db.String(80))
    futureDate = db.Column(db.String(80))

    def __init__(self, uId, sId, status, currentDate, futureDate):
        self.uId = uId
        self.sId = sId
        self.status = status
        self.currentDate = currentDate
        self.futureDate = futureDate

class StatusSchema(ma.Schema):
  class Meta:
    fields = ('uId', 'sId','status', 'currentDate', 'futureDate')

# Init schema
status_schema = StatusSchema()
statuss_schema = StatusSchema(many=True)