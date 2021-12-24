from django.urls import path
from . import views

urlpatterns = [
    path('albums', views.get_albums),
    path('albums/<album_id>', views.get_album),

    path('tracks', views.get_tracks),
    path('tracks/<track_id>', views.get_track),

    path('artists', views.get_artists),
    path('artists/<artist_id>', views.get_artist),

    path('lists', views.get_lists),
    path('lists/<list_id>', views.get_list),

    path('public', views.get_public_lists),
    path('public/<list_id>', views.get_public_list),

    path('my_lists', views.get_private_lists),
    path('my_lists/<list_id>', views.get_private_list)

]
