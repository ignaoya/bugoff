from django.contrib import admin

from .models import Project, Bug, Worknote

@admin.register(Project)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('project', 'complete', 'open_date')
    list_filter = ('complete', 'open_date', 'project')
    ordering = ('project', 'open_date')

@admin.register(Worknote)
class WorknoteAdmin(admin.ModelAdmin):
    list_display = ('bug', 'date')

