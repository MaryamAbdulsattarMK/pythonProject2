import datetime
from django.utils import timezone

from django.db import models



# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 100)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title


# Create your models here.
class Sign_Up(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=250)
    password = models.CharField(max_length=50 )
    Sign_Up_date = models.DateField(auto_created=True,default=timezone.now)
    gender = models.BooleanField()
    accessForAdmin = models.BooleanField()


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    Sign_Up_id = models.ForeignKey(Sign_Up, on_delete=models.CASCADE,default=1)
    last_login = models.DateTimeField()


class Access_admin_for_users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name_id = models.ForeignKey('Sign_Up', on_delete=models.CASCADE,default=1)


class Type_item(models.Model):
    id = models.AutoField(primary_key=True)
    name_type = models.CharField(max_length=250)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    By_user= models.TextField()
    Date = models.DateField(auto_created=True,default=timezone.now)
    chat_count = models.IntegerField()
    Action = models.TextField()
    #date_of_edit = models.DateField(datetime.date,default="1-1-1950")



class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    message_date_time = models.DateTimeField()
    message_topic = models.CharField(max_length=250)
    message = models.TextField()
    user_name_id_sender = models.ForeignKey('Sign_Up', on_delete=models.CASCADE,default=1)
    #user_name_id_Resever = models.ForeignKey(Sign_Up, on_delete=models.CASCADE,default=0)


class Autherized_post(models.Model):
    id = models.AutoField(primary_key=True)
    user_name_id = models.ForeignKey('Sign_Up', on_delete=models.CASCADE,default=1)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE,default=1)
