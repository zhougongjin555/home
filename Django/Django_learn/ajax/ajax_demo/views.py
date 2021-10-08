from django.shortcuts import render, HttpResponse

# Create your views here.
def index_func(request):

    return render(request, 'index.html')

def test_ajax_func(request):
    print(request.GET)           # 接受ajax返回的get请求

    return HttpResponse('200 OK')


def cal_ajax_func(request):
    print(request.POST)

    n1 = int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))
    ret = n1 * n2
    print('n1, n2:', n1, n2)
    return HttpResponse(ret)


def login_ajax_func(request):
    usn = request.POST.get('usn')
    pwd = request.POST.get('pwd')


    return HttpResponse('200 OK')



def files_func(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.FILES)
    #
    #     file_obj = request.FILES.get('file')
    #     with open(file_obj.name, 'wb') as f:
    #         for line in file_obj:
    #             f.write(line)
    #
    return render(request, 'files_upload.html')


def files_ajax_func(request):
    print(request.POST)   # 请求数据为urlencoded时候用POST接受数据
    # print(request.body)   # 请求为JSON时候用BODY接收数据
    file_obj = request.FILES.get('file')
    print('111',file_obj)
    with open(file_obj.name, 'wb') as f:
        for line in file_obj:
            f.write(line)

    return HttpResponse('200 OK')




