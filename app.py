from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import os
from datetime import datetime
import random


with open('config.json', 'r') as c:
    params = json.load(c)["params"]


local_server = params['local_server']

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['post_image_loc']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_id'],
    MAIL_PASSWORD=  params['gmail_id_pass']
)

mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)

class Contact(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mono = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    title = db.Column(db.String(80),primary_key=True,nullable=False)
    slug = db.Column(db.String(21), nullable=True)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    image = db.Column(db.String(100), nullable=False)
    no = db.Column(db.Integer, nullable=True)

class Accounts(db.Model):
    user_name = db.Column(db.String(80),primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    mail = db.Column(db.String(12), nullable=False)
    mo_no = db.Column(db.String(100), nullable=False)
    sdate = db.Column(db.Integer, nullable=True)

@app.route('/')
def home():
    if 'username' in session:
        posts =  Posts.query.filter_by().all()[0:params["post_section_feature_post_number"]]
        btntext = "sign out"
        btnlink = "/signout"
        btntexts = ""
        btnlinks = ""
        return render_template('index.html', params=params, posts=posts, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)
    else:
        posts =  Posts.query.filter_by().all()[0:params["post_section_feature_post_number"]]
        btntext = "sign in"
        btnlink = "/signin"
        btntexts = "sign up"
        btnlinks = "/signuppage"
        return render_template('index.html', params=params, posts=posts, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):
    if 'username' in session:
        post = Posts.query.filter_by(slug=post_slug).first()
        btntext = "sign out"
        btnlink = "/signout"
        btntexts = ""
        btnlinks = ""
        return render_template('post.html', params=params, post=post, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)
    else:
        btntext = "sign in"
        btnlink = "/signin"
        btntexts = "sign up"
        btnlinks = "/signuppage"
        errorlink = "/projects"
        errormsg = "you need to sign up to access this project...!"
        errorbtntext = "click here to sign up"
        return render_template("error.html", params=params, errorlink=errorlink, errormsg=errormsg, errorbtntext=errorbtntext, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)



@app.route('/projects')
def project():
    if 'username' in session:
        posts_for_project_page = Posts.query.filter_by().all()
        btntext = "sign out"
        btnlink = "/signout"
        btntexts = ""
        btnlinks = ""
        return render_template('projects.html', params=params, posts_for_project_page=posts_for_project_page, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)
    else:
        posts_for_project_page =  Posts.query.filter_by().all()[0:params["post_section_feature_post_number"]]
        btntext = "sign in"
        btnlink = "/signin"
        btntexts = "sign up"
        btnlinks = "/signuppage"
        return render_template('projects.html', params=params, posts_for_project_page=posts_for_project_page, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    rerror=''
    if('user' in session and session['user'] == params['admin_id']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if(username == params['admin_id'] and password == params['admin_password']):
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        else:
            rerror = 'please enter right username'

    return render_template('login.html', params=params, rerror=rerror)


@app.route('/edit/<string:no>', methods = ['GET', 'POST'])
def edit_post(no):
    if('user' in session and session['user'] == params['admin_id']):
        if(request.method=='POST'):
            title = request.form.get('title')
            image_url = request.form.get('image')
            content = request.form.get('content')
            date = datetime.now()

            slug = title.replace(" ", "-")

            if no=="0":
                post= Posts(title=title, image=image_url, content=content, slug=slug, date=date)
                db.session.add(post)
                db.session.commit()
            
            else:
                post = Posts.query.filter_by(no=no).first()
                post.title = title
                post.slug = slug
                post.content = content
                post.image = image_url
                post.date = date 
                db.session.commit()
                return redirect('/edit/' + no)
        post = Posts.query.filter_by(no=no).first()
        return render_template('edit.html', params=params, post=post, no=no)



@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if('user' in session and session['user'] == params['admin_id']):
        if(request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'] + f.filename))
            return "<h1 style='font-size:30px; text-align: center; line-height:50%;  margin-top:23%; text-transform: uppercase'>image uploaded successfully</h1>"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/admin')


@app.route('/delete/<string:no>', methods = ['GET', 'POST'])
def delete(no):
    if('user' in session and session['user'] == params['admin_id']):
        post = Posts.query.filter_by(no=no).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/admin')


@app.route("/contact", methods = ['GET', 'POST'])
def contacts():
    if 'username' in session:
        btntext = "sign out"
        btnlink = "/signout"
        btntexts = ""
        btnlinks = ""
        if(request.method=='POST'):
            '''Add entry to the database'''
            name = request.form.get('name')
            email = request.form.get('email')
            number = request.form.get('number')
            message = request.form.get('message')
            entry = Contact(name=name, mono= number, message= message, date= datetime.now(), email = email )
            db.session.add(entry)
            db.session.commit()
            mail.send_message('New Message Send From Super Web',
                            sender =  email,
                            recipients = [params['gmail_id']],
                            body = "Name : "+name+ "\n"+"Number : "+number+"\n"+"\n"+"\t"+message
                            )
        return render_template('contact.html', params=params, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)
    else:
        btntexts = "sign up"
        btnlinks = "/signuppage"
        btntext = "sign in"
        btnlink = "/signin"
        if(request.method=='POST'):
            '''Add entry to the database'''
            name = request.form.get('name')
            email = request.form.get('email')
            number = request.form.get('number')
            message = request.form.get('message')
            entry = Contact(name=name, mono= number, message= message, date= datetime.now(), email = email )
            db.session.add(entry)
            db.session.commit()
            mail.send_message('New Message Send From Super Web',
                            sender =  email,
                            recipients = [params['gmail_id']],
                            body = "Name : "+name+ "\n"+"Number : "+number+"\n"+"\n"+"\t"+message
                            )
            return render_template('contact.html', params=params, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)
        return render_template('contact.html', params=params, btntext=btntext, btnlink=btnlink, btntexts=btntexts, btnlinks=btnlinks)


@app.route("/signuppage", methods = ['GET', 'POST'])
def signuppage():
    return render_template("signup.html", params=params)


@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if(request.method=='POST'):
            user_name = request.form.get('username')
            password = request.form.get('password')
            semail = request.form.get('email')
            mono = request.form.get('mono')
            sdate = datetime.now()
            entry = Accounts(user_name=user_name, password= password, mail = semail, mo_no= mono, sdate = sdate )
            db.session.add(entry)
            db.session.commit()
    return redirect("/signin")



@app.route("/signin", methods = ['GET', 'POST'])
def signin():

    if(request.method=='POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        session['username'] = username
        

        if 'username' in session:
           return redirect('/')

        account = Accounts.query.filter_by(user_name=username, password=password).first()

        if account:
            return redirect('/')

        else:
            errormsg = "please enter the correct password"
            return render_template("signin.html", params=params, errormsg=errormsg)

    return render_template("signin.html", params=params)


@app.route('/signout')
def signout():
    session.pop('username')
    return redirect('/')


@app.route('/fatchuser', methods = ['GET', 'POST'])
def fathuser():
    rerror=''
    if('user' in session and session['user'] == params['admin_id']):
        posts = Accounts.query.all()
        return render_template('fatchuser.html', params=params, posts=posts)


@app.route('/dele/<string:mo_no>', methods = ['GET', 'POST'])
def dele(mo_no):
    if('user' in session and session['user'] == params['admin_id']):
        account = Accounts.query.filter_by(mo_no=mo_no).first()
        db.session.delete(account)
        db.session.commit()
    return redirect('/fatchuser')


app.run(debug=True)