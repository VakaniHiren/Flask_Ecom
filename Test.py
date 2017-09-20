from flask import Flask,session
from mongoengine import *
from models.Model import *

app = Flask(__name__)
app.secret_key = 'You Will Never Guess'
connect('flask_blog_db',host='mongodb://hiren:hiren@ds139954.mlab.com:39954/flask_ecome_db')

total=0
od = Order_Det.objects(oid="59c247b5dc31321480d7569c")
for k in od:
    print 'id   ' + str(k.id)
    p = k.pid
    total += p.pprice
print total
print "============"
ord = Order.objects
lis = []
total=0
for a in ord:
  #od=Order_Det.objects(oid=a.id).count()
  od = Order_Det.objects(oid=a.id)
  for k in od:
      print 'id   '+str(k.id)
      p=k.pid
      total+=p.pprice
  t1=a.id
  t2=a.odate
  lis.append({'oid': t1, 'date': t2})
print total
print lis

