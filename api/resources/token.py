from flask_restful import Resource
from api.models import user
from flask import request, jsonify
import jwt
from api import app
from functools import wraps

class Token(Resource):
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token= request.headers['x-access-token']


            if not token:
                return jsonify({'message':'Token is missing!'}), 401

            try:
                data = jwt.decode(token,app.config['SECRET_KEY'])
                current_user = user.User.query.filter_by(publicId=data['publicId']).first()
                if not current_user.token == token:
                    return jsonify({'message': 'Token does not match!'}), 401
            except:
                return jsonify({'message': 'Token is invalid!'}),401

            return f(current_user,*args,**kwargs)
        return decorated
    def publicId(self):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            id = data['publicId']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return id

class LogoutUser(Resource):
    def logout(self,publicId):
        usr = user.User.query.filter_by(publicId=publicId).first()
        usr.token = None
        return True


