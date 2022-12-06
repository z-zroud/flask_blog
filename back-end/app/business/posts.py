from app.models.post import Post
from app.schema.post import PostReq
from app.plugins import db
from flask import g



def add_post(post:PostReq) -> Post:
    new_post = Post()
    new_post.body = post.body
    new_post.title = post.title

    db.session.add(new_post)
    db.session.commit()

    return new_post



def query_posts(page, per_page):
    user_id = g.current_user.id
    pagination = Post.query.paginate(page, per_page, error_out=False)
    return pagination.pages, pagination.items



def get_post(id:int) -> Post:
    return Post.query.get_or_404(id)


def update_post(id:int, update_post:PostReq):
    post = Post.query.get_or_404(id)
    post.title = update_post.title
    post.body = update_post.body
    db.session.commit()


def delete_post(id:int):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
