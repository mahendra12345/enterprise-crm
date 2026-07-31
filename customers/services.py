# customers/services.py

from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Customer

class CustomerService:
 """
  Service layer for customer business logic.
 """

@staticmethod
@transaction.atomic
def create_customer(validated_data):
        """
        Create a new customer with an auto-generated customer code.
        """

        email = validated_data.get("email")

        if Customer.objects.filter(email=email, is_deleted=False).exists():
            raise ValidationError("Customer with this email already exists.")

        last_customer = Customer.objects.order_by("-id").first()

        if last_customer and last_customer.customer_code:
            number = int(last_customer.customer_code[3:]) + 1
        else:
            number = 1

        customer_code = f"CUS{number:06d}"

        customer = Customer.objects.create(
            customer_code=customer_code,
            **validated_data
        )

        return customer

@staticmethod
@transaction.atomic
def update_customer(customer, validated_data):
        """
        Update customer details.
        """

        email = validated_data.get("email")

        if email:
            exists = Customer.objects.exclude(pk=customer.pk).filter(
                email=email,
                is_deleted=False,
            ).exists()

            if exists:
                raise ValidationError("Customer with this email already exists.")

        for field, value in validated_data.items():
            setattr(customer, field, value)

        customer.save()

        return customer

@staticmethod
@transaction.atomic
def delete_customer(customer):
        """
        Soft delete a customer.
        """

        customer.is_deleted = True
        customer.save(update_fields=["is_deleted", "updated_at"])

        return customer
