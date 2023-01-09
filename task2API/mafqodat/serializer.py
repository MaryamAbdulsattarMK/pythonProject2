from rest_framework import serializers
from .models import Sign_Up, Autherized_post, Chat, Post, Type_item, Access_admin_for_users, Login


class Sign_upSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign_Up
        fields = ('id', 'user_name', 'phone_number','location','password','Sign_Up_date','gender','accessForAdmin')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id','Sign_Up_id','last_login')


class Access_adminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_admin_for_users
        fields = ('id','user_name_id')

class Type_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_item
        fields = ('id', 'name_type')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'auther_id','name_missing_item','type_item_id','image','location','contact_number','post_detail','uploaded_date',' edit_date','Aprovement_Not','active','access_admin_user')

class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'message_date_time','message_topic','message_detial','user_name_id_sender','user_name_id_Resever')

class Autherized_postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autherized_post
        fields = ('id', 'user_name_id','post_id')
