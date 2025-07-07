from flask import Blueprint, render_template

bp = Blueprint('user_center', __name__, url_prefix='/user_center', template_folder='templates')

"""
用户信息分四块：
1. 身份
2. 当前画像信息
3. 历次画像信息(给上能导出png的链接）
4. 解题情况（可以用文字表述）
"""
@bp.route('/')
def show_user():
    user_data = {
        'username': '齐家骏',
        'role': '红队',
        'score': 89.5,
        'skills': 'Web渗透, 内网提权',
        'solved_count': 42,
        'accuracy': 78.3,
        'favorite_topics': 'Reverse, Pwn',
        'radar_values': [90, 60, 70, 85, 88, 50],  # 雷达图六个维度得分
        'history': [
            {'date': '2025-06-01', 'score': 75, 'tags': '新手试炼'},
            {'date': '2025-06-15', 'score': 88, 'tags': '中级提升'},
            {'date': '2025-07-01', 'score': 92, 'tags': '高阶突破'},
        ]
    }
    return render_template('user_center.html', user=user_data)