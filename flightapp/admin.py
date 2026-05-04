from django.contrib import admin
from .models import *            #site modeli so *

class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 0


class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", "year_founded", "outside_Europe")
    inlines = [AirlinePilotInline,]

    def has_add_permission(self, request):
        return True

    fieldsets = [ #се става во рамки на класа/модел и може да се користат колоните од таа класа за поделба во секции
        (
            'Basic options',
            {
                "fields": ["name", "year_founded"],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["outside_Europe"],
            },
        ),
    ]


class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def get_queryset(self, request):
        return Flight.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj,'user',None) is None:
            obj.user = request.user
        obj.save()


    def has_change_permission(self, request, obj = None):    #може obj да биде none/null затоа мора да провериме дали постои прво инаку фрла грешка
        if obj and obj.user == request.user:      #ако тој што пробува да смени нешто(obj.user) е тој што е тековно најавен(request.user) = дозволи му инаку не
            return True
        return False



admin.site.register(Flight, FlightAdmin)
admin.site.register(Baloon)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)