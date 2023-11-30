from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return request.user.is_authenticated
        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) == 'admin'
