from rest_framework import serializers
from uploadfile.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
    
    def validate_name(self, value):
        if value is None:
            raise serializers.ValidationError("Name should not be None")
        if value is not None and len(value)> 50:
            raise serializers.ValidationError("Name should not be more than 50 chars")
        return value