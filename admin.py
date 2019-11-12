from django.contrib import admin

from homework1.models import Table, Column

# TODO: Implement movie, person and country model admins
class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_date', 'actual_date')
    pass


admin.site.register(Table, TableAdmin)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'datatype')
    pass


admin.site.register(Column, ColumnAdmin)


