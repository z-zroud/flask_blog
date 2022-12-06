from app.models.user import User
from app.schema.user import UserReq
from app.exceptions import HasExistedException
from app.plugins import db


def add_user(user:UserReq) -> User|HasExistedException:
    existed_user = User.query.filter_by(account=user.account).first()
    if existed_user:
        raise HasExistedException(reason=f"user {existed_user.account} has already existed.")
    
    new_user = User()
    new_user.account = user.account
    new_user.account_type = user.account_type
    new_user.display_name = user.display_name
    new_user.email = user.email
    new_user.secret = user.secret

    db.session.add(new_user)
    db.session.commit()
    return new_user