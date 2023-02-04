

from rest_framework import serializers
from .models import Movie ,Reservation,Guest,Post
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        # fields = '__all__'
        fields = ['pk', 'reservation', 'name', 'mobile']
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    