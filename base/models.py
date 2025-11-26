from django.db import models
from django.core.validators import MinLengthValidator
class Messages(models.Model):
    message_read = "r"
    message_unread = "u"
    message_variables  = [(message_read, "Read"),(message_unread,"Unread")]
    
    username = models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_status = models.CharField(max_length=10,choices=message_variables, default=message_unread)
    class Meta:
        ordering = ['username']
