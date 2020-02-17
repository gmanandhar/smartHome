from flask_restful import Resource
import logging as logger
from api.models import Status as sts
from flask  import request, jsonify


class GetStatusById(Resource):
    def get(self,id):
        logger.debug("Inside the get method")
        status_instance = sts.Status.query.get(id)
        return sts.status_schema.jsonify(status_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetStatus(Resource):
    def get(self):
        logger.debug("Inside the get method")
        all_status = sts.Status.query.all()
        result = sts.statuss_schema.dump(all_status)
        return jsonify(result)

class AddStatus(Resource):
    def post(self):
        logger.debug("Inside the POST method")
        uId= request.json['uId']
        sId= request.json['sId']
        status= request.json['status']
        currentDate= request.json['currentDate']
        futureDate= request.json['futureDate']

        new_status = sts.Status(uId, sId, status,currentDate,futureDate)
        sts.db.session.add(new_status)
        sts.db.session.commit()

        return sts.status_schema.jsonify(new_status)

class DeleteStatus(Resource):
    def get(self,id):
        status_del = sts.Status.query.get(id)
        sts.db.session.delete(status_del)
        sts.db.session.commit()

        return sts.status_schema.jsonify(status_del)