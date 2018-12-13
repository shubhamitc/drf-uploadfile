from django.shortcuts import render
from rest_framework import (
    status,
    generics
)
from rest_framework.response import Response
from uploadfile.constants import (
    NAME
)
import json
from django.http import HttpResponse
import mimetypes
import os

# Create your views here.

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from uploadfile.models import FileUpload
from uploadfile.serializers import FileUploadSerializer
# from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper


class FileUploadViewSet(ModelViewSet):
    
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(datafile=self.request.data.get('datafile'))
    
    def get(self, request, name, format=None):
        # serializer = FileUploadSerializer(data=request.data)
        print("pk is {}".format(name))
        upload = FileUpload.by_name(name)
        print("UPLOAD {}".format(upload.mimetype) )
    
        file1 = upload.datafile
        print(dir(file1.size))
        response = HttpResponse(FileWrapper(file1), content_type=upload.mimetype)
        response['Content-Disposition'] = 'attachment; filename="%s"' % upload.datafile.name
        response['Content-Length'] = os.path.getsize(os.path.join('./media/',file1.name))
        return response
        # return HttpResponse(upload.datafile)
    
    
    def post(self, request, format=None):
        print("request %s" % request)
        print("request %s" % request.data)
        
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            if FileUpload.by_name(serializer.validated_data[NAME]) is None:
                upload = serializer.save()
                print(upload.datafile.name)
                mimetype = mimetypes.MimeTypes().guess_type(upload.datafile.name)[0]
                print("Mimetype {}".format(mimetype) )
                upload.mimetype = mimetype
                upload.save()
            else:
                return HttpResponse("File with this name already exists")
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, name, format=None):
        upload = FileUpload.by_name(name)
        upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)