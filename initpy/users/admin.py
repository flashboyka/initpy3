from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from initpy.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(AdminImageMixin, auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["username", "is_superuser", "birth_day"]
    search_fields = ["name"]
    fieldsets = auth_admin.UserAdmin.fieldsets+(
        (_("Advanced options"), {
            "classes": ('collapse'),
            "fields": ("birth_day", "photo",)
        }),
    )
