from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Customer
from .serializers import (
    CustomerSerializer,
    CustomerCreateSerializer,
    CustomerUpdateSerializer,
)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customer CRUD APIs
    """

    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.filter(is_deleted=False)

    def get_serializer_class(self):

        if self.action == "create":
            return CustomerCreateSerializer

        if self.action in ["update", "partial_update"]:
            return CustomerUpdateSerializer

        return CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        """
        Soft Delete Customer
        """

        customer = self.get_object()

        customer.is_deleted = True
        customer.save(update_fields=["is_deleted"])

        return Response(
            {
                "success": True,
                "message": "Customer deleted successfully."
            },
            status=status.HTTP_200_OK
        )