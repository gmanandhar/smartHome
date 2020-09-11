from flask_restful import Resource
import logging as logger
from api.models import Status as sts,service as svc
from flask  import request, jsonify
from .token import Token
import datetime
from .task import add_task
from api import q
from rq import cancel_job
from .resPI import resPi


class GetStatusById(Resource):
    @Token.token_required
    def get(self,current_user,id):
        logger.debug("Return Status by ID")
        status_instance = sts.Status.query.get(id)
        return sts.status_schema.jsonify(status_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetStatus(Resource):
    @Token.token_required
    def get(self,current_user):
        logger.debug("Return all status of table")
        all_status = sts.Status.query.all()
        result = sts.statuss_schema.dump(all_status)
        return jsonify(result)

class AddStatus(Resource):
    @Token.token_required
    def post(self,current_user):
        logger.debug("Update Status Table")
        publicId= Token.publicId(self)
        sId= request.json['sId']
        status= request.json['status']
        currentDate= datetime.datetime.utcnow()
        futureDate= request.json['futureDate']
        sts_ins =sts.Status.query.filter_by(sId=sId).first()
        svc_ins = svc.Service.query.filter_by(svcId = sId).first()
        IN = svc_ins.pinIn if not svc_ins.pinIn == "" else svc_ins.pinIn = 0
        OUT = svc_ins.pinOut if not svc_ins.pinOut == "" else svc_ins.pinOut = 0

        if  not sts_ins == None:
            if sts_ins.status == True and status == 1:
                return {"message":"Device is already ON!!"},200
            elif sts_ins.status == False and status == 0:
                return {"message":"Device is already OFF!!"},200
            elif sts_ins.status == True and status == 0:
                can_job = cancel_job(sts_ins.jobId)
                if can_job == True:
                    sts_ins.publicId = publicId
                    sts_ins.status = status
                    sts_ins.currentDate = currentDate
                    sts_ins.futureDate = currentDate
                    if not resPi(IN, OUT, status):
                        sts.db.session.commit()
                        logger.debug("Respeberry Pi has been off Sucessuflly !!")
                return {"message":"Device trun off Forcely!!"}
            else:
                sts_ins.publicId = publicId
                sts_ins.status = status
                sts_ins.currentDate = currentDate
                sts_ins.futureDate = futureDate
                if resPi(IN, OUT, status):
                    task = q.enqueue(add_task, futureDate)
                    sts_ins.jobId = task.id
                    sts.db.session.commit()
                    logger.debug("Respeberry Pi has been on Sucessuflly !!")
                return {"message":"Device trun ON Sucessfully!!"}
        else:
            if status == 0:
                return {"message":"Device is already in OFF Status!!"}
            else:
                sts_ins.publicId = publicId
                sts_ins.status = status
                sts_ins.currentDate = currentDate
                sts_ins.futureDate = futureDate

                if resPi(IN, OUT, status):
                    task = q.enqueue(add_task, futureDate)
                    sts_ins.jobId = task.id
                    sts.db.session.commit()
                    logger.debug("Respeberry Pi has been on Sucessuflly !!")
                return {"message":"Device is ON"}

        return sts.status_schema.jsonify(new_status)

class DeleteStatus(Resource):
    @Token.token_required
    def get(self,current_user,id):
        status_del = sts.Status.query.get(id)
        sts.db.session.delete(status_del)
        sts.db.session.commit()

        return sts.status_schema.jsonify(status_del)