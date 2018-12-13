from django.db import models
from django.db.models import (
    Model,
    AutoField,
    CharField,
    IntegerField,
    TextField,
    DateTimeField,
    Index,
    BigIntegerField,
    BigAutoField
)
import logging

logger = logging.getLogger(__name__)



class FileUpload(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, null=True)
    datafile = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mimetype = CharField(max_length=50, null=True)

    @staticmethod
    def by_name(name):
        try:
            return FileUpload.objects.get(name=name)
        except Exception as identifier:
            logger.info("exception %s" % identifier)
        return None