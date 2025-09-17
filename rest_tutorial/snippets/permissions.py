from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Cho phép người tạo (owner) chỉnh sửa/xóa, người khác chỉ đọc.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        # Nếu không phải phương thức safe, kiểm tra xem user là owner không
        return obj.owner == request.user
