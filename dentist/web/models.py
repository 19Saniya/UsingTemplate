from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Topbar(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    youtube_url = models.CharField(max_length=255)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, " % (
        self.email, self.phone, self.facebook_url, self.twitter_url, self.linkedin_url, self.instagram_url,
        self.youtube_url)


class NavbarHeading(models.Model):
    navbar_heading = models.CharField(max_length=255)
    def __str__(self):
        return "%s" % self.navbar_heading



class BannerText(models.Model):
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)
    text4 = models.CharField(max_length=255)
    banner_img = models.ImageField(upload_to='banner', default=None, null=True, blank=True)

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.text1, self.text2, self.text3, self.text4, self.banner_img)


class AboutText(models.Model):
    about_img = models.ImageField(upload_to='about')
    about_text1 = models.CharField(max_length=150)
    about_text2 = models.CharField(max_length=255)

    def __str__(self):
        return "%s, %s, %s" % (self.about_img, self.about_text1, self.about_text2)


class AboutFeature(models.Model):
    about_icon = models.CharField(max_length=255)
    about_adjective = models.CharField(max_length=30)
    about_noun = models.CharField(max_length=30)

    def __str__(self):
        return "%s, %s, %s" % (self.about_icon, self.about_adjective, self.about_noun)



class ServiceHeading(models.Model):
    service_heading = models.CharField(max_length=255)
    def __str__(self):
        return "%s" % self.service_heading


class Service(models.Model):
    service_icon = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_detail = models.CharField(max_length=255)

    def __str__(self):
        return "%s, %s, %s" % (self.service_icon, self.service_name, self.service_detail)

# class HomeImg(models.Model):
#     banner_img = models.ImageField(upload_to='banner', default=None, null=True, blank=True)
#
#     def __str__(self):
#         return "%s" % self.banner_img

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on-delete==models.CASCADE)
