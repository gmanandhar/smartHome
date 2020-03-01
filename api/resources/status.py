from flask_restful import Resource
import logging as logger
from api.models import Status as sts
from flask  import request, jsonify
from .token import Token
import datetime


class GetStatusById(Resource):
    @Token.token_required
    def get(self,current_user,id):
        logger.debug("Inside the get method")
        status_instance = sts.Status.query.get(id)
        return sts.status_schema.jsonify(status_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetStatus(Resource):
    @Token.token_required
    def get(self,current_user):
        logger.debug("Inside the get method")
        all_status = sts.Status.query.all()
        result = sts.statuss_schema.dump(all_status)
        return jsonify(result)

class AddStatus(Resource):
    @Token.token_required
    def post(self,current_user):
        logger.debug("Inside the POST method")
        publicId= Token.publicId(self)
        sId= request.json['sId']
        status= request.json['status']
        currentDate= datetime.datetime.utcnow()
        futureDate= request.json['futureDate']

        new_status = sts.Status(publicId, sId, status,currentDate,futureDate)
        sts.db.session.add(new_status)
        sts.db.session.commit()

        return sts.status_schema.jsonify(new_status)

class DeleteStatus(Resource):
    @Token.token_required
    def get(self,current_user,id):
        status_del = sts.Status.query.get(id)
        sts.db.session.delete(status_del)
        sts.db.session.commit()

        return sts.status_schema.jsonify(status_del)