from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class AuditRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ip = models.GenericIPAddressField()
    user_agent = models.TextField()
    url = models.URLField()
    data = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class AuditException(models.Model):
    request = models.ForeignKey(AuditRequest, on_delete=models.CASCADE)
    exception = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class AuditResponse(models.Model):
    request = models.ForeignKey(AuditRequest, on_delete=models.CASCADE)
    data = models.TextField()
    status_code = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
