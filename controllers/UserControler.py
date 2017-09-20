from models.Model import User
from flask import render_template,jsonify,request
from flask_restful import Api, Resource,reqparse

class userController(Resource):
    def get(self):
        users=User.objects
        lis=[]
        for a in users:
            lis.append({'uname' :a['uname'],'uadd':a['uadd']})
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('uadd')
        parser.add_argument('uconnum')
        parser.add_argument('uemail')
        parser.add_argument('upass')
        args = parser.parse_args()
        user = User(uname=args['uname'],uadd=args['uadd'],uconnum=args['uconnum'], uemail=args['uemail'],upass=args['upass'])
        user.save()
        return "Success"

    def delete(self, us_id):
        User.objects(id=us_id).delete()
        return '', 204

    def put(self, us_id):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('uadd')
        parser.add_argument('uconnum')
        parser.add_argument('uemail')
        parser.add_argument('upass')
        args = parser.parse_args()
        usr = User.objects.get(id=us_id)
        usr.uname = args['uname']
        usr.uadd = args['uadd']
        usr.uconnum=args['uconnum']
        usr.uemail=args['uemail']
        usr.upass=args['upass']
        usr.save()
        return "Success"

class LogInController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('upass')
        args = parser.parse_args()
        one=User.objects(uname=args['uname'],upass=args['upass']).count()
        if one :
            return {'result': args['uname']}
        else:
            return "Sorry"