from django.urls import path
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    
    path('signin',views.signin,name='signup'),
    path('',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)