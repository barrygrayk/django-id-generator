from  validator.models import Person
from rest_framework import serializers

class CreateIDSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Person
        fields = ('__all__')