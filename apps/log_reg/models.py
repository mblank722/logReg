from __future__ import unicode_literals

from django.db import models

# Create your models here.
 #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def login(self, postData):

        # add vaidation here:

        user = User.objects.get(email=postData['email'])
        print "*"*50
        print "model: Login Method"
        print 'Email:',user.email
        print 'PW:',user.password
        print "ID:",user.id
        print "*"*5
        # print "Running a login function!"
        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"

    def register(self, postData):
        # print "Register a user here"
        # print "If successful, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] "
        User.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],email =postData['email'], password=postData['password'])
        # User.objects.get(id=1)
        # print 'in register method -  fn:'(u.first_name)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birth_day = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # *************************
    objects = UserManager()
