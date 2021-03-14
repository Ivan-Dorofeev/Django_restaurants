from django.contrib import admin
from .models import Restaurant, Waiter


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city', 'director']
    list_filter = ['city', 'country']
    search_fields = ['name']
    fieldsets = (
        ('Основаные сведения', {
            'fields': ('name', 'description', 'count_of_employers', 'director', 'chef')
        }),
        ('Локация и контакты', {
            'fields': ('country', 'city', 'street', 'house'),
            'classes': ['collapse']
        }),
        ('Сервис', {
            'fields': (
                'serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_donats', 'serves_coffee'),
            'description': 'Основные серсисы, преддоставляемые рестораном',
            'classes': ['collapse']
        })
    )


class WaiterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'restaurant', 'status']
    list_filter = ['restaurant', 'city']
    search_fields = ['first_name', 'last_name']
    actions = ['mark_wait', 'mark_ready']

    def mark_wait(self, request, queryset):
        queryset.update(status='w')

    def mark_ready(self, request, queryset):
        queryset.update(status='r')

    mark_wait.short_description = 'Поставить в ожидание'
    mark_ready.short_description = 'Пометить как в записи'


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
