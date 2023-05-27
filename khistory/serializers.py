from rest_framework import serializers

from khistory.models import Event, Personnage



class PersonnageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnage
        fields = Personnage.FORM_FIELDS
        


class EventSerializer(serializers.ModelSerializer):

    personnages = PersonnageSerializer(many=True, read_only=True)

    # def to_representation(self, instance):
    #     """Convert `username` to lowercase."""
    #     ret = super().to_representation(instance)
    #
    #     if ret['featured_image']:
    #         print("featured_image: {}".format(ret))
    #         ret['image_url'] = ret['featured_image']
    #     return ret

    class Meta:
        model = Event
        fields = Event.FORM_FIELDS