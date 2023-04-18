from django.db import models


class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name


class Visitor(models.Model):
    ip_address = models.CharField(max_length=45)
    count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address    


class About(models.Model):
    header = models.CharField(max_length=255)
    company_about = models.TextField()

    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    insta_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.header


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    