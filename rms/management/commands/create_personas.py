"""
Creates the personas
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import models
from opal import models as omodels


class Command(BaseCommand):
    def create_user(self, username):
        username = username.lower()
        user, created = models.User.objects.get_or_create(username=username)

        if created:
            user.set_password("{}1".format(username))
            profile, _ = omodels.UserProfile.objects.get_or_create(user=user)
            profile.force_password_change = False
            profile.save()
        user.first_name = username.title()
        user.save()
        return user

    def add_permission(self, user, permission_str):
        permission = models.Permission.objects.get(codename=permission_str)
        user.user_permissions.add(permission)

    def handle(self, *args, **options):
        linda = self.create_user("Linda")
        self.add_permission(linda, "can_refer")

        mary = self.create_user("Mary")
        self.add_permission(mary, "can_assign_location")

        mary = self.create_user("Mary")
        self.add_permission(mary, "can_assign_location")

        matt = self.create_user("Matt")
        self.add_permission(matt, "can_confirm_location")
