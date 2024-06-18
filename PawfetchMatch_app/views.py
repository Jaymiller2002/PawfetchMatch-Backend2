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


# Get All Profile's of Every User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_profiles(request):
    print('Getting all profiles: ', request.data)
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
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
    bio = request.data['bio']
    image = request.data['image']
    profile = Profile.objects.create(
        user = user,
        first_name = first_name,
        last_name = last_name,
        bio = bio,
        image = image
    )
    user_serialized = UserSerializer(user)
    return Response(user_serialized.data)

# Update User View
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user  # Get the currently authenticated user
    pk = user.id  # Get the ID of the authenticated user

    try:
        user_instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=404)
    
    # Update profile fields
    profile = Profile.objects.get(user=user_instance)
    print('PROFILE INFORMATION >>>>>>>>>', profile.first_name)
    profile.first_name = request.data.get('first_name', profile.first_name)
    profile.last_name = request.data.get('last_name', profile.last_name)
    profile.bio = request.data.get('bio', profile.bio)
    profile.image = request.data.get('image', profile.image)
    profile.save()
    
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

# Delete User View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    pk = user.id

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=404)
    
    # Check if the authenticated user is the same as the user being deleted
    if request.user != user:
        return Response({"error": "You are not allowed to delete this user"}, status=403)
    
    user.delete()
    return Response({"message": "User deleted successfully"}, status=204)

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

# Update Listing View
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_listing(request):
    print('UPDATE LISTING: ', request.data)
    user = request.user

    try:
        user_instance = User.objects.get(id=user.id)
    except User.DoesNotExist:
        return Response({"error": "Listing not found"}, status=404)

    # Update the listing attributes based on the request data, while preserving existing values if not provided in the request
    listing = Listing.objects.filter(user=user_instance).first()
    listing.title = request.data.get('title', listing.title)
    listing.description = request.data.get('description', listing.description)
    listing.price = request.data.get('price', listing.price)
    listing.quantity = request.data.get('quantity', listing.quantity)
    listing.image = request.data.get('image', listing.image)
    listing.save()

    listing_serialized = ListingSerializer(listing)
    return Response(listing_serialized.data)

# Delete Listing View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_listing(request):
    print('DELETE LISTING: ', request.data)
    user = request.user

    try:
        listing = Listing.objects.filter(user=user.id)
    except Listing.DoesNotExist:
        return Response({"error": "Listing not found"}, status=404)

    listing.delete()
    return Response({"success": "Listing deleted successfully"})

# Get Listing View
@api_view(['GET'])
@permission_classes([])
def get_listing(request):
    print("GETTING LISTINGS: ", request.data)
    # user = request.user
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)


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

# Update Message View- SORTA WORKS BUT CHANGES ALL MESSAGES
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_message(request):
    user = request.user
    
    try:
        messages = Message.objects.filter(sender_id=user.id)
    except User.DoesNotExist:
        return Response({"error": "Listing not found"}, status=404)

    updated_messages = []
    for message in messages:
        message.content = request.data.get('content', message.content)
        message.image = request.data.get('image', message.image)
        message.save()
        updated_messages.append(message)

    message_serialized = MessageSerializer(updated_messages, many=True)
    return Response(message_serialized.data)


# Delete Message View
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request):
    print('DELETE MESSAGE: ', request.data)
    user = request.user

    try:
        message = Message.objects.filter(sender_id=user.id)
    except Message.DoesNotExist:
        return Response({"error": "Listing not found"}, status=404)

    message.delete()
    return Response({"success": "Listing deleted successfully"})

# Get Message View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request):
    # Retrieve both sent and received messages for the authenticated user
    received_messages = Message.objects.filter(receiver=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    
    # Combine both querysets
    messages = list(received_messages) + list(sent_messages)

    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


#
##
#

# Logout View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    # Delete the token associated with the user
    return Response({"message": "Logged out successfully"})
