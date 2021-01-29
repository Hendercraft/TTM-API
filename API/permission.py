from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])

# def _is_user(user, model_id):
#     try:
#         return model_id.object.get().user_set.filter(id=user.id).exist()
#     except model_id.DoesNotExist:
#         return None

# def _is_user_profile(user, model_id):
#     try:
#         return User.objects.get().user_set.filter(id=user.id).exist()
#     except User.DoesNotExist:
#         return None

# def _has_object_permission(user, required_model_id):
#     return any([_is_user(user,model_id) for model_id in required_model_id])
"""
class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'anonymous']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user

class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_permission(self, request, view):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)

        return request.user and has_group_permission

class IsAnonymousUser(permissions.BasePermission):
    # Permission check if the user is Anonymous
    required_groups = ['anonymous']

    def has_permission(self, request, view):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        
        return request.user and has_group_permission

class IsResearcherUser(permissions.BasePermission):
    # Permission check if the user is researcher
    required_groups = ['researcher']

    def has_permission(self, request, view):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        
        return request.user and has_group_permission

class IsPublicUser(permissions.BasePermission):
    # Permission check if the user is public
    required_groups = ['publicUser']

    def has_permission(self, request, view):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        
        return request.user and has_group_permission