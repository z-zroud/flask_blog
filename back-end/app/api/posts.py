from flask import request
from app.api import bp
from app.business.auth import token_auth
from app.schema.post import PostSchema
from app.schema.response import Response
from app.business.posts import query_posts
from app.business import posts
from marshmallow import ValidationError

@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    data = request.get_json()
    schema = PostSchema()

    try:
        post_req = schema.load(data)
        new_post = posts.add_post(post_req)
    except ValidationError as err:
        return Response(status_code=400, msg=err.messages).json()

    return Response({"id":new_post.id}).json()


@bp.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get("page", 0)
    per_page = request.args.get("perPage", 10)
    total, posts = query_posts(page, per_page)
    results = PostSchema().dump(posts, many=True)
    return Response({"total":total, "posts":results}).json()


@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = posts.get_post(id)
    result = PostSchema().dump(post)
    return Response(result).json()


@bp.route('/posts/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_post(id):
    data = request.get_json()
    schema = PostSchema()

    try:
        post_req = schema.load(data)
        posts.update_post(post_req)
    except ValidationError as err:
        return Response(status_code=400, msg=err.messages).json()

    return Response().json()


@bp.route('/posts/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_post(id):
    posts.delete_post(id)
    return Response().json()