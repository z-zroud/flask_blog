from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models.user import User
from flask import g
from app.business.jwt import verify_jwt
from werkzeug.security import check_password_hash

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(account, password):
    user = User.query.filter_by(account=account).first()
    if user is None:
        return False
    g.current_user = user
    return check_password_hash(user.secret, password)

@token_auth.verify_token
def verify_token(token):
    user_id = verify_jwt(token)
    if user_id is None: 
        return False
    return g.current_user.id == user_id