from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

# from django.contrib.auth.views import password_reset, password_reset_done

urlpatterns = [


    url(r'^$', views.form_login, name='form_login'),
    url(r'^crear_cuenta/$', views.crear_cuenta, name='crear_cuenta'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    url(r'^404/$', views.e404, name='e404'),
    # url(r'^login/auth', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^inicio/$', views.inicio, name='inicio'),
    url(r'^proyectos/$', views.proyectos, name='proyectos'),
    url(r'^proyectodetalles/(?P<id>\d+)/$', views.proyectodetalles, name='proyectodetalles'),
    url(r'^tareadetalles/(?P<id>\d+)/$', views.tareadetalles, name='tareadetalles'),
    url(r'^borrartarea/(?P<tareaid>\d+)/(?P<proyectoid>\d+)/$', views.borrartarea, name='borrartarea'),
    url(r'^borrarproyecto/(?P<id>\d+)/$', views.borrarproyecto, name='borrarproyecto'),
    url(r'^proyectos/crear_proyecto/$', views.crear_proyecto, name='crear_proyecto'),
    url(r'^peliculas/crear/$', views.form_proyectos, name='form_proyectos'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^tareas/$', views.tareas, name='tareas'),
    url(r'^tareas/crear/(?P<id>\d+)/$', views.form_tareas, name='form_tareas'),

    url(r'^activar/(?P<tareaid>\d+)/(?P<devid>\d+)/$', views.activar, name='activar'),
    url(r'^desactivar/(?P<tareaid>\d+)/(?P<devid>\d+)/$', views.desactivar, name='desactivar'),
    url(r'^borrardev/(?P<tareaid>\d+)/(?P<devid>\d+)/$', views.borrardev, name='borrardev'),



        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),





    # url(r'^reset-password/$', password_reset, name='reset-passsword'),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


]
