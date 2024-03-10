from django.contrib import admin

# Register your models here.
from .models import Post, Category

# class CommentItemInline(admin.TabularInline):
#     model = Comment
#     row_id_field = ['post']
    
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    # inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}
    
    
    
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']    
    prepopulated_fields = {'slug': ('title',)}
    
    
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'post', 'created_at']
#     # search_fields = ['body']   

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)