from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment, Board

@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


admin.site.register(Goal)
admin.site.register(GoalComment)
admin.site.register(Board)
