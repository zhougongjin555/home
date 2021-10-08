import datetime
import time

import config
from utils.reslogin import relogin

class blogview(relogin):

    def select(self):
        '''选择想要的操作'''
        while True:
            msg = input('想干啥(q退出)：\n1：看博客列表\n2：发布博客\n').strip()
            if msg.lower() == 'q':
                break
            elif msg == '1':
                flag = 1
                self.seeblog_list()
                while flag:
                    flag = self.com_or_con()
            elif msg == '2':
                self.writeblog()
            else:
                print('输入错误')

    def com_or_con(self):
        msg = input('输入想看的博客序号(q返回)：').strip()
        if msg.lower() == 'q':
            return 0
        elif int(msg) in self.bid_list:
            blog_content_sql = f"select content from {config.TAB_CONTENTS} where title_id = {int(msg)};"
            blog_comment_sql = f"select username,comment from " \
                               f"(select * from {config.TAB_COMMENTS} left join (select uid,username from {config.TAB_USERS}) u " \
                               f"on u.uid = comments.user_id) a " \
                               f"where title_id = {int(msg)} " \
                               f"limit 10;"
            content_text = self.mysqlopts(blog_content_sql)  # 返回要看的文章的正文
            comment_list = self.mysqlopts(blog_comment_sql)  # 返回要看的文章的评论
            print(content_text['content'])
            if type(comment_list) == dict:
                print(f"用户 {comment_list['username']} 评论：{comment_list['comment']}")
            else:
                for i in comment_list:
                    print(f"用户 {i['username']} 评论：{i['comment']}")
            time.sleep(1)
            self._read(msg)
            time.sleep(1)
            choice = int(input("输入想对文章的操作(q返回)：\n1：点赞\n2：点踩\n3：推荐\n4：评论").strip())
            if choice == 1: # zan
                self._up(msg)
            elif choice == 2: # cai
                self._down(msg)
            elif choice == 3: # jian
                self._recommend(msg)
            elif choice == 4: # ping
                self._comment(int(msg), self.uid)
            else:
                print('输入无效')
            return 1
        else:
            print('输入无效')
            return 1

    def _read(self,msg):
        '''阅读+1'''
        up_sql = f"update brief set read_num=read_num+1 where bid={int(msg)};"
        self.mysqlopts(up_sql)
        print('阅读+1')

    def _up(self,msg):
        '''点赞'''
        up_sql = f"update brief set up_num=up_num+1 where bid={int(msg)};"
        self.mysqlopts(up_sql)
        print('点赞+1')

    def _down(self,msg):
        '''点踩'''
        up_sql = f"update brief set down_num=down_num+1 where bid={int(msg)};"
        self.mysqlopts(up_sql)
        print('点踩+1')

    def _recommend(self,msg):
        '''推荐'''
        up_sql = f"update brief set recommend_num=recommend_num+1 where bid={int(msg)};"
        self.mysqlopts(up_sql)
        print('推荐+1')

    def _comment(self,title_id,user_id):
        '''评论'''
        message = input('输入评论的内容：')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        up_sql = f"insert into comments(time,title_id,user_id,comment) values ('{now}', {title_id}, {user_id['uid']}, '{message}');"
        self.mysqlopts(up_sql)
        print("已添加评论")


    def writeblog(self):
        '''写博客'''
        while True:
            msg = input('写标题(q退出)：').strip()
            if msg.lower() == 'q':
                return
            if msg == '':
                print('不能为空')
            else:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                brief_sql = f"insert into {config.TAB_BRIEF}(title, writer_id, time) values ('{msg}', {self.uid['uid']}, '{now}');"
                self.mysqlopts(brief_sql)  # 将文章的标题写入brief数据库

                get_title_id_sql = f"select bid from {config.TAB_BRIEF} where title = '{msg}'"
                tid = self.mysqlopts(get_title_id_sql)['bid'] # 拿到新写入的博客的标题id

                while True:
                    content = input('写内容：').strip()
                    if not content:
                        print('不能为空')
                    else:
                        content_sql = f"insert into {config.TAB_CONTENTS}(title_id, content, time) values({tid},'{content}','{now}');"
                        self.mysqlopts(content_sql) # 将博客内容写入到数据库contents
                        print("已成功发布")
                        break
                break

    def split_page(self, num):
        blog_list_sql = f"select bid, title, username, time, read_num, comment_num, recommend_num, up_num, down_num from " \
                        f"(select * from {config.TAB_BRIEF} left join (select uid,username from {config.TAB_USERS}) u " \
                        f"on u.uid = brief.writer_id) a " \
                        f"limit 4 offset {num};"
        blog_list = self.mysqlopts(blog_list_sql)
        self.bid_list = [i['bid'] for i in blog_list]
        print('序号：标题  作者  时间  阅读量  评论数  推荐数  点赞数  点踩数')
        for i in blog_list:
            print(f"{i['bid']}: {i['title']}, {i['username']}, {i['time']}, "
                  f"{i['read_num']}, {i['comment_num']}, {i['recommend_num']}, {i['up_num']}, {i['down_num']}")
        print('\n')

    def seeblog_list(self):
        '''看博客列表'''
        list_count_sql = f"select count(0) from {config.TAB_BRIEF};"
        list_count = self.mysqlopts(list_count_sql) # 总页数
        list_count = list_count['count(0)']
        page_count = int(list_count/4 if list_count%4 == 0 else list_count/4+1)
        choice = int(input(f'请输入要查看的页数(共{page_count}页):'))
        if choice in range(1, page_count+1):
            print(f'\n正在展示第{choice}页')
            num = (choice - 1) * 4
            self.split_page(num)
        else:
            print('\n输入无效，展示首页')
            self.split_page(0)

    def seeblog_content(self):
        '''看博客文章'''
        pass

    def seeblog_comment(self):
        '''看博客的评论'''
        pass

    def run(self):
        usm = input('请输入你的用户名：').strip()
        pwd = input('请输入你的密码：').strip()
        uid_sql = f'select uid from {config.TAB_USERS} where username=(%s) and password=(%s);'
        self.uid = self.mysqlopts(uid_sql, (usm, pwd))
        # print(self.uid)
        if self.uid:
            print(f'欢迎用户{usm}使用此博客系统')
            '''登陆之后的功能'''
            self.select()
            pass
        else:
            print("\n用户不存在，欢迎注册\n")
            self.register()


