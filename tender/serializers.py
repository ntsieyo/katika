from rest_framework import serializers

from tender.models import CDI_CRI, ArmpEntry, Entreprise, TenderOwner


class TenderOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderOwner
        exclude = TenderOwner.SERIALIZER_EXCLUDE_FIELDS
        


class TenderSerializer(serializers.ModelSerializer):

    #type = IncidentTypeSerializer()
    #tags = serializers.StringRelatedField(many=True)
    #tags = TagSerializer(many=True)
    #content = serializers.CharField(max_length=1000) couldn't figure out Textfield->Charfield
    owner = TenderOwnerSerializer()

    class Meta:

        model = ArmpEntry
        fields = ArmpEntry.SERIALIZER_FIELDS
        
        

class CDI_CRI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CDI_CRI
        exclude = CDI_CRI.SERIALIZER_EXCLUDE_FIELDS
        

class EntrepriseSerializer(serializers.ModelSerializer):

    #owner = TenderOwnerSerializer()
    cdi_cri = CDI_CRI_Serializer()

    class Meta:
        model = Entreprise
        fields = Entreprise.SERIALIZER_FIELDS