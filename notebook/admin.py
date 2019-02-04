from django.contrib import admin
from .models import Contact, Account


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'city', 'followers',
            'updated_at')
    list_filter = ['updated_at']
    search_fields = ['name', 'company', 'city']


admin.site.register(Account)
admin.site.register(Contact, ContactAdmin)
