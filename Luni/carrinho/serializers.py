from .models import Carrinho
from rest_framework import serializers


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'
        