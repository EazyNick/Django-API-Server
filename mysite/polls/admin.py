from django.contrib import admin
from .models import *

# #Register your models here
# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question_text']}),
        # 'classes': ['collapse']}로 숨기기 기능 가능
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),        
    ]
    # pub_date는 auto 등록 해놨기 때문에, 읽기전용으로 해야 에러가 안난다.
    readonly_fields = ['pub_date']
    # 질문 항목에서도 답변 항목을 수정 가능하게 함
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)