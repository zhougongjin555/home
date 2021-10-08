from django.shortcuts import render,HttpResponse
import datetime

from demo.models import Employee
# Create your views here.


def index_func(request):
    ''':cvar
    模板语法：
    {{ }}：渲染变量
        1，深度查询，句点符
        2，过滤器


    {% %}：渲染标签

    '''

    name = 'zhougongjin'
    i = 10
    li = [11, 22, 33]
    info = {'name':'zhougongjin', 'age': 18}
    bool = True


    class person:
        def __init__(self, name, sex):
            self.name = name
            self.sex = sex

    zhuge = person('zhugeliang', 'man')
    zhouyv = person('zhougongjin', 'woman')

    persons = [zhuge, zhouyv]

    ctime = datetime.datetime.now()

    return render(request, 'index.html', locals())# locals()传入所有的局部变量


def login(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        print(request.POST)
        usn = request.POST.get('usn')
        pwd = request.POST.get('pwd')
        if usn == 'zhougongjin' and pwd == '666':
            return HttpResponse('200 OK')
        else:
            return HttpResponse('用户不存在')

def sql_func(request):

    # 创建一条记录
    # obj = Employee(name='zhougongjin', gender=1, birthday='2000-2-25', department='12', salary='20000.00')
    # obj.save()

    # 用objects创建对象
    # 返回值是生成的对象记录
    # Employee.objects.create(name='zhougongjin', gender=1, birthday='2000-2-25', department='12', salary='20000.00')

    # # 增删改查
    # emps = Employee.objects.all()
    # for emp in emps:
    #     print(emp.gender)
    #
    # # (2) fliter,筛选器
    # woman_list = Employee.objects.filter(gender=0)
    # print(woman_list)
    # woman_first = Employee.objects.filter(gender=0).first()
    # print(woman_first)
    #
    # # (3) get()  有且只有一个查询结果时才有意义  返回值:model对象
    # employee_obj = Employee.objects.get(department="22")
    # print(employee_obj)
    # employee_obj = Employee.objects.get(gender=0) # 不存在或者查询超出一个结果会报错
    # print(employee_obj)
    #
    # # (4) exclude 返回值:queryset对象
    # ret = Employee.objects.exclude(title="go") # 筛选不匹配的数据
    # print(ret)
    #
    # # (5) order_by   调用者: queryset对象   返回值:  queryset对象
    # ret = Employee.objects.all().order_by("-id")  # 反向排序
    # ret = Employee.objects.all().order_by("price","id")  # 多条件排序
    # print(ret)
    #
    # # (6) count()   调用者: queryset对象   返回值: int
    # ret = Employee.objects.all().count()
    # print(ret)
    #
    # # (7) exists
    # ret = Employee.objects.all().exists()

    # (8) values()  方法  调用者: queryset对象  返回值:queryset对象(里面放了个字典)
    # ret = Employee.objects.all().values('name')
    # print(ret)

    # (9) values_list 方法  调用者: queryset对象  返回值:queryset对象(里面放了个元组)
    # ret = Employee.objects.all().values_list('name')
    # print(ret)

    # (10) distinct 去重，不能指全字段，因为有主键，没意义
    # ret = Employee.objects.all().values('name').distinct()
    # print(ret)



##################################模糊查询###############################################
    
    # ret = Employee.objects.filter(salary__gt=10000)
    # print(ret)


##################################删除对象###############################################
    # delete调用对象，queryset对象和model对象
    # ret = Employee.objects.filter(id=1).delete()
    # print(ret)
    #
    # ret = Employee.objects.all().first().delete()
    # print(ret)

##################################修改对象###############################################
    # update只能由queryset来调用
    Employee.objects.filter(name='zhugeliang').update(salary=10000)







    return HttpResponse('200 OK')