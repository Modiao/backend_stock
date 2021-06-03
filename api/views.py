from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser



from .models import Ticket, Patient
from api.serializers import (RegisterUserSerializer, ListUserSerializer, \
        TicketSerializer, UpdateTicketSerializer)
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


class RegisteerUserView(generics.CreateAPIView):
    " This will be used for the login user "
    queryset = User.objects.all()
    permission_class = (AllowAny,)
    serializer_class = RegisterUserSerializer

class get_all_users(APIView):
    permission_class = (IsAuthenticated,)
    def get(self, request):
        users = User.objects.all()
        serializer = ListUserSerializer(users, many=True)
        return Response(serializer.data)

class RegisteerUserView(generics.CreateAPIView):
    " This will be used for the login user "
    queryset = User.objects.all()
    permission_class = (AllowAny,)
    serializer_class = RegisterUserSerializer

class TicketList(APIView):
    """
    List all Ticket, or create a new Ticket
    """
    def get(self, request, format=None):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
class TicketDetail(APIView):
    """
    Retrieve, update or delete a ticket instance.
    """
    def get(self, request, pk, format=None):
        comment = get_object_or_404(Ticket, id_ticket=pk)
        serializer = TicketSerializer(comment)
        return Response(serializer.data)
    
class UpdateTicketStatus(APIView):
    """
    This will help us to update the status of un specific ticket
    """
    serializer_class = UpdateTicketSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id_ticket = request.data["id_ticket"]
            ticket = Ticket.objects.filter(
                id_ticket = id_ticket
            )
            if not ticket:
                return Response({'code': '400', 'error': 'No ticket match with this id'}, status=status.HTTP_400_BAD_REQUEST)
            ticket = ticket[0]
            ticket.is_valid = False
            ticket.save()
            serialize = TicketSerializer(ticket)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
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
    
    