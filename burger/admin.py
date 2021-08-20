from django.contrib import admin

from .models import CarouselContent, BestBurger, PresidentBurger, HamburgerClient, OurGallery, \
    BlogPost, SingleBlog, GalleryImage, getInTouch


@admin.register(CarouselContent)
class CarouselContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


@admin.register(BestBurger)
class BestBurgerAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'image')


@admin.register(PresidentBurger)
class PresidentBurgerAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'image')


@admin.register(HamburgerClient)
class HamburgerClientAdmin(admin.ModelAdmin):
    list_display = ('comment', 'image', 'author', 'grade')


@admin.register(OurGallery)
class OurGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'comments', 'image', 'day')


@admin.register(SingleBlog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'comments', 'image')


@admin.register(GalleryImage)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(getInTouch)
class getInTouchAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'email', 'subject')
