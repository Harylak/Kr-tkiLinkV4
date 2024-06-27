from django.contrib import admin
from django.urls import path, re_path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    re_path(r'^(?P<short_url>\w{6})$', views.redirect_url, name='redirect_url'),
    # path('logs/', views.log_view, name='log_view'),  # Remove this line
]
