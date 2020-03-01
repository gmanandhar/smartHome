from flask_restful import Resource
import logging as logger
from api.models import service as svc
from flask  import request, jsonify
from  .token import Token
import datetime


class GetServiceById(Resource):
    @Token.token_required
    def get(self,current_user,id):
        logger.debug("Inside the get method")
        service_instance = svc.Service.query.get(id)
        return svc.service_schema.jsonify(service_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetService(Resource):
    @Token.token_required
    def get(self,current_user):
        logger.debug("Inside the get method")
        all_users = svc.Service.query.all()
        result = svc.services_schema.dump(all_users)
        return jsonify(result)

class AddService(Resource):
    @Token.token_required
    def post(self,current_user):
        logger.debug("Inside the POST method")
        data = request.get_json()
        svcName=data['svcName']
        pinIn=data['pinIn']
        pinOut=data['pinOut']

        new_service = svc.Service(svcName, pinIn, pinOut,datetime.datetime.utcnow(),data['username'],datetime.datetime.utcnow(),data['username'])
        svc.db.session.add(new_service)
        svc.db.session.commit()

        return svc.service_schema.jsonify(new_service)

class DeleteService(Resource):
    @Token.token_required
    def get(self,current_user,id):
        service_del = svc.Service.query.get(id)
        svc.db.session.delete(service_del)
        svc.db.session.commit()

        return svc.service_schema.jsonify(service_del)
#Method to update User
class UpdateUser(Resource):
    @Token.token_required
    def put(self,current_user,id):
        service = svc.Service.query.get(id)
        data = request.get_json()
        svcName = data['svcName']
        pinIn = data['pinIn']
        pinOut = data['pinOut']
        updatedDate = datetime.datetime.utcnow()
        service.svcName =svcName
        service.pinIn =pinIn
        service.pinOut = pinOut
        service.updatedDate = updatedDate
        service.db.session.commit()
        return svc.ServicesSchema.jsonify(service)