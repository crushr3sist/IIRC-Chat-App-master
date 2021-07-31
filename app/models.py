from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_potion import ModelResource, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'User'
    id            = db.Column(db.Integer(), primary_key = True)
    Username      = db.Column(db.String(), nullable=False)
    Email         = db.Column(db.String(), nullable=True)
    Password      = db.Column(db.String(), nullable=True)
    FirstName     = db.Column(db.String(), nullable=True)
    LastName      = db.Column(db.String(), nullable=True)
    def __init__(self,Username,Email,Password,FirstName,LastName ) -> None: 
        self.Username = Username 
        self.Email    = Email    
        self.Password = Password 
        self.FirstName= FirstName
        self.LastName = LastName 
    def __repr__(self) -> str:
        __name__ = 'User'
        return __name__

class ChatRoom(db.Model):
    __tablename__= 'ChatRoom'
    id           = db.Column(db.Integer(), primary_key = True)
    userID       = db.Column(db.Integer(), db.ForeignKey('User.id'))
    UsersName    = db.Column(db.String(), nullable=False) 
    TextBody     = db.Column(db.String(), nullable=False) 
    FileRef      = db.Column(db.String(), nullable=True) 
    def __init__(self,userID,UsersName,TextBody,FileRef) -> None: 
        self.userID   = userID    
        self.UsersName= UsersName    
        self.TextBody = TextBody  
        self.FileRef  = FileRef  
    def __repr__(self) -> str:
        __name__ = 'ChatRoom'
        return __name__

class FileReference(db.Model):
    __tablename__ = 'FileReference'    
    id            = db.Column(db.Integer(), primary_key = True)
    userID        = db.Column(db.Integer() ,db.ForeignKey('User.id'))
    FileReference = db.Column(db.String(), nullable=False) 
    FileType      = db.Column(db.String(), nullable=False) 

    def __init__(self,userID,UsersName,TextBody,FileRef) -> None: 
        self.userID   = userID    
        self.UsersName= UsersName    
        self.TextBody = TextBody  
        self.FileRef  = FileRef  

    def __repr__(self) -> str:
        __name__ = 'FileReference'
        return __name__

if __name__=="__main__":
    db.create_all()
    db.session.add(
User(
        Email    = 'hewlafkef@faewfwef.com',
        Username  = "Rahm0",
        Password  = "passwordd",
        FirstName = "Rohaan",
        LastName  = "Ahmed"
        ))
    db.session.commit()    

