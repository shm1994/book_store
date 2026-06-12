from django.contrib import admin

from books.models import Book ,Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'book','datetime_created','recommend','is_active')
    list_filter = ('user', 'book')
    search_fields = ('text',)
    ordering = ('-datetime_created',)


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)
