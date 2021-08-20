from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from burger.views import HomePage, MenuPage, AboutPageView, BlogView, SingleView, Pages, ContactView
urlpatterns = [
    path('', HomePage.as_view(), name='main-menu'),
    path('menu/', MenuPage.as_view(), name='menu'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('single-blog/', SingleView, name='single-blog'),
    path('pages/', Pages.as_view(), name='pages'),
    path('contact/', ContactView, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
