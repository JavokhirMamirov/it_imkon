from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(["GET"])
def get_viloyatlar(request):
    try:
        query = Viloyat.objects.all()
        ser = ViloyatSerializer(query, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)


@api_view(["GET"])
def get_tumanlar(request):
    try:
        viloyat = request.GET.get('viloyat')
        query = Tuman.objects.filter(viloyat_id=viloyat)
        ser = TumanSerializer(query, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)



@api_view(["GET"])
def get_mahallalar(request):
    try:
        tuman = request.GET.get('tuman')
        query = Mahalla.objects.filter(tuman_id=tuman)
        ser = MahallaSerializer(query, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)


@api_view(["GET"])
def get_games(request, pk=None):
    try:
        if pk is not None:
            query = Game.objects.get(id=pk)
            ser = GameSerializer(query)
        else:
            query = Game.objects.all()
            ser = GameNameSerializer(query, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)

@api_view(["GET"])
def get_yetakchi(request, pk=None):
    try:
        user = User.objects.get(id=pk)
        yetakchi = Yetakchi.objects.filter(mahalla=user.mahalla)
        yt = yetakchi.last()
        if yt is not None:
            chat_id = yt.chat_id
        else:
            chat_id = None
        data = {
            "success": True,
            "data": {
                "chat_id":chat_id
            }
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)

@api_view(["POST"])
def register(request, chat_id):
    try:
        try:
            user = User.objects.get(chat_id=chat_id)
        except User.DoesNotExist:
            user = User.objects.create(chat_id=chat_id)

        game = request.data.get("game")
        name = request.data.get("name")
        mahalla = request.data.get("mahalla")
        uy = request.data.get("uy")
        phone = request.data.get("phone")

        if game is not None:
            user.game_id = game
            user.status = 1

        if name is not None:
            user.name = name
            user.status = 2

        if phone is not None:
            user.phone = phone
            user.status = 3

        if mahalla is not None:
            user.mahalla_id = mahalla
            user.status = 4

        if uy is not None:
            user.uy = uy
            user.status = 5

        user.save()

        ser = UserSerializer(user)


        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)

@api_view(["GET"])
def get_user(request, chat_id=None):
    try:
        query = User.objects.get(chat_id=chat_id)
        ser = UserSerializer(query)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)
