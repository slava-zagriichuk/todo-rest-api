from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the item.
        return obj.user == request.user

