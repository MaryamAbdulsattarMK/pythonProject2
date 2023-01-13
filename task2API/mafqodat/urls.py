from django.conf.urls import url
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import TokenVerifyView

from .views import Sign_UpApi,Autherized_postApi,ChatApi,PostApi,Access_admin_for_usersApi,LoginApi,SaveFile,Type_itemApi
from .views import Sign_UpAPI,Autherized_postAPI,ChatAPI,PostAPI,Access_admin_for_usersAPI,LoginAPI,Type_itemAPI,sign_upapi

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    path("users",Sign_UpApi),
    path("users/([0-9]+)/",Sign_UpApi),
    path('admins',admin.site.urls),

    path('api/jwt/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token', obtain_auth_token, name="auth_token"),





    path('admins/jwt/user/([0-9]+)', Sign_UpAPI),


    path('admins/jwt/user/([0-9]+)/', sign_upapi),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
