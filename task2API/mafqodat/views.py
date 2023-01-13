from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Sign_Up, Autherized_post, Chat, Post, Type_item, Access_admin_for_users, Login
from .serializer import Sign_upSerializer, Autherized_postSerializer, chatSerializer, PostSerializer, \
    Access_adminSerializer, LoginSerializer, Type_itemSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated  # new import

from .models import Todo
from .serializer import TodoSerializer


# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    permission_classes = (IsAuthenticated,)  # permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    permission_classes = (IsAuthenticated,)  # permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@csrf_exempt
def Sign_UpApi(request,Sign_Up_Id=0):
    if request.method == 'GET':
        signUp = Sign_Up.objects.all()
        signUp_serializer = Sign_upSerializer(signUp, many=True)
        return JsonResponse(signUp_serializer.data, safe=False)
    elif request.method == 'POST':
        signUp_data = JSONParser().parse(request)
        signUp_serializer = Sign_upSerializer(data=signUp_data)
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        signUp_data = JSONParser().parse(request)
        Sign_Ups = Sign_Up.objects.get(id=signUp_data['id'])
        signUp_serializer = Sign_upSerializer(Sign_Ups, data=signUp_data)
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Sign_Ups = Sign_Up.objects.get(id=Sign_Up_Id)
        Sign_Ups.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Autherized_postApi(request,Autherized_Id=0):
    if request.method == 'GET':
        autherizedPost = Autherized_post.objects.all()
        Autherized_post_serializer = Autherized_postSerializer(autherizedPost, many=True)
        return JsonResponse(Autherized_post_serializer.data, safe=False)
    elif request.method == 'POST':
        autherized_data = JSONParser().parse(request)
        Autherized_post_serializer = Autherized_postSerializer(data=autherized_data)
        if Autherized_post_serializer.is_valid():
            Autherized_post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        autherized_data = JSONParser().parse(request)
        autherizeds = Autherized_post.objects.get(id=autherized_data['id'])
        Autherized_post_serializer = Autherized_postSerializer(autherizeds, data=autherized_data)
        if Autherized_post_serializer.is_valid():
            Autherized_post_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Autherized_posts = Autherized_post.objects.get(id=Autherized_Id)
        Autherized_posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def ChatApi(request,chat_id=0):
    if request.method == 'GET':
        chats = Chat.objects.all()
        chats_serializer = chatSerializer(chats, many=True)
        return JsonResponse(chats_serializer.data, safe=False)
    elif request.method == 'POST':
        chats_data = JSONParser().parse(request)
        chats_serializer = chatSerializer(data=chats_data)
        if chats_serializer.is_valid():
            chats_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        chats_data = JSONParser().parse(request)
        chats = Chat.objects.get(id=chats_data['id'])
        chats_serializer = chatSerializer(chats, data=chats_data)
        if chats_serializer.is_valid():
            chats_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        chats = Chat.objects.get(id=chat_id)
        chats.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def PostApi(request,post_id=0):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
    elif request.method == 'POST':
        posts_data = JSONParser().parse(request)
        posts_serializer = PostSerializer(data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        posts_data = JSONParser().parse(request)
        posts = Post.objects.get(id=posts_data['id'])
        posts_serializer = PostSerializer(posts, data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        posts = Post.objects.get(id=post_id)
        posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Type_itemApi(request,post_id=0):
    if request.method == 'GET':
        Type_items = Type_item.objects.all()
        Type_item_serializer = Type_itemSerializer(Type_items, many=True)
        return JsonResponse(Type_item_serializer.data, safe=False)
    elif request.method == 'POST':
        type_items_data = JSONParser().parse(request)
        Type_item_serializer = Type_itemSerializer(data=type_items_data)
        if Type_item_serializer.is_valid():
            Type_item_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        posts_data = JSONParser().parse(request)
        posts = Post.objects.get(id=posts_data['id'])
        posts_serializer = PostSerializer(posts, data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        posts = Post.objects.get(id=post_id)
        posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Access_admin_for_usersApi(request,Access_admin_id=0):
    if request.method == 'GET':
        access_admin_for_user = Access_admin_for_users.objects.all()
        Access_admin_for_users_serializer = Access_adminSerializer(access_admin_for_user, many=True)
        return JsonResponse(Access_admin_for_users_serializer.data, safe=False)
    elif request.method == 'POST':
        access_admin_for_user = JSONParser().parse(request)
        Access_admin_for_users_serializer = Access_adminSerializer(data=access_admin_for_user)
        if Access_admin_for_users_serializer.is_valid():
            Access_admin_for_users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        access_admin_for_user = JSONParser().parse(request)
        access_admin_for_users = Access_admin_for_users.objects.get(id=access_admin_for_user['id'])
        Access_admin_for_users_serializer = Access_adminSerializer(access_admin_for_users, data=access_admin_for_user)
        if Access_admin_for_users_serializer.is_valid():
            Access_admin_for_users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        access_admin_for_users = Access_admin_for_users.objects.get(id=Access_admin_id)
        access_admin_for_users.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def LoginApi(request,login_id=0):
    if request.method == 'GET':
        logins = Login.objects.all()
        logins_serializer = LoginSerializer(logins, many=True)
        return JsonResponse(logins_serializer.data, safe=False)
    elif request.method == 'POST':
        logins_data = JSONParser().parse(request)
        logins_serializer = LoginSerializer(data=logins_data)
        if logins_serializer.is_valid():
            logins_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        logins_data = JSONParser().parse(request)
        logins = Login.objects.get(id=logins_data['id'])
        logins_serializer = LoginSerializer(logins, data=logins_data)
        if logins_serializer.is_valid():
            logins_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        logins = Login.objects.get(id=login_id)
        logins.delete()
        return JsonResponse("Deleted Successfully", safe=False)







@csrf_exempt
def Sign_UpAPI(request,Sign_Up_Id=0):
    if request.method == 'GET':
        signUp = Sign_Up.objects.get(id=Sign_Up_Id)
        signUp_serializer = Sign_upSerializer(signUp)
        return JsonResponse(signUp_serializer.data, safe=False)
    elif request.method == 'POST':
        signUp_data = JSONParser().parse(request)
        signUp_serializer = Sign_upSerializer(data=signUp_data)
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        signUp_data = JSONParser().parse(request)
        Sign_Ups = Sign_Up.objects.get(id=signUp_data['id'])
        signUp_serializer = Sign_upSerializer(Sign_Ups, data=signUp_data)
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Sign_Ups = Sign_Up.objects.get(id=Sign_Up_Id)
        Sign_Ups.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Autherized_postAPI(request,Autherized_Id=0):
    if request.method == 'GET':
        autherizedPost = Autherized_post.objects.get(id=Autherized_Id)
        Autherized_post_serializer = Autherized_postSerializer(autherizedPost)
        return JsonResponse(Autherized_post_serializer.data, safe=False)
    elif request.method == 'POST':
        autherized_data = JSONParser().parse(request)
        Autherized_post_serializer = Autherized_postSerializer(data=autherized_data)
        if Autherized_post_serializer.is_valid():
            Autherized_post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        autherized_data = JSONParser().parse(request)
        autherizeds = Autherized_post.objects.get(id=autherized_data['id'])
        Autherized_post_serializer = Autherized_postSerializer(autherizeds, data=autherized_data)
        if Autherized_post_serializer.is_valid():
            Autherized_post_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Autherized_posts = Autherized_post.objects.get(id=Autherized_Id)
        Autherized_posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def ChatAPI(request,chat_id=0):
    if request.method == 'GET':
        chats = Chat.objects.get(id=chat_id)
        chats_serializer = chatSerializer(chats)
        return JsonResponse(chats_serializer.data, safe=False)
    elif request.method == 'POST':
        chats_data = JSONParser().parse(request)
        chats_serializer = chatSerializer(data=chats_data)
        if chats_serializer.is_valid():
            chats_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        chats_data = JSONParser().parse(request)
        chats = Chat.objects.get(id=chats_data['id'])
        chats_serializer = chatSerializer(chats, data=chats_data)
        if chats_serializer.is_valid():
            chats_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        chats = Chat.objects.get(id=chat_id)
        chats.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def PostAPI(request,post_id=0):
    if request.method == 'GET':
        posts = Post.objects.get(id=post_id)
        posts_serializer = PostSerializer(posts)
        return JsonResponse(posts_serializer.data, safe=False)
    elif request.method == 'POST':
        posts_data = JSONParser().parse(request)
        posts_serializer = PostSerializer(data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        posts_data = JSONParser().parse(request)
        posts = Post.objects.get(id=posts_data['id'])
        posts_serializer = PostSerializer(posts, data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        posts = Post.objects.get(id=post_id)
        posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Type_itemAPI(request,post_id=0):
    if request.method == 'GET':
        Type_items = Type_item.objects.get(id=post_id)
        Type_item_serializer = Type_itemSerializer(Type_items)
        return JsonResponse(Type_item_serializer.data, safe=False)
    elif request.method == 'POST':
        type_items_data = JSONParser().parse(request)
        Type_item_serializer = Type_itemSerializer(data=type_items_data)
        if Type_item_serializer.is_valid():
            Type_item_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        posts_data = JSONParser().parse(request)
        posts = Post.objects.get(id=posts_data['id'])
        posts_serializer = PostSerializer(posts, data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        posts = Post.objects.get(id=post_id)
        posts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Access_admin_for_usersAPI(request,Access_admin_id=0):
    if request.method == 'GET':
        access_admin_for_user = Access_admin_for_users.objects.get(id=Access_admin_id)
        Access_admin_for_users_serializer = Access_adminSerializer(access_admin_for_user)
        return JsonResponse(Access_admin_for_users_serializer.data, safe=False)
    elif request.method == 'POST':
        access_admin_for_user = JSONParser().parse(request)
        Access_admin_for_users_serializer = Access_adminSerializer(data=access_admin_for_user)
        if Access_admin_for_users_serializer.is_valid():
            Access_admin_for_users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        access_admin_for_user = JSONParser().parse(request)
        access_admin_for_users = Access_admin_for_users.objects.get(id=access_admin_for_user['id'])
        Access_admin_for_users_serializer = Access_adminSerializer(access_admin_for_users, data=access_admin_for_user)
        if Access_admin_for_users_serializer.is_valid():
            Access_admin_for_users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        access_admin_for_users = Access_admin_for_users.objects.get(id=Access_admin_id)
        access_admin_for_users.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def LoginAPI(request,login_id=0):
    if request.method == 'GET':
        logins = Login.objects.get(id=login_id)
        logins_serializer = LoginSerializer(logins)
        return JsonResponse(logins_serializer.data, safe=False)
    elif request.method == 'POST':
        logins_data = JSONParser().parse(request)
        logins_serializer = LoginSerializer(data=logins_data)
        if logins_serializer.is_valid():
            logins_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        logins_data = JSONParser().parse(request)
        logins = Login.objects.get(id=logins_data['id'])
        logins_serializer = LoginSerializer(logins, data=logins_data)
        if logins_serializer.is_valid():
            logins_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        logins = Login.objects.get(id=login_id)
        logins.delete()
        return JsonResponse("Deleted Successfully", safe=False)





def sign_upapi(request,Sign_Up_Id=0):
    if request.method == 'GET':
        signUp = Sign_Up.objects.get(id=Sign_Up_Id)
        signUp_serializer = Sign_upSerializer(signUp)
        return JsonResponse(signUp_serializer.data, safe=False)
    elif request.method == 'POST':
        signUp_data = JSONParser().parse(request)
        signUp_serializer = Sign_upSerializer(data=signUp_data)
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        signUp_data = JSONParser().parse(request)
        Sign_Ups = Sign_Up.objects.get(id=signUp_data['id'])
        signUp_serializer = Sign_upSerializer(Sign_Ups, data=signUp_data['password'])
        if signUp_serializer.is_valid():
            signUp_serializer.save()
            return JsonResponse("password Updated Successfully", safe=False)
        return JsonResponse("Failed to Update password")
    elif request.method == 'DELETE':
        Sign_Ups = Sign_Up.objects.get(id=Sign_Up_Id)
        Sign_Ups.delete()
        return JsonResponse("Deleted Successfully", safe=False)







@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name.file)
    return JsonResponse(file_name, safe=False)
