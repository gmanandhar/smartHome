from flask_restful import Resource
import logging as logger
from api.models import services as svc
from flask  import request, jsonify


class GetServiceById(Resource):
    def get(self,id):
        logger.debug("Inside the get method")
        service_instance = svc.Services.query.get(id)
        return svc.service_schema.jsonify(service_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetService(Resource):
    def get(self):
        logger.debug("Inside the get method")
        all_users = svc.Services.query.all()
        result = svc.services_schema.dump(all_users)
        return jsonify(result)

class AddService(Resource):
    def post(self):
        logger.debug("Inside the POST method")
        svcName=request.json['svcName']
        pinIn=request.json['pinIn']
        pinOut=request.json['pinOut']
        createdDate=request.json['createdDate']
        createdBy=request.json['createdBy']
        updatedDate=request.json['updatedDate']
        updatedBy=request.json['updatedBy']

        new_service = svc.Services(svcName, pinIn, pinOut,createdDate, createdBy, updatedDate,updatedBy)
        svc.db.session.add(new_service)
        svc.db.session.commit()

        return svc.service_schema.jsonify(new_service)

class DeleteService(Resource):
    def get(self,id):
        service_del = svc.Services.query.get(id)
        svc.db.session.delete(service_del)
        svc.db.session.commit()

        return svc.service_schema.jsonify(service_del)