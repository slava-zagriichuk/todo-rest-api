from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer, RegisterSerializer, ChangePasswordSerializer
from .permissions import IsOwner


class ItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self, *args, **kwargs):

        # filtering against queryset by status
        stat = self.request.query_params.get('status')
        if stat is not None:
            return Item.objects.all().filter(user=self.request.user, status=stat)

        # default filtering by item's owner
        return Item.objects.all().filter(user=self.request.user)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsOwner,)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsOwner,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "new_password": "Password updated successfully"
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

