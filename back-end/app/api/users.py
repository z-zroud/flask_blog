from flask import request
from app.api import bp
from app.schema.user import UserReq
from app.schema.response import Response
from marshmallow import ValidationError
from app.business.users import add_user

@bp.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    schema = UserReq()

    try:
        new_user = schema.load(data)
    except ValidationError as err:
        return Response(status_code=400, msg=err.messages).json()

    return add_user(new_user).json()


