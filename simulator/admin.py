from django.contrib import admin

from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.models.realestate import Flat, Room
from simulator.models.prices import Price
from simulator.models.deals import Sale, Rent


admin.site.register(PhysicalEntity)
admin.site.register(LegalEntity)
admin.site.register(Flat)
admin.site.register(Room)
admin.site.register(Price)
admin.site.register(Sale)
admin.site.register(Rent)
