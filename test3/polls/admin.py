from django.contrib import admin

from .models import Topics, News, SectionTopic, SectionNews, BadWords, NoBadWords, Items, Runes, Champions, Ability


admin.site.register(Topics)
admin.site.register(News)
admin.site.register(SectionNews)
admin.site.register(SectionTopic)
admin.site.register(BadWords)
admin.site.register(NoBadWords)
admin.site.register(Items)
admin.site.register(Runes)
admin.site.register(Champions)
admin.site.register(Ability)

'''
class SpecialityInline(admin.TabularInline):
    model = Speciality
    extra = 3


class DoctorAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,                 {'fields': ['first_name']} ),
    #    ('speciality',         {'fields': ['allspeciality'], 'classes': ['collapse']}),
    #]
    list_display = ('first_name', 'two_name', 'patronymic_name')
    list_filter = ['all_speciality']


admin.site.register(Doctor, DoctorAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    list_display =('specialty_name')
    list_filter = ['specialty_name']


admin.site.register(Speciality)


class BadWordsAdmin(admin.ModelAdmin):

    list_filter = ['word']


class NoBadWordsAdmin(admin.ModelAdmin):

    list_filter = ['word']


admin.site.register(BadWords, BadWordsAdmin)
admin.site.register(NoBadWords, NoBadWordsAdmin)


class ReviewAdmin(admin.ModelAdmin):


    list_display = ('doctor', 'pub_date', 'review_text', 'edit_review_text', 'user', 'ip_user')
    list_filter = ['doctor', 'pub_date']


admin.site.register(Review, ReviewAdmin)


'''