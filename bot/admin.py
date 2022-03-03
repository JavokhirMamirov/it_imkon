from django.contrib import admin

# Register your models here.
from bot.models import Viloyat, Tuman, Mahalla, Game, Yetakchi, User

admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Mahalla)
admin.site.register(Game)
admin.site.register(Yetakchi)
admin.site.register(User)
