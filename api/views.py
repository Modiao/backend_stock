from rest_framework import status
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser


from .models import Ticket, Patient
from api.serializers import (RegisterUserSerializer, ListUserSerializer, \
        TicketSerializer, PatientSerializer)
from backend_stock.utilities import get_price
# Create your views here.
class get_token(ObtainAuthToken):
    "This will generate the token"
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)

@api_view(['POST'])
def logout(request):
    logout(request)
    data = {'success': 'Sucessfully logged out'}
    return Response(data=data, status=status.HTTP_200_OK)
        
@permission_classes((IsAuthenticated,))
class RegisteerUserView(generics.CreateAPIView):
    " This will be used for the login user "
    queryset = User.objects.all()
    permission_class = (AllowAny,)
    serializer_class = RegisterUserSerializer
@permission_classes((IsAuthenticated,))
class get_all_users(APIView):
    permission_class = (IsAuthenticated,)
    def get(self, request):
        users = User.objects.all()
        serializer = ListUserSerializer(users, many=True)
        return Response(serializer.data)
@permission_classes((IsAuthenticated,))
class RegisteerUserView(generics.CreateAPIView):
    " This will be used for the login user "
    queryset = User.objects.all()
    permission_class = (AllowAny,)
    serializer_class = RegisterUserSerializer

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def get_price_of_ticket(request):
    """
    this will help us to get the price for an specific type of ticket
    """
    data = JSONParser().parse(request) 
    if "type" not in data:
        return JsonResponse({'code': '400', 'error': 'type is missing'}, status=400)
    price = get_price.get(data["type"])
    if not price:
        return JsonResponse({"error": "No price is available for this ticket"}, status=200)
    return JsonResponse({"price": price}, status=200)
@permission_classes((IsAuthenticated,))
class PatientAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'
    serializer_class = PatientSerializer
    def get_queryset(self):
        qs = Patient.objects.all()
        id = self.request.GET.get("id")
        if id is not None:      
            qs = qs.filter(Q(id = id)).distinct()   
        return qs
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)

@permission_classes((IsAuthenticated,))
class PatientRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.all()

class TicketAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TicketSerializer
    def get_queryset(self):
        qs = Ticket.objects.all()
        id_ticket = self.request.GET.get("id_ticket")
        if id_ticket is not None:      
            qs = qs.filter(Q(id_ticket = id_ticket)).distinct()   
        return qs
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
@permission_classes((IsAuthenticated,))
class TicketRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id_ticket' 
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.all()

