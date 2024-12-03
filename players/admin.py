from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Player, RankingLog


# @admin.register(Player)
# class PlayerAdmin(admin.ModelAdmin):
#     pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Player Info",
            {
                "fields": (
                    "uuid",
                    "username",
                    "password",
                    "email",
                    "tier",
                    "main_agent",
                    "last_login",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
                "description": "Permissions can be changed in the User Permissions section.",
            },
        ),
    )

    list_display = [
        "username",
        "tier",
        "main_agent",
        "email",
    ]

    readonly_fields = [
        "last_login",
        "uuid",
    ]

    list_select_related = [
        "tier",
        "main_agent",
    ]

    list_prefetch_related = [
        "stats",
    ]

    list_filter = [
        "tier__division",
    ]

    search_fields = [
        "username",
        "first_name",
        "email",
    ]

    list_per_page = 10

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user_permissions":
            kwargs["queryset"] = Permission.objects.all().select_related("content_type")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # If the password is changed, update it
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)


@admin.register(RankingLog)
class RankingLogAdmin(admin.ModelAdmin):

    readonly_fields = [
        "last_position",
        "last_position_change",
    ]

    list_display = [
        "player",
        "last_position",
        "last_position_change",
        "updated_at",
    ]

    search_fields = [
        "player__username",
    ]

    list_per_page = 10
