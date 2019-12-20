from django.contrib import admin

from learning_logs.models import Topic, Entry

#这行代码让Django通过管理网站注册Topic
admin.site.register(Topic)
admin.site.register(Entry)
