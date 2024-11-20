from rest_framework import serializers
from dealers.models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'name', 'location', 'contact_info']
