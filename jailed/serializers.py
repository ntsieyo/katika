from rest_framework import serializers

from jailed.models import Incarceration, IncarcerationTag, Prison


class IncarcerationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncarcerationTag
        fields = IncarcerationTag.FORM_FIELDS


class PrisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prison
        fields = Prison.FORM_FIELDS


class IncarcerationSerializer(serializers.ModelSerializer):

    tags = IncarcerationTagSerializer(many=True)
    prison = PrisonSerializer()

    class Meta:

        model = Incarceration
        fields = Incarceration.FORM_FIELDS