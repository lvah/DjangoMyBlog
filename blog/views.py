from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.db.models.sql import OR
from django.shortcuts import render, get_object_or_404

# Create your views here.
from markdown import markdown, Markdown

from blog.models import Post, Tag
from comments.forms import CommentForm
from Blog.settings import  PER_PAGE

def index(request):

    # 对文章列表对象进行分页, 目前可以却四嗯每页多少条数据；
    pageinator  = Paginator(Post.objects.all(), PER_PAGE)
    # /
    # /?page=1
    # /?page=2
    # /?page=3
    # 获取当前的页数
    page = request.GET.get('page')

    # 假设要看-1页? 总共10页， 要看12页?要做异常处理;
    try:
        # post对象拥有的方法查看源代码:Page类；
        posts = pageinator.page(page)
        # 获取宗页数；
        print(pageinator.num_pages)
        # 获取页数显示列表; range(1,11), 将舍page_range有100页， 如何让显示参考flask的设置；
        print(pageinator.page_range)
    except (PageNotAnInteger, EmptyPage):
        # 如果传进来的时字符串， 默认去看第一页;
        posts = pageinator.page(1)


    return render(request, 'blog/index.html',
                  context={'title': '博客首页',
                           'posts': posts,
                           'paginator': pageinator,
                           'page_nums': pageinator.page_range })

def detail(request, id):
    post = Post.objects.get(id=id)
    post.add_views()
    # post.body  = markdown(
    #     post.body,
    #     extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #         'markdown.extensions.toc',
    #     ],
    #     output_format='html'
    # )
    #
    # md对象里面包含toc属性， 可以获取里面的目录;
    md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ],
        output_format='html'
    )
    post.body = md.convert(post.body)

    # 动态给post对象添加toc属性， 并没有保存到数据库中； md.toc是该博客对象目录的html代码
    post.toc = md.toc
    # print(post.toc)

    # 用户评论的表单；(去comment app 里面创建表单对象)
    form = CommentForm()

    # 用户的所有评论；(获取当前文章的所有评论)
    comments = Paginator(post.comment_set.all(), PER_PAGE)

    return render(request, 'blog/detail.html',
                  context={
                      'post': post,
                      'form': form,
                      'comments': comments,
                  })


def archive(request, year, month):  # 2018 10
    posts = Post.objects.filter(
        create_time__year=year,
        create_time__month=month
    ).order_by('-create_time')

    return render(request, 'blog/index.html',
                  context={
                      'posts': posts
                  })


def category(request, id):
    posts = Post.objects.filter(category_id=id).order_by('-create_time')
    return render(request, 'blog/index.html',
                  context={
                      'posts': posts
                  })


def tag(request, id):
    # 先找出TagId对应的tag对象；
    tag = get_object_or_404(Tag, id=id)
    posts = Post.objects.filter(tags=tag).order_by('-create_time')
    return render(request, 'blog/index.html',
                  context={
                      'posts': posts
                  })


def search(request):
    # get方法提交数据的。 如何获取get方法提交的数据;
    query = request.GET.get('query', None)  # westos
    # Q对象包装查询逻辑， 找出标题中包含query或者文章内容中包含query的博客对象;
    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    # 如果没有找到， 返回一个报错信息；
    if not posts:
        return  render(request, 'blog/index.html',
                       context={
                           'posts':posts,
                           'message':"没有找到相关信息"
                       })
    else:
        return  render(request, 'blog/index.html',
                       context={
                           'posts':posts,

                       })




