from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

users = {}
user_id = 0

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('job_title')
parser.add_argument('communicate_information', type=dict)

class User(Resource):
    
    def get(self, user_id):
        if user_id in users.keys():
            return users[user_id]
        else:
            return {
                'message': 'User not found.',
                'success': False
            }
    
    def put(self, user_id):
        global users
        if user_id in users.keys():
            args = parser.parse_args()
            user_info = {
                'name': args['name'],
                'job_title': args['job_title'],
                'communicate_information': args['communicate_information']
            }
            users[user_id] = user_info
            return {
                'message': 'Successfully update user.',
                'updated_user': user_info,
                'success': True
            }
        else:
            return {
                'message': 'Can not update user. User not found.',
                'success': False
            }
    
    def delete(self, user_id):
        global users
        if user_id in users.keys():
            users.pop(user_id)
            return {
                'message': 'Successfully delete user.',
                'success': True
            }
        else:
            return {
                'message': 'Can not delete user. User not found.',
                'success': False
            }

class UserList(Resource):
    
    def get(self):
        return {
            'message': 'Successfully get user list.',
            'user_list': users,
            'success': True
        }

    def post(self):
        args = parser.parse_args()
        user_info = {
            'name': args['name'],
            'job_title': args['job_title'],
            'communicate_information': args['communicate_information']
        }
        
        global users
        global user_id
        users[user_id] = user_info
        user_id += 1

        return {
            'message': 'Successfully create user.',
            'new_user': user_info,
            'success': True
        }
    
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserList, '/user_list')
