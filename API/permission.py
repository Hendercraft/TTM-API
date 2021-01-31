from django.contrib.auth.models import Group
from rest_framework import permissions



"""
    Functions used in permissions
"""

def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    """
    Check if the user is in one (or several) of required_groups
    """
    return any([_is_in_group(user, group_name) for group_name in required_groups])


"""
    Permissions
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owner of an object to edit it.
    If the user is not the owner it can only use "Safe methods like get".
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user

class IsUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow user to edit it's own profile.
    If the user is not the owner it can only use "Safe methods like get".
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.id == request.user.id

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
    # Permission check if the user is a researcher
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
    # Permission check if the user is a public user
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