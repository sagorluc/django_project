# makeing our custom permision

from rest_framework import permissions

# if the perosn is admin.Otherwise read only
class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # check if the get request means read only
            return  True
        else:
            return bool(request.user and request.user.is_staff) # post, put, delete
            
# if the person is reviewers.Otherwise read only
class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # check if the get request means read only
            return  True
        else:
            return obj.user == request.user # post, put, delete (user form model user)
    
    