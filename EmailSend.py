from flask_mail import Mail,Message
from flask import Flask,request,url_for
from itsdangerous import URLSafeTimedSerializer,SignatureExpired

app=Flask(__name__)
app.config.from_pyfile('config.cfg')

mail=Mail(app)

s= URLSafeTimedSerializer('Thisissecret')
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return '<form action="/" method="post"><input name="email"><input type="submit"></form>'
    email=request.form['email']
    token = s.dumps(email,salt='email-confirm')

    msg = Message('Confirm Email',sender='anil.tadvi501@gmail.com',recipients=[email])
    link = url_for('confirm_email',token=token,external=True)
    msg.body = 'Your link is {}'.format(link)
    mail.send(msg)
    return 'The email you enter is {}. The toke is {}</h1>'.format(email,token)

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email=s.loads(token,salt='email-confirm',max_age=20)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    return '<h1>The token Works</h2>'

if __name__ == '__main__':
    app.run(debug=True)