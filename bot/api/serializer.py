from rest_framework import serializers

from bot.models import *

class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = "__all__"

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = "__all__"

class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = "__all__"

class GameNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class YetakchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yetakchi
        fields = ['id', 'chat_id']

class UserSerializer(serializers.ModelSerializer):
    mahalla = serializers.SerializerMethodField()
    game = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = "__all__"

    def get_mahalla(self, obj):
        try:
            return obj.mahalla.name
        except:
            return None


    def get_game(self, obj):
        try:
            return obj.game.name
        except:
            return None