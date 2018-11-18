from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.



# 处理用户提交的评论信息;
# 确定url(路由)
from blog.models import Post
from  comments.forms import CommentForm
from comments.models import Comment


def post_comment(request, pk):
    # 1). 找出要评论的文章对象
    post = get_object_or_404(Post, pk=pk)
    # print(post)


    # 2). 如果用户提交评论；
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        # 判断是否合法？
        if form.is_valid():
            # # 保存到数据库中;

            # 会保存用户提交的相关信息到数据库中， 但是用户给哪篇博客评论， 并没有保存;
            # commit=False, 并没有提交到数据库中;
            comment = form.save(commit=False)

            # 将评论和被评论的博客关联;
            comment.post = post

            # 保存并写入数据库;
            comment.save()

            # data = request.POST
            #
            # comment = Comment(user=data['user'], email=data['email'],
            #         text=data['text'], post = post)
            # comment.save()
            return redirect(post.get_url())
        else:
            return render(request, 'blog/detail.html',
                          context={
                              'errors': form.errors
                          })

    # 3). 如果不是post请求， 访问用户的详情页
    return redirect(post.get_url())
