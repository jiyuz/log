from django.db import models
from django.contrib.auth.models import User


class Topic (models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        #嵌套类，设置了一个特殊属性，让Django在需要时使用Entris来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            """返回模型的字符串表示"""
            return self.text[:50] + "..."
        else:
            return self.text
