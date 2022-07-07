from django.contrib import admin

from main.models import Comment, Tickets


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user', 'is_active', 'created_at')
    search_fields = ('title', 'content')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'content', 'created_at')
    search_fields = ('ticket',)


admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Comment, CommentAdmin)