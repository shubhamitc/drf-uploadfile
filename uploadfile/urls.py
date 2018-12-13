from django.urls import path
from django.conf.urls import url
from uploadfile.views import FileUploadViewSet

urlpatterns = [
    url(r'^api/v1/$', FileUploadViewSet.as_view({'get': 'list'})),
    url(r'api/v1/(?P<name>\w+)/$', FileUploadViewSet.as_view({'get': 'get', 'delete': 'delete'})),
]