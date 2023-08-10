# blog_posts/views.py
from flask import render_template, url_for, flash, request, redirect, abort, Blueprint
from flask_login import current_user, login_required
from blogproject import db
from blogproject.models import BlogPost
from blogproject.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)


@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Article created')
        return redirect(url_for('core.index'))
    return render_template('article_post.html', form=form)


@blog_posts.route('/<int:blog_post_id>')
def view_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('article.html', title=blog_post.title,
                           date=blog_post.date, post=blog_post)


@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm(obj=blog_post)
    if form.validate_on_submit():
        form.populate_obj(blog_post)
        db.session.commit()
        flash('Article updated')
        return redirect(url_for('blog_posts.view_post', blog_post_id=blog_post.id))
    return render_template('article_post.html', title='Updating', form=form)


@blog_posts.route('/<int:blog_post_id>/delete', methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Article deleted')
    return redirect(url_for('core.index'))
