from django.shortcuts import render
from django.views.generic import ListView
from .models import Job, Employee, Subdivision


def home_page(request):
    ctx = {"name": "Hello world"}
    return render(request, 'index.html', ctx)


class JobsListView(ListView):
    template_name = 'jobs.html'
    paginate_by = 3
    model = Job


class SubdivisionListView(ListView):
    template_name = 'subdivision.html'
    # ordering = '-time_bought_at'
    paginate_by = 3
    model = Subdivision

    def get_queryset(self):
        if self.kwargs.__contains__('parent'):
            self.queryset = Subdivision.filter(parent=self.kwargs['parent'])
        else:
            self.queryset = Subdivision.filter(parent=None)

        return super().get_queryset()


class EmployeeListView(ListView):
    template_name = 'employee.html'
    # ordering = '-time_bought_at'
    paginate_by = 3
    model = Employee

    def get_queryset(self):
        if self.kwargs.__contains__('parent'):
            self.queryset = Employee.filter(subdivision=self.kwargs['parent'])
        else:
            self.queryset = Employee.filter(subdivision=None)

        return super().get_queryset()
