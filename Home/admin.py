from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User

admin.site.site_header="BRICS"
admin.site.site_title="BRICS"

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(Slider)
admin.site.register(Event)
admin.site.register(GalleryImage)
admin.site.register(About)
admin.site.register(Video)
admin.site.register(Link)
admin.site.register(Report)