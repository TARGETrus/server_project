from django.contrib import admin

from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.models.realestate import Flat, Room
from simulator.models.prices import Price
from simulator.models.deals import Sale, Rent


class PhysicalEntityAdmin(admin.ModelAdmin):
    model = PhysicalEntity
    list_display = ['get_name']

    def get_name(self, obj):
        return 'PhysicalEntity: %s' % obj.id


class LegalEntityAdmin(admin.ModelAdmin):
    model = LegalEntity
    list_display = ['get_name']

    def get_name(self, obj):
        return 'LegalEntity: ' + str(obj.id)


class FlatAdmin(admin.ModelAdmin):
    model = Flat
    list_display = ['get_name']

    def get_name(self, obj):
        return 'Flat: ' + str(obj.id)


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ['get_name']

    def get_name(self, obj):
        return 'Room: ' + str(obj.id)


class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['get_name']

    def get_name(self, obj):
        return 'Price: ' + str(obj.id)


class SaleAdmin(admin.ModelAdmin):
    model = Sale
    list_display = ['get_name']

    def get_name(self, obj):
        return 'Sale: ' + str(obj.id)


class RentAdmin(admin.ModelAdmin):
    model = Rent
    list_display = ['get_name']

    def get_name(self, obj):
        return 'Rent: ' + str(obj.id)


admin.site.register(PhysicalEntity, PhysicalEntityAdmin)
admin.site.register(LegalEntity, LegalEntityAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Rent, RentAdmin)
