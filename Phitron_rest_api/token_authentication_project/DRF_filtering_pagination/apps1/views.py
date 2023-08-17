
                # this is for product and product reviews 
                # ===========================================    
                
from rest_framework import viewsets
from apps1.permisions import AdminOrReadOnly, ReviewerOrReadOnly
from apps1.models import Product, ProductReview
from apps1.serializers import ProductSerializer, ProductReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps1.paginations import ProductPaginaion, ProductLimitOffsetPagination, ProductCursorPagination
   
# Create your views here.
# product list
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly] # custom permission
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # convert to json format
    
    # customize searching filter
    # we have to off all the filtering while we useing CursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']  # (/?search=television) searching product by procuct_name and product_description

    # ordering/sorting assending/dessending on price 
    # we have to off all the filtering while we useing CursorPagination
    filter_backends = [filters.OrderingFilter] # overriding
    ordering_fields = ['price'] # (assending- /?ordering=price) and (dessending- /?ordering=-price)
    
    # 3 types of paginations
    pagination_class = ProductPaginaion # PageNumberPagination
    # pagination_class = ProductLimitOffsetPagination # LimitOffSetPagination
    # pagination_class = ProductCursorPagination # CursorPagination

# product reviews list   
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewerOrReadOnly] # custom permission
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer # convert to json format
    
    # customize filtering reviw by username 
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']  # (?username=jakir) by username
    filterset_fields = ['rating', 'product'] # (/?rating=5&product=4) by rating and multiple product
    
    # build-in filtering reviw by username (?username=jakir)
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains = username) # iconains is not case sencetive
    #     return queryset


                        # registration class
                        # =====================
                        
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps1.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from . import singnals

# Create your views here.                       
class RegistrationView(APIView):
    def post(self, request):
        serial = RegistrationSerializer(data= request.data)
        data = {} 
        if serial.is_valid():
            account = serial.save()
            data['response'] = 'Registration Successfull !!'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user = account).key # generate token
            data['token'] = token
            Response(serial.data, status= status.HTTP_201_CREATED)
        else:
            data = serial.errors
        return Response(data)
    
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)
    
    

