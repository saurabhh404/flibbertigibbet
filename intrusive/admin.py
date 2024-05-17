from django.contrib import admin

from intrusive.models import Post
from intrusive.models import SideNote
from intrusive.models import Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(SideNote)
admin.site.register(Tag)
