# 授权码： ZKKCAQDPVURWDNBA
# 地址：smpt.163.com

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# ### 1.邮件内容配置 ###
msg = MIMEText("周公瑾", 'html', 'utf-8')
msg['From'] = formataddr(["周公瑾", "zhouggongjin@163.com"], )
msg['Subject'] = "work report"



# ### 2.发送邮件 ###
server = smtplib.SMTP_SSL("smpt.163.com")
server.login("zhouggongjin@163.com", "ZKKCAQDPVURWDNBA")
server.sendmail("zhouggongjin@163.com", "850635521@qq.com", msg.as_string())
server.quit()
