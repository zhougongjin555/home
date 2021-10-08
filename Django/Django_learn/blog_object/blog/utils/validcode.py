# coding ：UTF-8
# 开发人员： 
# 开发时间： 2021/8/28 15:27
# 文件名称： validcode.py
# 文件地址： blog/utils
# 开发工具： PyCharm
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def get_random_color():
    '''生成随机的颜色'''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def valid_code(request):
    '''生成随机的验证码'''
    img = Image.new('RGB', (270, 40), color=get_random_color())
    font = ImageFont.truetype('static/maobi.TTF', size=40)  # 字体文件

    # with open('valid_code.png', 'wb') as f:
    #     img.save(f, 'png')
    # with open('valid_code.png', 'rb') as f:
    #     data = f.read()

    # chr(65) - 90 对应大写A-Z ，chr(97) - 122对应小写a-z
    draw = ImageDraw.Draw(img)  # 画板生成图片

    # 生成随机的数字和大小写字母
    vcode = ''
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_up_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_up_alpha])
        vcode += random_char  # 验证码保存
        draw.text((i * 60, -5), random_char, get_random_color(), font=font)  # 设置画板上面的形状和样式
    print(vcode)

    request.session['vcode'] = vcode
    # 1, 生成随机字符串（adasdasafa）
    # 2， COOKIE{'sessionid': 随机字符串（adasdasafa）}
    # 3， django-session
    #     session-key       session-data
    #     adasdasafa        {'vcode': vcode}

    # 生成随机的噪点、噪线
    width = 250
    height = 31
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(50):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    f = BytesIO()  # 内存管理
    img.save(f, 'png')
    data = f.getvalue()

    return data


