from rest_framework.pagination import CursorPagination

class MypaginationClass(CursorPagination):
    page_size = 1
    ordering = 'roll' 