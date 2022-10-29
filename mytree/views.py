from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Job, Employee, Subdivision
from .serializers import SubdivisionModelSerializer
import json


def home_page(request):
    divs = Subdivision.objects.filter(parent=None)
    serializer = SubdivisionModelSerializer(divs, many=True)
    data = json.dumps(serializer.data, ensure_ascii=False).encode('utf8').decode()
    return render(request, 'treeview.html', {"divs": data})


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.__contains__('parent'):
            context['subdivision'] = self.kwargs['parent']
        return context


class EmployeeListView(ListView):
    template_name = 'employee.html'
    paginate_by = 3
    model = Employee

    def get_queryset(self):
        if self.kwargs.__contains__('parent'):
            self.queryset = Employee.filter(subdivision=self.kwargs['parent'])
        else:
            self.queryset = Employee.filter(subdivision=None)

        return super().get_queryset()
