from flask import Flask, render_template
from app.auth.routes import bp as auth_bp
from app.user_center.routes import bp as user_bp
import config
from datetime import timedelta

app = Flask(__name__)

#设置session
app.secret_key = config.SCRET_KEY
app.permanent_session_lifetime = timedelta(minutes=30)

#注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(port=80, debug=True)