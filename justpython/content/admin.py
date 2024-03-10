from django.contrib import admin

# Register your models here.
from .models import Course, Video, Pricing, Subscription

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Pricing)
admin.site.register(Subscription)