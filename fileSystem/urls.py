from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'',views.FileSystemBase.as_view(), name='home'),
]
