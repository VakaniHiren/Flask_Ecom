from models.Model import Product,Unit,Group,User
from flask import render_template,jsonify,request
from flask_restful import Api, Resource,reqparse

class productController(Resource):
    def get(self):
        products=Product.objects
        lis=[]
        for a in products:
            lis.append({'id':str(a.id),'name' :a['pname'],'Description':a['pdesc'],'Group':str(a['gid'].gname),'Unit':str(a['unid'].utname),'User':str(a['usid'].uname)})
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pname')
        parser.add_argument('pdesc')
        parser.add_argument('pprice')
        parser.add_argument('gid')
        parser.add_argument('unid')
        parser.add_argument('usid')
        args = parser.parse_args()
        g_id = Group.objects.get(id=args['gid'])
        un_id = Unit.objects.get(id=args['unid'])
        us_id = User.objects.get(id=args['usid'])
        product = Product(pname=args['pname'],pdesc=args['pdesc'],pprice=args['pprice'],gid=g_id ,unid=un_id,usid=us_id)
        product.save()
        return "Success"

    def delete(self, pr_id):
        Product.objects(id=pr_id).delete()
        return '', 204

    def put(self, pr_id):
        parser = reqparse.RequestParser()
        parser.add_argument('pname')
        parser.add_argument('pdesc')
        parser.add_argument('pprice')
        parser.add_argument('gid')
        parser.add_argument('unid')
        parser.add_argument('usid')
        args = parser.parse_args()
        g_id = Group.objects.get(id=args['gid'])
        un_id = Unit.objects.get(id=args['unid'])
        us_id = User.objects.get(id=args['usid'])
        prd = Product.objects.get(id=pr_id)
        prd.pname = args['pname']
        prd.pdesc = args['pdesc']
        prd.pprice = args['pprice']
        prd.gid = g_id
        prd.unid = un_id
        prd.usid = us_id
        prd.save()
        return "Success"

class unitController(Resource):
    def get(self):
        units = Unit.objects
        lis = []
        for a in units:
            lis.append({'name': a['utname'], 'Description': a['utdesc']})
        return jsonify({'result': lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('utname')
        parser.add_argument('utdesc')
        args = parser.parse_args()
        unit = Unit(utname=args['utname'], utdesc=args['utdesc'])
        unit.save()
        return "Success"

    def delete(self, ut_id):
        Unit.objects(id=ut_id).delete()
        return '', 204

    def put(self, ut_id):
        parser = reqparse.RequestParser()
        parser.add_argument('utname')
        parser.add_argument('utdesc')
        args = parser.parse_args()
        unt = Unit.objects.get(id=ut_id)
        unt.utname = args['utname']
        unt.utdesc = args['utdesc']
        unt.save()
        return "Success"

class groupController(Resource):
    def get(self):
        groups = Group.objects
        lis = []
        for a in groups:
            lis.append({'name': a['gname'], 'Description': a['gdesc']})
        return jsonify({'result': lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gname')
        parser.add_argument('gdesc')
        args = parser.parse_args()
        group = Group(gname=args['gname'], gdesc=args['gdesc'])
        group.save()
        return "Success"

    def delete(self,gr_id):
        Group.objects(id=gr_id).delete()
        return '', 204

    def put(self,gr_id):
        parser = reqparse.RequestParser()
        parser.add_argument('gname')
        parser.add_argument('gdesc')
        args = parser.parse_args()
        grp = Group.objects.get(id=gr_id)
        grp.gname = args['gname']
        grp.gdesc = args['gdesc']
        grp.save()
        return "Success"

