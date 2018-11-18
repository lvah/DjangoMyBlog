


from django import  forms
# class CommentForm(forms.Form):
#     user = forms.CharField(
#         label="用户名",
#         required=True,
#     )
#
#     email  = forms.EmailField(
#         label="邮箱",
#         required=True
#     )
#
#     text = forms.CharField(
#         label="评论",
#         widget=forms.TextInput()
#
#     )


# 将表单和数据库结合;
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # 表明这个表单对应的数据库模型
        model = Comment
        # 表明表单需要显示的字段
        fields= ['user', 'email', 'text']


