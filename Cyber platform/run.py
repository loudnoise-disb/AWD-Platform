from flask import Flask, render_template
from app.auth.routes import bp as auth_bp
from app.user_center.routes import bp as user_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(port=80, debug=True)