from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class StandardPagination(PageNumberPagination):
    page_size = 50
    page__size_query_param = 'page_size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.next_page_number()-1),
            ('total', int(self.page.paginator.count/self.page_size)),
            ('records', self.page.paginator.count),
            ('rows', data)
        ]))