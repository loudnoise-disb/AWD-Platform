import pymysql
import config

def create_connection():
    """创建数据库连接"""
    try:
        conn = pymysql.connect(
            host=config.HOST,
            user=config.USER,
            passwd=config.PASSWD,
            database=config.DB
        )
        print(f"成功连接到数据库 有可能为无")
        return conn
    except pymysql.Error as e:
        print(f"错误: {e}")
        return None

def User_form():
    """
    一次性创建用户表并插入默认用户数据
    1. 字段：id(INT AUTO_INCREMENT), username(VARCHAR), key(VARCHAR), role (ENUM: blue or red)
    """
    # 数据库连接信息
    try:
        conn = create_connection()
        with conn.cursor() as cursor:
            # 1. 创建用户表（如果不存在）
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                `key` VARCHAR(100) NOT NULL,
                role ENUM('blue', 'red') NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            cursor.execute(create_table_sql)
            print("✅ 用户表创建成功（或已存在）")

            # 2. 插入一条示例用户数据（可扩展为多条）
            insert_sql = "INSERT INTO users (username, `key`, role) VALUES (%s, %s, %s)"
            cursor.execute(insert_sql, ('admin', 'supersecretkey', 'blue'))

            # 3. 提交更改
            conn.commit()
            print("✅ 默认用户插入成功")

    except Exception as e:
        print(f"❌ 出错啦：{e}")
    finally:
        conn.close()

def register_user(username: str, key: str, role: str):
    """
    用户注册函数：根据用户名、密钥和角色将数据插入到 users 表中

    :param username: 用户名（唯一）
    :param key: 用户密码或密钥（建议加密）
    :param role: 用户角色（blue 或 red）
    :return: None
    """
    # 简单校验
    if role not in ('blue', 'red'):
        print("❌ 角色必须是 'blue' 或 'red'")
        return 0

    conn = create_connection()

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (username, `key`, role) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, key, role))
            conn.commit()
            print(f"✅ 用户 {username} 注册成功，加入 {role} 队伍")
            return True
    except pymysql.err.IntegrityError:
        print("❌ 注册失败：用户名已存在")
    except Exception as e:
        print(f"❌ 注册出错：{e}")
    finally:
        conn.close()

def check_login(username: str, key: str) -> bool:
    """
    登录检查函数：验证用户名和密码是否正确
    :param username: 用户名
    :param key: 密码或密钥
    :return: True 表示登录成功，False 表示失败
    """
    conn = create_connection()

    try:
        with conn.cursor() as cursor:
            sql = "SELECT `key` FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                stored_key = result[0]
                return key == stored_key  # 明文对比，建议加密后对比
            else:
                return False
    except Exception as e:
        print(f"❌ 登录检查出错：{e}")
        return False
    finally:
        conn.close()

#获取用户画像
def get_user_profile_data(user_id):
    pass

if __name__ == '__main__':
    User_form()