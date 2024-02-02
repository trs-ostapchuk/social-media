from django.contrib import admin

from social_app.models import Profile, Post, LikePost

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
