from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('owner_panel/', views.owner_panel),
    path('owner_panel/create/', views.owner_panel_create),
    path('edit_occupant/<page_name>', views.edit_occupant, name='edit_occupant'),
    path('zhiteli/<page_name>', views.occupant_page, name='occupant_page'),
    path('login/', views.login_page),
    path('logout/', views.logout_view),
    path('interactions/<page_name>', views.interactions, name='interactions'),
    path('kisses/', views.kisses),
    path('requestkisses/', views.requestkisses),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
