from django.contrib import admin
from .models import Post , Category , Comment
# from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(admin.ModelAdmin):
# class PostAdmin(SummernoteModelAdmin):

#     date_hierarchy = 'published_date'
#     empty_value_display = '-empty-'
#     # soton ya radif hayi ke khali hastan ro empty mizare 
#     #
#     # fields = ('title', ) # ba in kar vgti ke vared poshe haye model mishavim fgt field 
#     #title ya har chiz dige ra mibinim va be bagiye dast rasi nadarim !!!
    
#     # ordering = []
    
#     # exclude = mitavanim begim in fidld ra dar nazar nagir  
    
    list_display = ('id' , 'title' , 'login_require', 'status')
    list_filter = ('status',)
    search_fields = ['title' , 'id']
    # summernote_fields = ('content',)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'post', 'approveh' , 'created_date' , 'email')
    search_fields = ['post' , 'approveh']

    
admin.site.register(Category)    
admin.site.register(Post, PostAdmin) 
admin.site.register(Comment , CommentAdmin) 