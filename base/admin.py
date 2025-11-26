from django.contrib import admin
from .models import Messages

class messagefilter(admin.SimpleListFilter):
    title = 'message_status'
    parameter_name = "message_status"
    
    def lookups(self, request, model_admin):
        return [('r','Read'),('u','Unread')]
    
    def queryset(self, request, queryset):
        if self.value == 'r':
            return queryset.filter(message_status='r')
        
        elif self.value == 'u':
            return queryset.filter(message_status = 'u')

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username','email','created_at']
    list_filter = [messagefilter]
# Register your models



