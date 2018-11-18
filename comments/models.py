from django.db import models

# Create your models here.



from django.contrib.auth.models import User

# 用户：评论===（1：n）
# 文章:评论====(1 : n)
class Comment(models.Model):
	user = models.ForeignKey(User)
	email = models.EmailField(max_length=50)
	text = models.TextField()
	# 如果修改评论的内容， 重新保存时， 会把created_time的值更新为当前的时间；
	created_time = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('blog.Post')

	def __str__(self):
		return self.text[:10]
