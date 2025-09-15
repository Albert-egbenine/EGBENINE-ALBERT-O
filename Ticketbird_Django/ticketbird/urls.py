from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Core pages
    path('', core_views.home, name='home'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('register/', core_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Event booking
    path('book/<int:event_id>/', core_views.book_event, name='book_event'),

    # Fake payment flow
    path('payment/<int:booking_id>/', core_views.fake_payment, name='fake_payment'),
    path('payment/success/<int:booking_id>/', core_views.payment_success, name='payment_success'),
    path('payment/failed/<int:booking_id>/', core_views.payment_failed, name='payment_failed'),
]

# Media file handling (for event images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)