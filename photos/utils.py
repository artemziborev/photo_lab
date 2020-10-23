
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Photo


class PaginationPhotos(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PhotoFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags', lookup_expr='in')
    event =CharFilterInFilter(field_name='tags', lookup_expr='in')

    class Meta:
        model = Photo
        fields = ['event', 'tags']