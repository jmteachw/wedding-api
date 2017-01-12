from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import RSVP
from api.serializers import RSVPSerializer


@api_view(['GET', 'POST'])
def rsvp_list(request):
    """
    List all snippets, or create a new RSVP.
    """
    if request.method == 'GET':
        rsvps = RSVP.objects.all()
        serializer = RSVPSerializer(rsvps, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RSVPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def rsvp_detail(request, first_name, last_name):
    """
    Retrieve, update or delete a RSVP instance.
    """
    try:
        rsvp = RSVP.objects.get(first_name=first_name, last_name=last_name)
    except RSVP.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RSVPSerializer(rsvp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RSVPSerializer(rsvp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rsvp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
