from flask_restful import Resource
import logging as logger
from api.models import user
from flask import request, jsonify, make_response
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import uuid, jwt
from api import app
from .token import Token, LogoutUser

#Method to login into API
class UserLogin(Resource):

    def get(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {'WWW-Authentication':'Basic-realm="Login Required"'})
        user_ins = user.User.query.filter_by(username=auth.username).first()
        if not user_ins:
            return make_response('Could not verify', 401, {'WWW-Authentication':'Basic-realm="Login Required"'})

        if check_password_hash(user_ins.password,auth.password):
            token = jwt.encode({'publicId':user_ins.publicId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
            user_ins.token = token.decode('UTF-8')
            user.db.session.commit()
            return jsonify({'token':token.decode('UTF-8')})
        return make_response('Could not verify', 401, {'WWW-Authentication': 'Basic-realm="Login Required"'})

#Method to get user by ID
class GetUserById(Resource):
    @Token.token_required
    def get(self,id):
        logger.debug("Inside the get method")
        user_instance = user.User.query.get(id)
        return user.user_schema.jsonify(user_instance)
#Method to get All User
class GetUser(Resource):
    @Token.token_required
    def get(self, current_user):
        logger.debug("Inside the get method")
        if True:
            all_users = user.User.query.all()
            result = user.users_schema.dump(all_users)
            return jsonify(result)

        else:
            return {"message": "User is Invalid"}, 403

#Method to create user
class CreateUser(Resource):
    def post(self):
        public_id =uuid.uuid4()
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        hashlib.md5(request.json['password'].encode()).hexdigest()
        new_user = user.User(str(public_id),data['fullName'],data['contact'],data['email'],data['username'],hashed_password,"firstTimeUser",datetime.datetime.utcnow(),data['username'],datetime.datetime.utcnow(),data['username'])
        user.db.session.add(new_user)
        user.db.session.commit()
        return user.user_schema.jsonify(new_user)
#Method to Delete User
class DeleteUser(Resource):
    @Token.token_required
    def get(self,current_user,id):
        user_del = user.User.query.get(id)
        user.db.session.delete(user_del)
        user.db.session.commit()
        return user.user_schema.jsonify(user_del)

#Method to update User
class UpdateUser(Resource):
    @Token.token_required
    def put(self,current_user,id):
        usr = user.User.query.get(id)
        fullName = request.json['fullName']
        contact = request.json['contact']
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        token = request.json['token']
        createdDate = request.json['createdDate']
        createdBy = request.json['createdBy']
        updatedDate = request.json['updatedDate']
        updatedBy = request.json['updatedBy']
        usr.fullName =fullName
        usr.contact =contact
        usr.email = email
        usr.username = username
        usr.password =password
        usr.token =token
        usr.createdDate=createdDate
        usr.createdBy = createdBy
        usr.updatedDate=updatedDate
        usr.updatedBy =updatedBy
        user.db.session.commit()
        return user.user_schema.jsonify(usr)

#Method to Logout from session
class UserLogout(Resource):
    def get(self):
        LogoutUser.logout(self,Token.publicId(self))
        print(Token.publicId(self))
