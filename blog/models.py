from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"
    name = models.CharField(max_length=100,unique=True,verbose_name="文章分类")

    def __str__(self):
        return "%s" %(self.name)

class Tag(models.Model):
    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = "文章标签"

    name = models.CharField(max_length=50, unique=True, verbose_name="标签名")

    def __str__(self):
        return "%s" % (self.name)

class Post(models.Model):
    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"
    title = models.CharField(max_length=50,unique=True,verbose_name="博客标题")
    body = models.TextField(verbose_name="博客正文")
    create_time = models.DateTimeField(verbose_name="发表时间")
    # blank=True, 文章摘要可以为空;
    summary = models.CharField(max_length=200,unique=True,blank=True, verbose_name="摘要")

    category = models.ForeignKey(Category,verbose_name="博客分类")
    tags = models.ManyToManyField(Tag,verbose_name="博客标签")
    author = models.ForeignKey(User,verbose_name="作者")
    views = models.PositiveIntegerField(default=0,verbose_name="阅读量")

    def __str__(self):
        return "%s" % (self.title)

    def get_url(self):
        return reverse("blog:detail",kwargs={'id':self.id})


    def add_views(self):
        self.views +=1
        self.save(update_fields=['views'])


    # def save(self, *args, **kwargs):
    #     if not self.summary:
    #         # 如果没有摘要， 则设置摘要文章的前200个字符;
    #         self.summary = self.body[:200]
    #     super(Post, self).save(*args, **kwargs)

