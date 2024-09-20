from .models import Blog, BlogDetail, AdditionalImage, Tag, Category,PortfolioProject
from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Technology ,Brand,Service1,CustomerReview,FAQ,Testimonial,TeamMember,TimelineEvent,Contact, GalleryImage

from django.utils.html import format_html

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_image') 
    def logo_image(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "No Logo"

    logo_image.short_description = 'Logo'  


admin.site.register(Service)
admin.site.register(Technology)
admin.site.register(Service1)
admin.site.register(CustomerReview)
admin.site.register(Testimonial)
admin.site.register(FAQ)
admin.site.register(TeamMember)
admin.site.register(TimelineEvent)
admin.site.register(Contact)


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')
    readonly_fields = ('image_thumbnail',)
    
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="700" height="845" />')
        return "No Image"

    image_thumbnail.short_description = 'Image Thumbnail'

admin.site.register(GalleryImage, GalleryImageAdmin)


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_date', 'author')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BlogDetail)
class BlogDetailAdmin(admin.ModelAdmin):
    list_display = ('blog', 'content')

@admin.register(AdditionalImage)
class AdditionalImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

