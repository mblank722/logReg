from __future__ import unicode_literals


from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
 #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def login(self, postData):

        # add vaidation here:

        user = User.objects.get(email=postData['email'])
        password = b"user.password"
        print "*"*50
        print "model: Login Method"
        print 'Email:',user.email
        print 'PW:',user.password
        print "ID:",user.id
        print "*"*5
        return ({'insertIsValid':True, 'id':user.id,' email':user.email, 'password':user.password })
        # print "Running a login function!"
        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"

    def register(self, postData):
        # print "Register a user here"
        # print "If successful, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] "


        # validate User date,:
        #if pass edits: insert users, return (True, user_id)
        #else: return (False, errors[])
        errors = []
        if len(postData['first_name'])== 0:
            errors.append("First Name is required, please enter.")
        if len(postData['last_name'])== 0:
            errors.append("Last Name is required, please enter.")

        if len(postData['email'])<= 5 or not EMAIL_REGEX.match (postData['email']):
            errors.append("Valid Email required, please enter valid email")

        if len(postData['password']) < 8:
            errors.append("Password is required and must contain at least 8 characters , please enter.")
        if (len(postData['password']) < 8) \
        and (postData['password'] != postData['confirm']):
            errors.append("Password and Password Confirmation must match, please reenter.")

        if len(errors) is not 0:
            return ({'insertIsValid' : False, 'errors' : errors})
        else:
            password = "super secret password"
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print hashed
            print len(hashed)
            hashed2 = bcrypt.hashpw(password, bcrypt.gensalt())
            print hashed2
            print bcrypt.hashpw(password,hashed)
            user = User.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],email =postData['email'], password=postData['password'])
            user.save()
        return ({'insertIsValid':True, 'id':user.id })
        # User.objects.get(id=1)
        # print 'in register method -  fn:'(u.first_name)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=False)
    password = models.CharField(max_length=30)
    birth_day = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # *************************
    objects = UserManager()
