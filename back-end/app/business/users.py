from app.models.user import User
from app.schema.response import Response
from app.plugins import db


def add_user(user:User) -> Response:
    user = User.query.filter_by(account=user.account).first()
    if user:
        return Response(status_code=400, msg=f"user {user.account} has already existed.")
    
    db.session.add(user)
    db.session.commit()
    return Response()