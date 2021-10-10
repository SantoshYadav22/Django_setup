from django.contrib import admin
from core.models import Student


# admin.site.register(Student)    ----------------first type



# class StudentAdmin(admin.ModelAdmin):         ----------------second type
#     list_display=('id','studid','studname','studmail','studpass','comment')

# admin.site.register(Student, StudentAdmin)



# third type-----------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):    
    list_display=('id','studid','studname','studmail','studpass','comment')

