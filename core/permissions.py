from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == 'GET':
            return True

        return request.user.is_authenticated
