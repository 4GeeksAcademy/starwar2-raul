from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        # do not serialize the password, its a security breach
        return { "id": self.id,
                 "email": self.email,
        "is active": self.is_active}
            
            
    class Post(db.Model):
        id = db.Colum(db.Integer, primary_key=True)
        title = db.Colum8(db.String(), nullable=True)
        descriotion = db.Colum(db.String(), nullable=True)
        body =  db.Colum(db.String(), nullable=True)
        date =  db.Colum(db.date())
        image_url = db.Colum(db.String())

       class Medias(db.Model):
        id = db.Colum(db.Integer, primary_key=True)
        type = db.Colum8(db.enum(), nullable=True)
        image_url = db.Colum(db.String())  
