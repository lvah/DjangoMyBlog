# flask： 第三方模块flask-wtf
# Django: 自带的， 继承Django表但验证的类


"""


# 1.Form表单作用:
    1). 自动生成对应的html表单;
    2). 验证输入内容是否正确;  form.is_valid()


# 2. 如何创建Form表单?
class 表单名称(forms.Form):
    属性名 = forms.选择的区域Field(
        label="文字描述",       # 调用时： form.属性名.label
        required=True,
        min_length=2,
        max_length=10,


        # 1). 自定义错误信息
        # 如果出错， 会在前端显示对应出错的文字
         error_messages={
            'required': "用户名不能为空",
            'min_length': "长度不正确: 小于2"

        },


        # 2). 自定义Form的样式属性
        #  对于表单设置样式(自定义Form的样式属性);
         # <input type="text" class="form-control" placeholder="用户名">
        widget=forms.TextInput(attrs={
            'class': "form-control",
            "placeholder": "用户名",
        }),


        # 3). 自定义验证Form表单的内容是否合法?




        # 4). 自定义Form中的select
         widget=forms.Select(choices=[(0, "普通会员"), (1, "超级会员")])





    )
        # 5). 自定义Form中的select结合数据库

    # 为了防止数据库添加了数据或者删除了数据；
    # 但是页面对于下拉列表的数据有缓存， 导致不能及时同步;
    def __init__(self, *args, **kwargs):  # 每次创建对象时，都会执行下面代码;
        # 继承父类的构造函数
        super(LoginForm, self).__init__(*args, **kwargs)

        categories = [(cate.id, cate.name) for cate in Category.objects.all()]

        # 记忆一下:
        self.fields['category'] = forms.CharField(widget=forms.Select(choices=categories))







# 3. 视图函数里面常用的form的属性和方法?

    1). form.is_valid()    # 判断提交的数据(与form表单的定义设置进行对比)是否合法?
    2). form.cleaned_data  # 获取用户提交的数据， 并返回一个字典便于操作;
    3). form.errors        # 返回表单中所有错误信息对象;eg: form.errors.user


# 4. html中form的使用?
    1). {{ form.user.label }}
    2). {{ form.user }}
    3). {{ form.errors.user }}






"""
import re

from django import forms

# form.user.label
from django.core.exceptions import ValidationError

from blog.models import Category


class LoginForm(forms.Form):  # 自定义的验证表单类

    user = forms.CharField(
        label="用户名",
        required=True,
        min_length=2,
        max_length=10,
        error_messages={
            'required': "用户名不能为空",
            ' min_length': "长度不正确: 小于2"

        },
        # <input type="text" class="form-control" placeholder="用户名">
        widget=forms.TextInput(attrs={
            'class': "form-control",
            "placeholder": "用户名",
        })
    )

    # 密码区域
    pwd = forms.CharField(
        label="密码",
        # min_length=6,
        # max_length=8,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                "placeholder": "密码",
            }
        )
    )

    # flask：
    choice = [(0, "普通会员"), (1, "超级会员")]
    type = forms.IntegerField(
        label="会员类型",
        required=True,
        error_messages={
            'required': "用户类型未选择!"
        },
        widget=forms.Select(choices=choice)
    )
    categories = [(cate.id, cate.name) for cate in Category.objects.all()]
    category = forms.IntegerField(
        label="分类",
        required=True,
        error_messages={
            'required': "用户分类未选择!"
        },
        widget=forms.Select(choices=categories)
    )

    def phone_is_valid(value):
        print("value", value)
        # 编写正则判断电话号码是否合法?
        pattern = re.compile(r'^1\d{2}-?\d{4}-?\d{4}$')

        if not re.match(pattern, value):
            # 抛出异常
            raise  ValidationError("手机格式错误")

    phone = forms.CharField(
        label="电话",
        validators=[
            phone_is_valid,
        ]
    )


    # 为了防止数据库添加了数据或者删除了数据；
    # 但是页面对于下拉列表的数据有缓存， 导致不能及时同步;
    def __init__(self, *args, **kwargs):  # 每次创建对象时，都会执行下面代码;
        # 继承父类的构造函数
        super(LoginForm, self).__init__(*args, **kwargs)

        categories = [(cate.id, cate.name) for cate in Category.objects.all()]

        # 记忆一下:
        self.fields['category'] = forms.CharField(widget=forms.Select(choices=categories))

