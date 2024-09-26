from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import Item
from .serializers import ItemSerializer, UserSerializer


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

        # Check cache
        item = cache.get(cache_key)
        if not item:
            # If not found in cache, fetch from DB
            item = get_object_or_404(Item, pk=item_id)
            cache.set(cache_key, item)

        serializer = ItemSerializer(item)
        return Response(serializer.data)


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.create_user(username=username, password=password)
        return Response({"status": "User created"}, status=status.HTTP_201_CREATED)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        cache_key = f"item_{item_id}"

        # Check cache
        item = cache.get(cache_key)
        if not item:
            # If not found in cache, fetch from DB
            item = get_object_or_404(Item, pk=item_id)
            cache.set(cache_key, item)

        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Handle the PUT request to update an item."""
        item = self.get_object()  # Retrieve the item from the database
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update the cache with the new item details
        cache_key = f"item_{item.id}"
        cache.set(cache_key, serializer.data)

        return Response(serializer.data)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        cache_key = f"item_{item_id}"

        # Check cache
        item = cache.get(cache_key)
        if not item:
            # If not found in cache, fetch from DB
            item = get_object_or_404(Item, pk=item_id)
            cache.set(cache_key, item)

        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Handle the DELETE request to delete an item."""
        item = self.get_object()  # Fetch the item
        self.perform_destroy(item)

        # Remove the deleted item from the cache
        cache_key = f"item_{item.id}"
        cache.delete(cache_key)

        return Response(
            {"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
