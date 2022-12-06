from app.plugins import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text)
    create_time = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    last_update_time = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def __repr__(self):
        return '<Post {}>'.format(self.title)
