from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, APIView
from .serializers import BookSerializer, RegisterSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Пользователь создан'}, status=201)
        return Response(serializer.errors, status=400)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name', 'author', 'genre', 'age']
    search_fields = ['name', 'author', 'genre']
    ordering_fields = ['name', 'author', 'genre', 'age']
    ordering = ['name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    



