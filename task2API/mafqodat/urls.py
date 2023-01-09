from django.conf.urls import url
from .views import Sign_UpApi,Autherized_postApi,ChatApi,PostApi,Access_admin_for_usersApi,LoginApi,SaveFile,Type_itemApi

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^SignUp$', Sign_UpApi),
    url(r'^SignUp/([0-9]+)$', Sign_UpApi),

    url(r'^Autherized_post$', Autherized_postApi),
    url(r'^Autherized_post/([0-9]+)$', Autherized_postApi),

    url(r'^Chat$', ChatApi),
    url(r'^Chat/([0-9]+)$', ChatApi),

    url(r'^Post$', PostApi),
    url(r'^Post/([0-9]+)$', PostApi),

    url(r'^Type_item$', Type_itemApi),
    url(r'^Type_item/([0-9]+)$', Type_itemApi),

    url(r'^Access_admin_for_users$', Access_admin_for_usersApi),
    url(r'^Access_admin_for_users/([0-9]+)$', Access_admin_for_usersApi),

    url(r'^Login$', LoginApi),
    url(r'^Login/([0-9]+)$', LoginApi),


    url(r'^SaveFile',SaveFile)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
