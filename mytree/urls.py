from django.urls import path
from .views import home_page, JobsListView, EmployeeListView, SubdivisionListView

urlpatterns = [
    # path('', home_page, name="home_page"),
    path('jobs/', JobsListView.as_view(), name="job-list"),
    path('employees/<int:parent>', EmployeeListView.as_view(), name="emp-list"),
    path('employees/', EmployeeListView.as_view(), name="emp-list"),
    path('div-list/', SubdivisionListView.as_view(), name="div-list"),
    path('div-list/<int:parent>', SubdivisionListView.as_view(), name="div-list"),
]
