from django.db import models
from django.utils.six import python_2_unicode_compatible
from blog.models import Post
from users.models import UserProfile

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255)
    # #url = models.URLField(blank=True)
    name = models.ForeignKey(UserProfile,verbose_name=u'user')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post,verbose_name=u'blog')

    class Meta:
        verbose_name = u'comments'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.text[:20]