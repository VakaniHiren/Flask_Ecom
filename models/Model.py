from mongoengine import *
from datetime import datetime

class User(Document):
    uname =  StringField(unique=True,required=True)
    uadd  =  StringField()
    uconnum = StringField()
    uemail = StringField()
    upass =  StringField(required=True)

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