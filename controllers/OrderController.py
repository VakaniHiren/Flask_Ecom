from models.Model import Order,Order_Det,User,Product,GenerateBill
from flask import render_template,jsonify,request
from flask_restful import Api, Resource,reqparse

#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))

class orderController(Resource):
    def get(self):
        orders=Order.objects
        lis=[]
        for a in orders:
            lis.append({'Date' :a['odate'],'Number':a['onum'],'usid':a['usid'].uname})
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('odate')
        parser.add_argument('onum')
        parser.add_argument('usid')
        args = parser.parse_args()
        us_id = User.objects.get(id=args['usid'])
        order = Order(odate=args['odate'],onum=args['onum'],usid=us_id)
        order.save()
        return "Success"


    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('or_id')
        args = parser.parse_args()
        Order.objects(id=str(args['or_id'])).delete()
        return "Delete Success"

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('or_id')
        parser.add_argument('odate')
        parser.add_argument('onum')
        parser.add_argument('usid')
        args = parser.parse_args()
        us_id = User.objects.get(id=args['usid'])
        ord = Order.objects.get(id=args['or_id'])
        ord.odate = args['odate']
        ord.onum= args['onum']
        ord.usid = us_id
        ord.save()
        return "Update Success"

class orderDetailController(Resource):
    def get(self):
        orderdets = Order_Det.objects
        lis=[]
        for a in orderdets:
            lis.append({'order id' :str(a['oid'].id),'Product_id':str(a['pid'].id)})
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('oid')
        parser.add_argument('pid')
        parser.add_argument('qty')
        args = parser.parse_args()
        or_id = Order.objects.get(id=args['oid'])
        pr_id = Product.objects.get(id=args['pid'])
        orderdet = Order_Det(oid=or_id,pid=pr_id,qty=args['qty'])
        orderdet.save()
        return "Success"


    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ord_id')
        args = parser.parse_args()
        Order_Det.objects(id=str(args['ord_id'])).delete()
        return "Delete Success"

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ord_id')
        parser.add_argument('oid')
        parser.add_argument('pid')
        parser.add_argument('qty')
        args = parser.parse_args()
        ord = Order_Det.objects.get(id=str(args['ord_id']))
        ord.pid = Product.objects.get(id=str(args['pid']))
        ord.oid = Order.objects.get(id=str(args['oid']))
        ord.qty=args['qty']
        ord.save()
        return "Update Success"

class generateBillController(Resource):
    def get(self):
        orderdets = Order_Det.objects
        lis=[]
        for a in orderdets:
            lis.append({'order id' :str(a['oid'].id),'Total Amount': "Amount" })
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('oid')
        args = parser.parse_args()
        or_id = Order.objects.get(id=args['oid'])
        total = 0
        od = Order_Det.objects(oid=or_id)
        for k in od:
            print 'id   ' + str(k.id)
            p = k.pid
            total += p.pprice * k.qty
        gbill = GenerateBill(oid=or_id,TotalAmt=total)
        gbill.save()
        return "Success"


    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bill_id')
        args = parser.parse_args()
        GenerateBill.objects(id=str(args['bill_id'])).delete()
        return "Delete Success"

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('bill_id')
        parser.add_argument('oid')
        args = parser.parse_args()
        GBObj = GenerateBill.objects.get(id=str(args['bill_id']))
        GBObj.oid = Order.objects.get(id=str(args['oid']))
        #or_id = Order.objects.get(id=str(args['oid']))
        total = 0
        od = Order_Det.objects(oid=GBObj.oid)
        for k in od:
            #print 'id   ' + str(k.id)
            p = k.pid
            total += p.pprice * k.qty
        ord.save()
        return "Update Success"