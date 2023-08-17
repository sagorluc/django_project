from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# PageNumberPagination
class ProductPaginaion(PageNumberPagination):
    page_size = 3  # (2 page create hobe) jodi 10 ta product thake tahole 2 page e 5 ta kore show korbe
    page_query_param = 'p' # (/?page=2) modify to (/?p=2)
    page_size_query_param = 'size' # user can set the product on a page as he/she wish
    max_page_size = 4 # our total page size is 4.
    

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2 # (/?limit=2&offset=3) 2 product in a page and product number after 3 like (4,5)
    limit_query_param = 'l' # (/?l=2&offset=3)
    offset_query_param = 's' # (/?l=2&s=3)
    max_limit = 4 
    
    
class ProductCursorPagination(CursorPagination):
      page_size = 2 
      ordering = 'price' # ordering/sorting by price. Must have to use ordering otherwise will not work
      cursor_query_param = 'data' # (?data=cD00MjAuOTk%3D)