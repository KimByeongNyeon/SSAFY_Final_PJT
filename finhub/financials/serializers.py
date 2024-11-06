from rest_framework import serializers
from .models import FinancialProducts,FinancialOptions,FinancialComment
class FinancialProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinancialProducts
        fields = "__all__"

class FinancialOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOptions
        fields = "__all__"
        read_only_fields = ('product',)

class FinancialCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialComment
        fields = "__all__"
        read_only_fields = ('users, financial_products')