import os
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'customer.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)
Migrate(app,db)

###### Customer Class########
class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    add   = db.Column(db.String(200))
    email = db.Column(db.String(200))
    dob   = db.Column(db.String(200))
    room_no = db.Column(db.Integer)
    room_type =db.Column(db.String(200))
    check_in_date =db.Column(db.String(200))
    check_out_date = db.Column(db.String(200))
    rn = db.relationship('Room',backref='customer', uselist=False)

    def __init__(self,fname,lname,add,email,dob,room_no,room_type,check_in_date,check_out_date):
        self.fname = fname
        self.lname = lname
        self.add   = add
        self.email = email
        self.dob = dob
        self.room_no = room_no
        self.room_type = room_type
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date



########Home Page########
@app.route('/')
def home():
    return render_template('home.html')

#Method to add cutomer
@app.route('/add',methods =['GET','POST'])
def addCustomer():
    if request.method =='POST':
        cust = Customer(request.form['fname'],request.form['lname'],request.form['add'],request.form['email'],
                request.form['dob'],request.form['room_no'],request.form['room_type'],request.form['check_in_date'],
                request.form['check_out_date'])
        db.session.add(cust)
        db.session.commit()
    return render_template('add.html')

#Method to display customer data
@app.route('/display')
def display():
    return render_template('display.html',Customer= Customer.query.all())


#Method to Delete customer Data
@app.route('/delete',methods =['GET','POST'])
def delete():
    if request.method =='POST':
        # print(request.form['id']+" abc")
        emp = Customer.query.get(request.form['id'])
        db.session.delete(emp)
        db.session.commit()
    return render_template('delete.html')


########Room############
class Room(db.Model):
    __tablename__="room"
    room_no = db.Column(db.Integer,primary_key=True)
    room_type = db.Column(db.String(200))
    cust_id = db.Column(db.Integer,db.ForeignKey('customer.id'))

    def __init__(self,room_no,room_type,cust_id):
          self.room_no = room_no
          self.room_type = room_type

          self.cust_id = cust_id

# Function to add room
@app.route('/addroom',methods =['GET','POST'])
def addroom():
    if request.method =='POST':
        room = Room(request.form['roomno'],request.form['roomtype'],request.form['cust_id'])
        db.session.add(room)
        db.session.commit()
    return render_template('addroom.html')

# Function to display room data
@app.route('/displayroom')
def displayroom():
    return render_template('displayroom.html',Room=Room.query.all())




if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
