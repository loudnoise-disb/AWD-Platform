from flask import Blueprint, render_template, request, redirect
from app.models import register_user, check_login

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

# 登录页面
@bp.route('/login')
def login_page():
    return render_template('login.html')

# 登录处理逻辑
@bp.route('/submit', methods=['POST'])
def login_submit():
    id = request.form.get('id')
    key = request.form.get('key')
    if check_login(id, key):
        return render_template('home.html')
    else:
        return "登录失败，请检查用户名或密码"

# 注册页面
@bp.route('/register')
def register_page():
    return render_template('register.html')

# 注册处理逻辑
@bp.route('/do_register', methods=['POST'])
def register_submit():
    id = request.form.get('id')
    key = request.form.get('key')
    role = request.form.get('role')
    if register_user(id, key, role):
        return redirect('/auth/login')  # 注册成功跳转登录页
    else:
        return "注册失败，用户可能已存在"
