from app.api import bp
from app.business.auth import basic_auth
from flask import g
from app.business.jwt import generate_jwt
from app.schema.response import Response

@bp.route('/login', methods=['POST'])
@basic_auth.login_required
def login():
    token = generate_jwt(g.current_user.id, g.current_user.account)
    return Response({'token':token}).json()