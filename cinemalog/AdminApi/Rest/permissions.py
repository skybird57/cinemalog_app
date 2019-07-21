from rest_framework import permissions


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

    def has_permission(self, request, view):
            
        return super().has_permission(request, view)


#check auth/auth in apis
def check_permissions(user,permit):
    if user.is_authenticated:
        if permit in user.get_all_permissions():
            return True
    return False

class check_perm():
    def __init__(self, user, permit):
        self.user=user
        self.permit=permit

    def check_permissions(self):
        if self.user.is_authenticated:
            if permit in user.get_all_permissions():
                return True
        return False   