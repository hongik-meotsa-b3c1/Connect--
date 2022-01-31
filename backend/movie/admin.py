from django.contrib import admin
from .models import MovieInfo,MoviePost
from django.utils.safestring import mark_safe



@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(MoviePost)
class MoviePostAdmin(admin.ModelAdmin):
    list_display=["post_id","title", "image"]
    list_display_links = ["post_id"]

    def image(self, moviePost):
        return mark_safe(f"<img src={moviePost.movie_image} style='width: 100px;' />")
    
