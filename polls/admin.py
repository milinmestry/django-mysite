from django.contrib import admin

from .models import Choice, Question
# Register your models here.

# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']})
        , ('Date information', {'fields': ['pub_date']})]

    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 25
    # list_display_links = ('question_text',)

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
