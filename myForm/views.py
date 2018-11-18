from django.shortcuts import render, HttpResponse, redirect
from myForm.forms import  LoginForm
# Create your views here.




# 如果是GET请求的话， 视图函数需要编写两个;
def search_form(request):
    return render(request, 'myForm/index.html')

#
def search(request):
    # 1). 获取用户提交的数据(GET方法提交的；)
    #  Flask: request.args.get('search_key')
    #  Django：


    print(request.GET)

    if request.GET['search_key']:
        message = "搜索内容为%s" %(request.GET['search_key'])
    else:
        message = "你提交了空数据"

    return HttpResponse(message)




# 1. 三个重要方法： is_valid, cleand_data, errors
# 如果是POST请求的话， 视图函数需要编写1个;
def search_post(request):
    # 获取请求方法
    if request.method == 'POST':
        data = request.POST['search_key']
        return  HttpResponse("搜索内容为%s" %(data))
    else:
        return  render(request, 'myForm/post.html')




def login(request):
    if request.method == 'POST':
        # 创建验证表单类， 将用户请求的POST对象传入表单验证类进行验证;
        form = LoginForm(request.POST)
        if form.is_valid():  # 检测POST提交的数据是否验证成功;
            print(form.cleaned_data)  # 获取用户提交的数据， 并返回一个字典便于操作;
            user = form.cleaned_data['user']
            pwd = form.cleaned_data['pwd']
            # 判断用户名和密码是否正确?
            if user == 'root' and pwd == 'root':
                # 如果正确， 跳转到网站首页；
                return  redirect('/')
            else:
                return  render(request, 'myForm/login.html',
                           context={
                               'form':form,
                               'message': "用户名和密码错误"
                           })
        else:
            #  form.errors: 返回表单中所有错误信息对象;
            # user:    form.errors.user
            # pwd:    form.errors.pwd
            #  如果错误， 重新登录，并显示错误原因;
            return  render(request, 'myForm/login.html',
                           context={
                               'form':form,
                               'errors': form.errors
                           })
    else:
        form = LoginForm()
        return  render(request, 'myForm/login.html',
                       context={
                           'form':form
                       })






















