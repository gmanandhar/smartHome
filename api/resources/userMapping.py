from flask_restful import Resource
import logging as logger
from api.models import userMapping as usrMap
from flask  import request, jsonify


class GetMapById(Resource):
    def get(self,id):
        logger.debug("Inside the get method")
        usrMap_instance = usrMap.UserMapping.query.get(id)
        return usrMap.userMap_schema.jsonify(usrMap_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetMap(Resource):
    def get(self):
        logger.debug("Inside the get method")
        all_usrMap = usrMap.UserMapping.query.all()
        result = usrMap.userMaps_schema.dump(all_usrMap)
        return jsonify(result)

class AddMap(Resource):
    def post(self):
        logger.debug("Inside the POST method")
        uId= request.json['uId']
        sId= request.json['sId']
        read= request.json['read']
        write= request.json['write']
        delete= request.json['delete']
        createdDate = request.json['createdDate']
        createdBy = request.json['createdBy']
        updatedDate =request.json['updatedDate']
        updatedBy = request.json['updatedBy']

        new_usrMap = usrMap.UserMapping(uId, sId, read, write, delete, createdDate, createdBy, updatedDate,updatedBy)
        usrMap.db.session.add(new_usrMap)
        usrMap.db.session.commit()

        return usrMap.userMap_schema.jsonify(new_usrMap)

class DeleteMap(Resource):
    def get(self,id):
        map_del = usrMap.UserMapping.query.get(id)
        usrMap.db.session.delete(map_del)
        usrMap.db.session.commit()

        return usrMap.userMaps_schema.jsonify(map_del)