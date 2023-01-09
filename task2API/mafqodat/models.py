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
    Sign_Up_date = models.DateTimeField()
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
    auther_id = models.ForeignKey('Sign_Up', on_delete=models.CASCADE,default=1)
    name_missing_item = models.TextField()
    type_item_id = models.ForeignKey('Type_item', on_delete=models.CASCADE,default=1)
    image = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    post_detail = models.TextField()
    uploaded_date = models.DateTimeField()
    edit_date = models.DateTimeField()
    Aprovement_Not = models.BooleanField()
    active = models.IntegerField()
    access_admin_user = models.ForeignKey('Access_admin_for_users', on_delete=models.CASCADE,default=1)


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
