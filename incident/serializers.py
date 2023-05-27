from rest_framework import serializers

from incident.models import Incident, IncidentType, Tag



class IncidentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncidentType
        fields = IncidentType.FORM_FIELDS


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = Tag.FORM_FIELDS


class IncidentSerializer(serializers.ModelSerializer):

    type = IncidentTypeSerializer()
    #tags = serializers.StringRelatedField(many=True)
    tags = TagSerializer(many=True)

    class Meta:

        model = Incident
        fields = Incident.FORM_FIELDS