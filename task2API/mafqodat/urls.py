from django.conf.urls import url
from django.urls import include

from .views import Sign_UpApi,Autherized_postApi,ChatApi,PostApi,Access_admin_for_usersApi,LoginApi,SaveFile,Type_itemApi
from .views import Sign_UpAPI,Autherized_postAPI,ChatAPI,PostAPI,Access_admin_for_usersAPI,LoginAPI,Type_itemAPI,sign_upapi

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    url(r'^admins',admin.site.urls),
    url(r'^api/jwt/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/jwt/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^docs',include_docs_urls(title='Todo Api')),
    url(r'^api/token', obtain_auth_token, name="auth_token"),



    url(r'^users$', Sign_UpApi),
    url(r'^users/([0-9]+)$', Sign_UpApi),

    url(r'^Autherized_posts$', Autherized_postApi),
    url(r'^Autherized_posts/([0-9]+)$', Autherized_postApi),

    url(r'^Chats$', ChatApi),
    url(r'^Chats/([0-9]+)$', ChatApi),

    url(r'^Posts$', PostApi),
    url(r'^Posts/([0-9]+)$', PostApi),

    url(r'^Type_items$', Type_itemApi),
    url(r'^Type_items/([0-9]+)$', Type_itemApi),

    url(r'^Access_admin_for_users$', Access_admin_for_usersApi),
    url(r'^Access_admin_for_users/([0-9]+)$', Access_admin_for_usersApi),

    url(r'^Logins$', LoginApi),
    url(r'^Logins/([0-9]+)$', LoginApi),


    url(r'^user/([0-9]+)$', Sign_UpAPI),


    url(r'^user/([0-9]+)/$', sign_upapi),


    url(r'^Autherized_post/([0-9]+)$', Autherized_postAPI),


    url(r'^Chat/([0-9]+)$', ChatAPI),


    url(r'^Post/([0-9]+)$', PostAPI),


    url(r'^Type_item/([0-9]+)$', Type_itemAPI),


    url(r'^Access_admin_for_user/([0-9]+)$', Access_admin_for_usersAPI),


    url(r'^Login/([0-9]+)$', LoginAPI),




    url(r'^SaveFile',SaveFile)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
