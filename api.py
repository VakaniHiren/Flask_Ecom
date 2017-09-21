from flask import Flask,session,render_template
from flask_restful import Api,Resource
from mongoengine import *
from flask_cors import CORS
from controllers import UserControler,ProductController,OrderController
from flask_mail import Mail,Message


app = Flask(__name__)
CORS(app)
api = Api(app)
app.secret_key = 'You Will Never Guess'
connect('flask_blog_db',host='mongodb://hiren:hiren@ds139954.mlab.com:39954/flask_ecome_db')

api.add_resource(UserControler.userController, '/api/users')
api.add_resource(UserControler.LogInController, '/api/users/login')
api.add_resource(ProductController.unitController, '/api/units')
#api.add_resource(ProductController.unitController, '/api/units/<ut_id>')
api.add_resource(ProductController.groupController, '/api/groups')
api.add_resource(ProductController.productController, '/api/products')
api.add_resource(OrderController.orderController, '/api/orders')
api.add_resource(OrderController.orderDetailController, '/api/orderdetails')
api.add_resource(OrderController.generateBillController, '/api/generatebills')

if __name__ == '__main__':
    app.run(debug=True)