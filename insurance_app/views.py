from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import InsuranceData
from .serializers import InsuranceSerializer
from .forms import InsuranceForm

class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = InsuranceData.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['sex', 'smoker', 'region']

def index(request):
    """
    Main page with application details and hyperlinks to endpoints.
    """
    context = {
        'python_version': '3.9.1',
        'django_version': '4.2',
        'packages': ['djangorestframework', 'django-filter'],
        'admin_user': 'hassan@hassan.com',
        'admin_password': '123456'
    }
    return render(request, 'insurance_app/index.html', context)

def add_insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insurance_list')
    else:
        form = InsuranceForm()
    return render(request, 'insurance_app/add_insurance.html', {'form': form})

def insurance_list(request):
    entries = InsuranceData.objects.all()
    return render(request, 'insurance_app/insurance_list.html', {'entries': entries})

def update_insurance(request, pk):
    insurance = get_object_or_404(InsuranceData, pk=pk)
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect('insurance_list')
    else:
        form = InsuranceForm(instance=insurance)
    return render(request, 'insurance_app/update_insurance.html', {'form': form})

def delete_insurance(request, pk):
    insurance = get_object_or_404(InsuranceData, pk=pk)
    if request.method == 'POST':
        insurance.delete()
        return redirect('insurance_list')
    return render(request, 'insurance_app/confirm_delete.html', {'object': insurance})

def insurance_list_view(request):
    return render(request, 'insurance_app/filter_list.html')
