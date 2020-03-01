from api import app
from flask_restful import Api
from .user import *
from .services import *
from .status import *
from .userMapping import *
restServer = Api(app)


#User Gatetway
restServer.add_resource(GetUserById,"/api/user/<id>",  endpoint = 'getUserById')
restServer.add_resource(GetUser,"/api/user/",  endpoint = 'get_user')
restServer.add_resource(CreateUser,"/api/user", endpoint = 'add_user')
restServer.add_resource(DeleteUser,"/api/user/delete/<int:id>", endpoint = 'delete_user')
restServer.add_resource(UpdateUser,"/api/user/update/<int:id>", endpoint = 'update_user')

#Services
restServer.add_resource(GetServiceById,"/api/service/<id>",  endpoint = 'getServiceById')
restServer.add_resource(GetService,"/api/service/",  endpoint = 'getService')
restServer.add_resource(AddService,"/api/service", endpoint = 'AddService')
restServer.add_resource(DeleteService,"/api/service/delete/<int:id>", endpoint = 'deleteService')

#User Mapping
restServer.add_resource(GetMapById,"/api/map/<id>",  endpoint = 'GetMapById')
restServer.add_resource(GetMap,"/api/map/",  endpoint = 'GetMap')
restServer.add_resource(AddMap,"/api/map", endpoint = 'AddMap')
restServer.add_resource(DeleteMap,"/api/map/<int:id>", endpoint = 'DeleteMap')

#Status
restServer.add_resource(GetStatusById,"/api/status/<id>",  endpoint = 'GetStatusById')
restServer.add_resource(GetStatus,"/api/status/",  endpoint = 'GetStatus')
restServer.add_resource(AddStatus,"/api/status", endpoint = 'AddStatus')
restServer.add_resource(DeleteStatus,"/api/status/<int:id>", endpoint = 'DeleteStatus')

#Login Crediential
restServer.add_resource(UserLogin,"/api/login", endpoint = 'login')
restServer.add_resource(UserLogout,"/api/logout", endpoint = 'logout')