from rest_framework import serializers
# import serializer as serializer
from homework1.models import Table, Column


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'title', 'content', 'create_date', 'actual_date', 'columns']


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'description', 'datatype']
