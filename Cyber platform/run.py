from flask import Flask, render_template
from app.auth.routes import bp as auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(port=80, debug=True)