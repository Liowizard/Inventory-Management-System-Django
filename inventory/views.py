from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer

from .models import Item
from .serializers import ItemSerializer


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        cache_key = f"item_{item_id}"

        item = cache.get(cache_key)
        if not item:
            item = get_object_or_404(Item, pk=item_id)
            cache.set(cache_key, item)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        cache_key = f"item_{item.id}"
        cache.set(cache_key, serializer.data)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        self.perform_destroy(item)

        cache_key = f"item_{item.id}"
        cache.delete(cache_key)

        return Response(
            {"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """Handle user registration."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Will raise 400 error if validation fails
        serializer.save()  # This calls the `create` method from the serializer
        return Response({"status": "User created"}, status=status.HTTP_201_CREATED)
