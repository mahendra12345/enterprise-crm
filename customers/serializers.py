from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer used for GET (List/Retrieve)
    """

    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer

        fields = (
            "id",
            "customer_code",
            "company_name",
            "contact_person",
            "email",
            "phone",
            "website",
            "industry",
            "city",
            "state",
            "country",
            "postal_code",
            "address",
            "owner",
            "owner_name",
            "status",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "customer_code",
            "created_at",
            "updated_at",
        )

    def get_owner_name(self, obj):
        return obj.owner.full_name


from rest_framework import serializers
from .models import Customer


class CustomerCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fields = (
            "company_name",
            "contact_person",
            "email",
            "phone",
            "website",
            "industry",
            "city",
            "state",
            "country",
            "postal_code",
            "address",
            "owner",
            "status",
        )

    def validate_email(self, value):

        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Customer email already exists."
            )

        return value

    def validate_phone(self, value):

        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number is invalid."
            )

        return value

    def create(self, validated_data):

        last_customer = Customer.objects.order_by("-id").first()

        if last_customer:
            number = int(last_customer.customer_code[3:]) + 1
        else:
            number = 1

        validated_data["customer_code"] = f"CUS{number:06d}"

        return Customer.objects.create(**validated_data)

from rest_framework import serializers
from .models import Customer


class CustomerUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fields = (
            "company_name",
            "contact_person",
            "email",
            "phone",
            "website",
            "industry",
            "city",
            "state",
            "country",
            "postal_code",
            "address",
            "owner",
            "status",
        )

    def validate_email(self, value):

        customer = self.instance

        if Customer.objects.exclude(
            pk=customer.pk
        ).filter(
            email=value
        ).exists():

            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate_phone(self, value):

        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number is invalid."
            )

        return value





    
        