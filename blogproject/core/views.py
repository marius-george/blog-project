from blogproject.models import BlogPost
from flask import render_template, request, Blueprint

# Create a Blueprint named 'core' for core views
core = Blueprint('core', __name__)

@core.route('/')
def index():
    """
    Render the index page with paginated blog posts.

    Retrieves the page number from the request arguments and fetches
    paginated blog posts ordered by date in descending order.

    Returns:
        Rendered HTML template with paginated blog posts.
    """
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/info')
def info():
    """
    Render the information page.

    Returns:
        Rendered HTML template for the information page.
    """
    return render_template('info.html')
