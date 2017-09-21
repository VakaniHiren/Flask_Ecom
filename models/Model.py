from mongoengine import *
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import JSONWebSignatureSerializer as Serializer

class User(Document):
    uname =  StringField(unique=True,required=True)
    uadd  =  StringField()
    uconnum = StringField()
    uemail = StringField()
    upass =  StringField(required=True)
    admin = BooleanField(default=False)

    def is_admin(self):
        return self.admin

    def encrypt_set_password(self, password):
        self.upass = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.upass)

    def generate_auth_token(self):
        s = Serializer(SECRET_KEY)
        return s.dumps({"id": str(self.id), "password": self.upass}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
            user = User.objects(id=data["id"]).first()
            return user
        except:
            return None

class Group(Document):
    gname = StringField(unique=True,required=True)
    gdesc = StringField()

class Unit(Document):
    utname = StringField(unique=True,required=True)
    utdesc = StringField()

class Product(Document):
    pname = StringField(unique=True,required=True)
    pdesc  = StringField()
    pprice = DecimalField()
    gid   =  ReferenceField(Group)
    unid  =  ReferenceField(Unit)
    usid  =  ReferenceField(User)


class Order(Document):
    odate = DateTimeField(default=datetime.now)
    onum  = StringField()
    usid  = ReferenceField(User)

class Order_Det(Document):
    oid  =  ReferenceField(Order)
    pid  = ReferenceField(Product)
    qty  = IntField()

class GenerateBill(Document):
    oid = ReferenceField(Order)
    TotalAmt = DecimalField()