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
from rest_framework.permissions import IsAuthenticated # new import

from .models import Todo
from .serializer import TodoSerializer


# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,) #permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    permission_classes = (IsAuthenticated,)#permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    permission_classes = (IsAuthenticated,)#permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    permission_classes = (IsAuthenticated,)#permission classes
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@csrf_exempt
def Sign_UpApi(request):
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


@csrf_exempt
def Autherized_postApi(request):
    if request.method == 'GET':
        autherizedPost = Autherized_post.objects.all()
        Autherized_post_serializer = Autherized_postSerializer(autherizedPost, many=True)
        return JsonResponse(Autherized_post_serializer.data, safe=False)
    elif request.method == 'POST':
        signUp_data = JSONParser().parse(request)
        Autherized_post_serializer = Autherized_postSerializer(data=signUp_data)
        if Autherized_post_serializer.is_valid():
            Autherized_post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def ChatApi(request):
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


@csrf_exempt
def PostApi(request):
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


@csrf_exempt
def Type_itemApi(request):
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


@csrf_exempt
def Access_admin_for_usersApi(request):
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


@csrf_exempt
def LoginApi(request):
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


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name.file)
    return JsonResponse(file_name, safe=False)
