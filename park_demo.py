#! /usr/bin/env python3
# -*- conding:utf-8 -*-
from flask import Flask,render_template,redirect,request,url_for,json
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/park"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 创建Manager对象并指定要管理的app
manager = Manager(app)
# 创建Migrate对象,并指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加数据库的迁移指令
# 为manager增加一个子命令-db(自定义),具体操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100), unique=True, nullable=False)
    pwd1 = db.Column(db.String(100), nullable=False)
    pwd2 = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    ucard = db.Column(db.String(100), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    is_Active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return "<Users:%r>" % self.uname


class Parks(db.Model):
    __tablename__ = 'parks'
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    pnum = db.Column(db.Integer, nullable=False)
    price = db.Column(db.DECIMAL(2, 1), default=3.5)
    coordi_x = db.Column(db.DECIMAL(4, 2), nullable=False)
    coordi_y = db.Column(db.DECIMAL(4, 2), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)
    is_Active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return "<Parks:%r>" % self.pname


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100), unique=True, nullable=False)
    pname = db.Column(db.String(100), unique=True, nullable=False)
    addtime = db.Column(db.DateTime, default=datetime.now)
    startT = db.Column(db.DateTime, nullable=False)
    endT = db.Column(db.DateTime, nullable=False)
    totalT = db.Column(db.String(100), nullable=False)
    spend = db.Column(db.DECIMAL(5, 2), nullable=False)
    is_Delete = db.Column(db.Boolean, default=False)

    def __str__(self):
        return "<Record %r>" % self.id


class Tourist(db.Model):
    __tablename__ = 'tourist'
    id = db.Column(db.Integer, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return "<Tourist %r>" % self.id


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == "GET":

        return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """登录"""
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == 'POST':
        phone = request.form.get('phone')
        pwd1 = request.form.get('upwd')
    # 判断手机号和密码是否填写
        if not all([phone,pwd1]):
            msg = "*请填写完整的信息*"
            return render_template('login.html')
        # 核对用户名和密码是否一致
        user = Users.query.filter_by(phone=phone,pwd1=pwd1).first()
        # 如果用户名和密码一致
        if user:
            return redirect('/home')
        else:
            msg = "*手机号和密码不一致*"
            return render_template('login.html',msg=msg)

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/checkuname')
def checkuname():
    uname = request.args['uname']
    user = Users.query.filter_by(uname=uname).first()
    if user:
        dic = {
            "status":1,
            "text":"uname already exist"
        }
        return json.dumps(dic)
    else:
        dic = {
            "status":0,
            "text":"uname does not exist"
        }
        return json.dumps(dic)

@app.route('/reguser',methods=['POST'])
def reguser():
    uname = request.form['uname']
    pwd1 = request.form['pwd1']
    pwd2 = request.form['pwd2']
    email = request.form['email']
    phone = request.form['phone']
    ucard = request.form['ucard']

    user = Users()
    user.uname = uname
    user.pwd1 = pwd1
    user.pwd2 = pwd2
    user.email = email
    user.phone = phone
    user.ucard = ucard
    try:
        db.session.add(user)
        db.session.commit()
        dic = {
            "status":1,
            "text":"register success"
        }
        return json.dumps(dic)
    except Exception as ex:
        print(ex)
        dic = {
            "status": 0,
            "text": "register failed"
        }
        return json.dumps(dic)

@app.route("/test",methods=['GET','POST'])
def test():
    if request.method == 'POST':
        return render_template('login.html')




















#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     """注册"""
#     if request.method == "GET":
#         return render_template('register.html')
#     else:
#         uname = request.form.get('uname')
#         pwd1 = request.form.get('upwd1')
#         pwd2 = request.form.get('upwd2')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         ucard = request.form.get('ucard')
#
#         # 定义一个变量来控制过滤用户填写的信息
#         flag = True
#         # 判断用户是否信息都填写了.(all()函数可以判断用户填写的字段是否有空)
#         if not all([uname,pwd1,pwd2,email,phone,ucard]):
#             msg,flag = "*请填写完整信息*",False
#         elif len(uname) > 16:
#             msg,flag = "*用户名太长*",False
#         elif pwd1 != pwd2:
#             msg,flag = "*两次输入密码不一致*",False
#         if not flag:
#             return render_template('register.html',msg=msg)
#         # 核对输入的用户是否已经被注册了
#         u = Users.query.filter(Users.uname == uname).first()
#         # 判断用户名是否已经存在
#         if u:
#             msg = "用户名已经存在"
#             return render_template('register.html',msg=msg)
#         user = Users(uname=uname,pwd1=pwd1,pwd2=pwd2,email=email,phone=phone,ucard=ucard)
#         db.session.add(user)
#         return redirect('/login')


if __name__ == '__main__':
    manager.run()
