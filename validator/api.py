from .models import Person
from .serializers import CreateIDSerializer
from rest_framework import  viewsets


class IdViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = CreateIDSerializer


