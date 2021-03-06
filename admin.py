from django.contrib import admin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('personal_number',)
       
admin.site.register(Company, CompanyAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'get_personal_number')
    search_fields = ('id',)
    
    def get_search_results(self, request, queryset, search_term):
       queryset, use_distinct = super().get_search_results(request, queryset, search_term)
       queryset |= self.model.objects.filter_by_personal_number(search_term)
       return queryset, use_distinct
   
admin.site.register(Vacancy, VacancyAdmin)
