# customers/selectors.py

from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Customer

def get_customer(customer_id):
    """
        Get a single active customer by ID.
        Raises 404 if the customer does not exist or is soft deleted.
    """


    return get_object_or_404(
    Customer.objects.select_related("owner"),
    id=customer_id,
    is_deleted=False,
)


def get_active_customers():
    """
    Return all active (non-deleted) customers.
    """


    return (
    Customer.objects.select_related("owner")
    .filter(
        status="ACTIVE",
        is_deleted=False,
    )
    .order_by("company_name")
)

def search_customers(query=None, owner_id=None, city=None, status=None):
    """
    Search customers by multiple fields.


Filters:
- company name
- contact person
- email
- phone
- city
- owner
- status
"""

queryset = (
    Customer.objects.select_related("owner")
    .filter(is_deleted=False)
)

if query:
    queryset = queryset.filter(
        Q(company_name__icontains=query)
        | Q(contact_person__icontains=query)
        | Q(email__icontains=query)
        | Q(phone__icontains=query)
    )

if owner_id:
    queryset = queryset.filter(owner_id=owner_id)

if city:
    queryset = queryset.filter(city__iexact=city)

if status:
    queryset = queryset.filter(status=status)
#return queryset.order_by("company_name")
