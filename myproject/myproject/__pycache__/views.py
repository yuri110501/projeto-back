from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from models import Product, Order
from serializers import ProductSerializer, OrderSerializer
from services.order_service import OrderService
from repositories.order_repository import OrderRepository

@api_view(['POST'])
def create_order(request):
    data = request.data
    try:
        order = OrderService.create_order(data['product_id'], data['quantity'])
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order(request, order_id):
    try:
        order = OrderRepository.get_order_by_id(order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_order(request, order_id):
    data = request.data
    try:
        order = OrderService.update_order(order_id, data['quantity'])
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_order(request, order_id):
    try:
        OrderService.delete_order(order_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
