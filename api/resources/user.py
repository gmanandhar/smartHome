from flask_restful import Resource
import logging as logger
from api.models import user
from flask  import request, jsonify


class GetUserById(Resource):
    def get(self,id):
        logger.debug("Inside the get method")
        user_instance = user.User.query.get(id)
        return user.user_schema.jsonify(user_instance)
        # return {"message":"This is get Method >>>>" + id},200


class GetUser(Resource):
    def get(self):
        logger.debug("Inside the get method")
        all_users = user.User.query.all()
        result = user.users_schema.dump(all_users)
        return jsonify(result)

class AddUser(Resource):
    def post(self):
        logger.debug("Inside the POST method")
        fullName = request.json['fullName']
        contact = request.json['contact']
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        token = request.json['token']
        createdDate = request.json['createdDate']
        createdBy = request.json['createdBy']
        updatedDate =request.json['updatedDate']
        updatedBy = request.json['updatedBy']

        new_user = user.User(fullName, contact, email, username, password, token, createdDate, createdBy, updatedDate,
                        updatedBy)
        user.db.session.add(new_user)
        user.db.session.commit()

        return user.user_schema.jsonify(new_user)

class DeleteUser(Resource):
    def get(self,id):
        user_del = user.User.query.get(id)
        user.db.session.delete(user_del)
        user.db.session.commit()

        return user.user_schema.jsonify(user_del)