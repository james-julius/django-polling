from django.contrib import admin
# admin.autodiscover()
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,  {'fields': ['question_text']}),
            ('Date Information',  {'fields': ['pub_date']}),
        ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
        
# Register your models here.
admin.site.register(Question, QuestionAdmin)
