from django.urls import path
from .views import home_page, EmployeeListView, SubdivisionListView

urlpatterns = [
    path('', home_page, name="home-page"),
    path('employees/<int:parent>', EmployeeListView.as_view(), name="emp-list"),
    path('div-list/', SubdivisionListView.as_view(), name="div-list"),
    path('div-list/<int:parent>', SubdivisionListView.as_view(), name="div-list"),
]
