from django.contrib import admin
from .models import Topbar, NavbarHeading, BannerText, AboutText, AboutFeature, ServiceHeading, Service, Member
# Register your models here.

admin.site.register(Member)
admin.site.register(Topbar)
admin.site.register(NavbarHeading)
admin.site.register(BannerText)
admin.site.register(AboutText)
admin.site.register(AboutFeature)
admin.site.register(Service)
admin.site.register(ServiceHeading)
# admin.site.register(HomeImg)