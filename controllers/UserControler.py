from models.Model import User
from flask import render_template,jsonify,request
from flask_restful import Api, Resource,reqparse
from flask_mail import Mail,Message
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
        parser.add_argument('admin')
        args = parser.parse_args()
        #us1 = User()
        user = User()
        user.uname=args['uname']
        user.uadd=args['uadd']
        user.uconnum=args['uconnum']
        user.uemail=args['uemail']
        user.encrypt_set_password(args['upass'])
        #user.admin=str(args['admin'])
        user.save()
        return "Success"

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('us_id')
        args = parser.parse_args()
        User.objects(id=str(args['us_id'])).delete()
        return "Delete Success"

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('us_id')
        parser.add_argument('uname')
        parser.add_argument('uadd')
        parser.add_argument('uconnum')
        parser.add_argument('uemail')
        parser.add_argument('upass')
        parser.add_argument('admin')
        args = parser.parse_args()
        usr = User.objects.get(id=str(args['us_id']))
        usr.uname = args['uname']
        usr.uadd = args['uadd']
        usr.uconnum=args['uconnum']
        usr.uemail=args['uemail']
        usr.upass=args['upass']
        print str(args['admin'])
        if(str(args['admin'])=="false"):
            usr.admin=False
        elif(str(args['admin'])=="true"):
            usr.admin=True
        else:
            usr.admin = False
        #usr.IsAdmin =
        usr.save()
        return "Update Success"

class LogInController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('upass')
        args = parser.parse_args()
        usr = User.objects(uname=args['uname']).first()
        #one=User.objects(uname=args['uname'],upass=).count()
        if usr and usr.verify_password(str(args['upass'])):
            #usrobj = User.objects.get(uname=args['uname'])
            if usr.admin :
                return {"Admin": args['uname']}
            else:
                return {'Normal User': args['uname']}
        else:
            return "Sorry"
