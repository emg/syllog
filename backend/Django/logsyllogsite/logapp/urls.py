from django.urls import path, re_path
from . import views


urlpatterns = [
   path('', views.root_view,  name='root_view'),
   path('log/', views.log, name='log'),
   path('log3/', views.log3, name='log3'),
   path('log4/', views.log4, name='log4'),
   path('log5/', views.log5, name='log5'),
   path('dump/', views.dump, name='dump'),
   path('dump2/', views.dump2, name='dump2'),
   path('dump3/', views.dump3, name='dump3'),
   path('dump4/', views.dump4, name='dump4'),
   path('dump5/', views.dump5, name='dump5'),
   path('dump3/aggregatesess/', views.dump3_aggregatesess, name='dump3_aggregatesess'),
   re_path('^dump3/syllogism_based/valid_only/(?P<start_date>\d\d\d\d-\d\d-\d\d)/(?P<end_date>\d\d\d\d-\d\d-\d\d)/$', views.dump3_syllogism_based_validonly_dates, name='dump3_syllogism_based_validonly_dates'),
   path('dump3/syllogism_based/valid_only/', views.dump3_syllogism_based_validonly, name='dump3_syllogism_based_validonly'),
   re_path('^dump3/syllogism_based/valid_and_invalid/(?P<start_date>\d\d\d\d-\d\d-\d\d)/(?P<end_date>\d\d\d\d-\d\d-\d\d)/$', views.dump3_syllogism_based_valid_and_invalid_dates, name='dump3_syllogism_based_valid_and_invalid_dates'),
   path('dump3/syllogism_based/valid_and_invalid/', views.dump3_syllogism_based_valid_and_invalid, name='dump3_syllogism_based_valid_and_invalid'),
   path('dump4/aggregatesess/', views.dump4_aggregatesess, name='dump4_aggregatesess'),
   path('dump5/aggregatesess/', views.dump5_aggregatesess, name='dump5_aggregatesess'),
]
