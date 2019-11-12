from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from homework1.models import Table, Column
from homework1.serializers import TableSerializer, ColumnSerializer

@api_view(['GET', 'POST'])
def table_list(request):
    """
    List all tables, or create new table.
    """
    if request.method == 'GET':
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def table_detail(request, pk):
    """
    Retrieve, update or delete a table.
    """
    try:
        table = Table.objects.get(pk=pk)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableSerializer(table)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def column_list(request):
    """
    List all column, or create new column.
    """
    if request.method == 'GET':
        columns = Column.objects.all()
        serializer = ColumnSerializer(columns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'UPDATE'])
def column_detail(request, pk):
    """
    Retrieve, update or delete a column.
    """
    try:
        column = Column.objects.get(pk=pk)
    except Column.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ColumnSerializer(column)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ColumnSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)