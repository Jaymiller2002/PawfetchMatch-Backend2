from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
# Get Profile View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

# Create New User View
@api_view(['POST'])
@permission_classes([])
def create_user(request):
    # print('CREATE USER ', request.data)
    username = request.data['username']
    user = User.objects.create(
        username = username
    )
    user.set_password(request.data['password'])
    user.save()
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    profile = Profile.objects.create(
        user = user,
        first_name = first_name,
        last_name = last_name
    )
    user_serialized = UserSerializer(user)
    return Response(user_serialized.data)

# Listing Views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_listing(request):
    print('CREATE LISTING: ', request.data)
    user = request.user
    form_data = {
        'title': request.data['title'],
        'user': user.pk,
        'description': request.data['description'],
        'price': request.data['price'],
        'quantity': request.data['quantity'],
        'image': request.data['image']
    }
    serializer = ListingSerializer(data=form_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_listing(request):
    print("GETTING LISTINGS: ", request.data)
    user = request.user
    listings = Listing.objects.filter(user=user)
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)

# Add a Delete option for listings

#
##
#

# Message View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
    form_data = {
        'sender': request.user.pk,
        'receiver': request.data.get('receiver'),
        'content': request.data.get('content'),
        'image': request.data.get('image'),
    }

    # Create a new message
    serializer = MessageSerializer(data=form_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request):
    # Retrieve messages for the authenticated user
    messages = Message.objects.filter(receiver=request.user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


#
##
#

# Cart View
