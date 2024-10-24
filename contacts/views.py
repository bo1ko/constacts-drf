from rest_framework import viewsets

from contacts.models import Contact
from contacts.permission import GeoPermission
from contacts.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contacts.
    """

    permission_classes = [GeoPermission]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer