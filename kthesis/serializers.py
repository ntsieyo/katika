from rest_framework import serializers

from kthesis.models import Degree, Scholar, Thesis, University


class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholar
        exclude = Scholar.SERIALIZER_EXCLUDE_FIELDS
    


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'
        
        

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = University.SERIALIZER_FIELDS


class ThesisSerializer(serializers.ModelSerializer):
    author = ScholarSerializer(read_only=True)
    degree = DegreeSerializer(read_only=True)
    supervisors = ScholarSerializer(many=True, read_only=True)
    committee = ScholarSerializer(many=True, read_only=True)
    university = UniversitySerializer(read_only=True)

    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail'
    # )

    class Meta:
        model = Thesis
        #fields = '__all__'
        exclude = Thesis.SERIALIZER_EXCLUDE_FIELDS