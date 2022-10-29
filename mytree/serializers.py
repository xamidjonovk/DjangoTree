from abc import ABC

from rest_framework.serializers import ModelSerializer, Serializer, CharField, SerializerMethodField
from .models import Subdivision, Employee


class EmployeeSerializer(ModelSerializer):
    text = SerializerMethodField('get_text')

    def get_text(self, obj):
        if obj:
            id = obj[0].subdivision_id
            return f"""<a href="employees/{id}">employees</a>"""

    class Meta:
        model = Employee
        fields = ('text',)


class RecursiveSerializer(Serializer):

    def to_representation(self, value):

        serializer = self.parent.parent.__class__(value, context=self.context)
        if len(serializer.data['nodes']) == 0:
            queryset = Employee.filter(subdivision_id=serializer.data['id'])
            if queryset:
                serializer = EmployeeSerializer(queryset)
        return serializer.data


class SubdivisionModelSerializer(ModelSerializer):
    nodes = RecursiveSerializer(many=True, read_only=True)
    text = CharField(source='title')

    class Meta:
        model = Subdivision
        fields = ['text', 'nodes', 'id']
