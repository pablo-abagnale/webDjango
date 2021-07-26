from django.contrib import admin
from cv_app.models import experiencia,estudios_formale,skill,hobbi,dato

class experiencia_admin(admin.ModelAdmin):
    list_display = ('empresa','puesto')
    search_fields = ('empresa','puesto')
    list_filter = ('puesto',)


class estudios_formales_admin(admin.ModelAdmin):
    list_display = ('lugar','titulo')
    search_fields = ('titulo',)
    list_filter = ('titulo',)


class skills_admin(admin.ModelAdmin):
    list_display = ('nivel','titulo')
    search_fields = ('titulo',)

class hobbis_admin(admin.ModelAdmin):
    list_display = ('actividad',)
    search_fields = ('actividad',)

class datos_admin(admin.ModelAdmin):
    list_display = ('nombre',)


# Register your models here.
admin.site.register(experiencia,experiencia_admin)
admin.site.register(estudios_formale,estudios_formales_admin)
admin.site.register(skill,skills_admin)
admin.site.register(hobbi,hobbis_admin)
admin.site.register(dato,datos_admin)