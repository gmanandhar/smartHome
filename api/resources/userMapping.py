from flask_restful import Resource
import logging as logger
from api.models import userMapping as usrMap, user
from flask  import request, jsonify
from  .token import Token
import datetime

class GetMapById(Resource):
    @Token.token_required
    def get(self,current_user,id):
        logger.debug("Inside the get method")
        usrMap_instance = usrMap.UserMapping.query.get(id)
        return usrMap.userMap_schema.jsonify(usrMap_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetMap(Resource):
    @Token.token_required
    def get(self,current_user):
        logger.debug("Inside the get method")
        all_usrMap = usrMap.UserMapping.query.all()
        result = usrMap.userMaps_schema.dump(all_usrMap)
        return jsonify(result)

class AddMap(Resource):
    @Token.token_required
    def post(self,current_user):

        data = request.get_json()
        publicId = Token.publicId(self)
        sId = data['svcId']
        read = data['read']
        write = data['write']
        delete = data['delete']
        user_ins = user.User.query.filter_by(publicId=publicId).first()
        createdDate = datetime.datetime.utcnow()
        createdBy = user_ins.username
        updatedDate = datetime.datetime.utcnow()
        updatedBy = user_ins.username

        new_usrMap = usrMap.UserMapping(publicId, sId, read, write, delete, createdDate, createdBy, updatedDate,updatedBy)
        usrMap.db.session.add(new_usrMap)
        usrMap.db.session.commit()

        return usrMap.userMap_schema.jsonify(new_usrMap)

class DeleteMap(Resource):
    @Token.token_required
    def get(self,current_user,id):
        map_del = usrMap.UserMapping.query.get(id)
        usrMap.db.session.delete(map_del)
        usrMap.db.session.commit()

        return usrMap.userMaps_schema.jsonify(map_del)