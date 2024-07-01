from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Tutors(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    username=db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    phone = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)
    batch = db.Column(db.String(100),nullable=False)
    experience =db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"Tutors('{self.username}','{self.email}','{self.phone}','{self.password}','{self.batch}','{self.experience}')"

class Tuition(db.Model):
    id= db.column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False)
    