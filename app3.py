from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)


#data base connectivy configuration code.....
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flaskproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Deepanshu")
db = SQLAlchemy(app)

#database model:

class employee(db.Model):
      eid=db.Column(db.Integer,primary_key=True)
      ename=db.Column(db.String(80),nullable=True)
      eemail=db.Column(db.String(80),nullable=True)
      e_phone_num=db.Column(db.String(12),nullable=True)
      e_meg=db.Column(db.String(80),nullable=True)
with app.app_context():
     db.create_all()



if __name__=='__main__':
    app.run(debug=True)