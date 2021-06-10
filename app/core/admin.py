from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # import the default Django user admin
from django.utils.translation import gettext as _  # converting string in python to human readable text
    # make it easier to do translations

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # adding sections
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields':('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # add a string classes now these are just the classes that are assigned to the form and
                                    #I just took the defaults
                                    #from the user admin documentation
            'fields': ('email', 'password1', 'password2')
        }),  # no title: None, open a dictionary here
    )

admin.site.register(models.User, UserAdmin)
# Register your models here.
