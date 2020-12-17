from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Start adding my validations
        if len(postData['real_name']) < 1:
            errors['real_name'] = "Name is required!"
        if len(postData['username']) < 4:
            errors['username'] = "Username must be at least 4 characters!"
        if len(postData['username']) < 1:
            errors['username'] = "Username is required!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 1:
            errors['email'] = "Email is required!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if len(postData['password']) < 1:
            errors['password'] = "Password is required!"
        if postData['password'] != postData['pass_confirm']:
            errors['password'] = "Password and password confirm do not match!"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            log_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), log_user.password.encode()):
                errors['password'] = "Invalid login attempt"
        else:
            errors['password'] = "Invalid login attempt"
        return errors


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class CardManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = "Name is required!"
        if len(postData['image']) < 1:
            errors['image'] = "Image is required!"
        if len(postData['card_type']) < 1:
            errors['card_type'] = "Card type is required!"
        return errors 

class Card(models.Model):
    name = models.CharField(max_length=45)
    image = models.CharField(max_length=255)
    card_type = models.CharField(max_length=45)
    owners = models.ManyToManyField(User, related_name="collection")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CardManager()