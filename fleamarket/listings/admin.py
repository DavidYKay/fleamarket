from django.contrib import admin
from listings.models import Item
#from listings.models import Choice
#admin.site.register(Poll)
#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

class ItemAdmin(admin.ModelAdmin):
    fields = [
        'seller', 
        'description',
        'price',
        'on_hand',
        'was_sold',
    ]
    #fieldsets = [
    #    (None, {'fields': ['question']}),
    #    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    #inlines = [ChoiceInline]
    #list_display = ('question', 'pub_date', 'was_published_today')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'
 
#admin.site.register(Choice)
#admin.site.register(Item, ItemAdmin)
admin.site.register(Item)
