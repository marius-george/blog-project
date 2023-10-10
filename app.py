import os
from blogproject import create_app

try:
    import env
except:
    pass
app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("DEBUG")
    )     