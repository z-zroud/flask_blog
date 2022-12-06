from flask import request
from app.api import bp
from app.schema.user import UserSchema
from app.schema.response import Response
from marshmallow import ValidationError
from app.exceptions import HasExistedException
from app.business.users import add_user

@bp.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    schema = UserSchema()

    try:
        user_req = schema.load(data)
        new_user = add_user(user_req)
    except ValidationError as err:
        return Response(status_code=400, msg=err.messages).json()
    except HasExistedException as err:
        return Response(status_code=400, msg=err.reason).json()


    return Response({"id":new_user.id}).json()


