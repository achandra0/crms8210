from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Vehicle
from django.urls import reverse_lazy


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ('owner', 'make', 'model', 'vin_number', 'purchase_date', 'last_service', 'description')
    template_name = 'vehicle_edit.html'

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('owner', 'make', 'model', 'vin_number', 'purchase_date', 'last_service', 'description')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
