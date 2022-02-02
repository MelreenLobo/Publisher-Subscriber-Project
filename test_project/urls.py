# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import path
from test_project import views

urlpatterns = [
    path('', views.main),   # Loads Landing Page
    path('transaction/', views.transaction_api),   # Transaction API
    path('transaction_summary_bySKU/', views.transaction_summary_by_name_api),  # Summary by Name API
    path('transaction_summary_byCategory/', views.transaction_summary_by_category_api),  # Summary by category API
]