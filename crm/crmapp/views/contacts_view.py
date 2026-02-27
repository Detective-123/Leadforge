from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.contact import Contact

# NEEDS UPDATE NOT FINAL ON HOLD FUNCTION
class ContactListView(LoginRequiredMixin, ListView):
  model = Contact
  template_name="contact/list.html"
  context_object_name="contacts"

  def get_queryset(self):
    return Contact.objects.filter(company=self.request.user.company)
  
# NEEDS UPDATE NOT FINAL ON HOLD FUNCTION
class ContactCreateView(LoginRequiredMixin, CreateView):
  model=Contact
  fields=['title', 'email', 'phone']