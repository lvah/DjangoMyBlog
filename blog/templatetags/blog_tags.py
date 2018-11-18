from django.db.models import Count

from blog.models import Post, Category, Tag
from django import template

register = template.Library()


# {% get_recent_post %}
@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates(
        'create_time',
        'month',
        order='DESC'
    )


@register.simple_tag
def get_category():
    """
     这个 Category.objects.annotate 方法和 Category.objects.all 有点类似，它会返回数据库中全部 Category 的记录，但同时它还会做一些额外的事情，
    在这里我们希望它做的额外事情就是去统计返回的 Category 记录的集合中每条记录下的文章数。
    :return:
    """
    # 给category对象中添加统计每个分类包含文章的个数.
    return Category.objects.annotate(num_posts=Count('post')
                                     # 筛选出分类中文章个数大于0的传递给html代码;
                                     ).filter(num_posts__gt=0)


@register.simple_tag
def get_tag():
    """
    :return:
    """
    # return  Tag.objects.all()
    return Tag.objects.annotate(num_posts=Count('post')
                                ).filter(num_posts__gt=0)
