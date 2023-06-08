from django.contrib import admin
from .models import Portfolio

# Adding tables to admin panel
class PortfolioTable(admin.ModelAdmin):
    list_display = ("user_name", "id")

# Register your models here.
admin.site.register(Portfolio,PortfolioTable)

# username = faizan
# pass = faizan