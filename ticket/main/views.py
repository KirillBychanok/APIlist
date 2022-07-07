from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from .models import Comment, Tickets
from .serializers import CommentSerializer, TicketSerializer
from .tasks import send_spam_email


class GuestApiList(ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Tickets.objects.filter(is_active='a')


class AdminApiSet(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Tickets.objects.filter(is_active='a')


class AdminApiBack(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Tickets.objects.filter(is_active='o')


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request, pk):
    human = Tickets.objects.get(pk=pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_spam_email.delay(human.user.email)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comment = Comment.objects.filter(is_active=True, ticket=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)