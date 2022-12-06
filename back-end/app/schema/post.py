from marshmallow import Schema, fields, post_load


class PostReq:
    def __init__(self) -> None:
        self.title = ""
        self.body = ""

class PostSchema(Schema):
    title = fields.String(data_key='title', required=True, error_messages={'required': '标题不能为空'})
    body = fields.String(data_key='body')
    id = fields.String(data_key="id")
    create_time = fields.DateTime(data_key="createTime")
    last_update_time = fields.DateTime(data_key="lastUpdateTime")

    @post_load
    def create_post(self, data:dict, **kwargs):
        post_req = PostReq()
        post_req.title = data.get("title")
        post_req.body = data.get("body")


        return post_req
