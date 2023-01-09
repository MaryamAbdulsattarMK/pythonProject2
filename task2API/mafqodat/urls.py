from django.conf.urls import url
from django.urls import include

from .views import Sign_UpApi,Autherized_postApi,ChatApi,PostApi,Access_admin_for_usersApi,LoginApi,SaveFile,Type_itemApi

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    url(r'^admin$',admin.site.urls),
    url(r'^api/jwt/token/$',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/jwt/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^docs$',include_docs_urls(title='Todo Api')),
    url(r'^api/token$', obtain_auth_token, name="auth_token"),



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
