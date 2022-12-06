from marshmallow import Schema, fields, post_load, validate
from app.models.user import User
from app.constant.user_type import UserType
from werkzeug.security import generate_password_hash

# class BaseSchema(Schema):

#     def handle_error(self, exc, data, **kwargs):


class UserReq:
    def __init__(self) -> None:
        self.secret = ""
        self.account = ""
        self.email = ""
        self.display_name = ""
        self.account_type = UserType.common_user


class UserSchema(Schema):
    account = fields.String(data_key='account', required=True, error_messages={'required': '账号不能为空'}, validate=validate.Length(3, 128, error="长度必须在[6-128]之间"))
    password = fields.String(data_key='password', required=True, error_messages={'required': '密码不能为空'}, validate=validate.Length(6, 128, error="长度必须在[6-128]之间"))
    email = fields.String(data_key='email', required=True, error_messages={'required':'邮箱不能为空'}, validate=validate.Length(6, 128, error="长度必须在[6-128]之间"))
    display_name = fields.String(data_key='display_name')
    account_type = fields.Int(data_key='account_type')

    @post_load
    def create_user(self, data:dict, **kwargs):
        new_user = UserReq()
        new_user.secret = generate_password_hash(data.get('password'))
        new_user.account = data.get('account')
        new_user.email = data.get('email')
        new_user.display_name = data.get('display_name')
        new_user.account_type = data.get('account_type', UserType.common_user)

        return new_user

