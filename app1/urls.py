from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.login_p,name='login_p'),
    path('signup',views.signup,name='signup'),
    # path('login_form',views.login_form,name='login_form'),
    # path('signup_form',views.signup_form,name='signup_form'),
    path('logout_p',views.logout_p,name='logout_p'),
    path('admin_panel',views.admin_panel,name='admin_panel'),
    path('add_user',views.add_user,name='add_user'),
    path('upload/',views.upload,name='upload'),
    # path('adduser_form',views.adduser_form,name='adduser_form'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('update_user/<int:id>',views.update_user,name='update_user'),
    # path('update_user_form/<int:id>',views.update_user_form,name='update_user_form'),
    path('search_data',views.search_data,name='search_data'),
    path('
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         home',views.home,name='home'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)