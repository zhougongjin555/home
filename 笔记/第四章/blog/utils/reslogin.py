'''定义登录以及注册函数'''
import pymysql
import datetime

import config

class relogin:
    def __init__(self):
        pass

    def login(self):
        pass

    def register(self):
        while True:
            username = input("请输入你的账号：").strip()
            password1 = input("请输入你的密码：").strip()
            password2 = input("请再次输入确认你的密码：").strip()
            name = input("请输入你的昵称：").strip()
            phone = input('请输入你的手机号：').strip()
            email = input('请输入你的emial')
            if password1 != password2:
                print('\n两次输入的结果不一致,请重新注册\n')
                continue
            elif any(i == '' for i in [username, password1, name, phone, email]):
                print('\n有注册字段为空,请重新注册\n')
                continue
            else:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sql = f'insert into {config.TAB_USERS}(username, password, name, phone, email, time) \
                        values{username, password1, name, phone, email, now}; '
                print(sql)
                self.mysqlopts(sql)
                print('\n注册成功，请登录\n')
                self.run()
                break

    @staticmethod
    def mysqlopts(sql, *args):
        sql_connect = pymysql.connect(host=config.HOST,
                                      port=config.PORT,
                                      user=config.USER,
                                      password=config.PASSWORD,
                                      database=config.DATABASE,
                                      charset='utf8')
        cursor = sql_connect.cursor(pymysql.cursors.DictCursor)  # 字典形式返回查找结果
        cursor.execute(sql, *args)
        if sql.startswith('select'):
            data = cursor.fetchall()
            cursor.close()
            sql_connect.close()
            if len(data) == 1:
                return data[0]
            else:
                return data
        elif sql.startswith('insert') or sql.startswith('update'):
            sql_connect.commit()
            cursor.close()
            sql_connect.close()
            return


    # def run(self):
    #     usm = input('请输入你的用户名：').strip()
    #     pwd = input('请输入你的密码：').strip()
    #     uid_sql = f'select uid from {config.TAB_USERS} where username=(%s) and password=(%s);'
    #     self.uid = self.mysqlopts(uid_sql, (usm, pwd))
    #     # print(self.uid)
    #     if self.uid:
    #         print(f'欢迎用户{usm}使用此博客系统')
    #         '''登陆之后的功能'''
    #
    #         pass
    #     else:
    #         print("\n用户不存在，欢迎注册\n")
    #         self.register()

#
#
# if __name__ == '__main__':
#     loginer = relogin() # 实例化对象
#     loginer.run()
#
#
