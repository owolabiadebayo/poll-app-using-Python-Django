from django.shortcuts import get_object_or_404, render, redirect, reverse 
from django.urls import reverse_lazy
from . import models

from django.views.generic.edit import DeleteView, UpdateView

from django.views.generic import ListView
from article.models import Contact
from django.views.generic.edit import FormView
from article.forms import ContactForm




class IndexDeleteView(DeleteView):
	# specify the model you want to use
    model = models.Contact
    pk_url_kwargs = 'id'
    template_name = 'article/confirm_delete.html'
    success_url = reverse_lazy('home')


# class ContactView(FormView):
#     template_name = 'article/contact.html'
#     form_class = ContactForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)




# class ContactCreate(CreateView):
#     model = Contact
#     fields = ['name']  
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
#     form_class = ContactForm



def index(request):
    context = {
        "cars": models.Car.objects.all(),
        "contacts": models.Contact.objects.all()
    }

    if request.method == 'POST':
        query = request.POST.get("query")
        car_name = request.POST.get("car_name")
        car_models = request.POST.get("car_model")
        contact = models.Contact(name=query)
        contact.save()
        car = models.Car(name=car_name)
        car.save()  
        car_model= models.Car(car_model=car_models)
        context["car"] = car_model 
        person = models.Contact.objects.last().name
        context["contact"] = person
        print(person)
        print(car)
        return render(request, "article/index.html", context)

    return render(request, "article/index.html", context)



def delete_contact(request, p_id):
    person_to_del = models.Contact.objects.get(p_id)
    person_to_del.delete()
    person_to_del.commit()



class HomeListView(ListView):
    model = Contact
    http_method_names=['get', 'post', 'put', 'delete']
    context_object_name= "contacts"
    template_name = "article/index.html"
   

    def post(self, request, *args, **kwargs):
        contact = request.POST.get('query')
        print(contact)
        c = Contact(name=contact)
        c.save()
        return render(request, self.template_name, {'contacts': Contact.objects.all()})
      

class DeleteListView(DeleteView):
    model = Contact
    pk_url_kwargs = 'id'
    template_name = 'article/confirm_delete.html'
    success_url = reverse_lazy('article:home')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Contact, id=id_)


class UpdateListView(UpdateView):
    model = Contact
    fields=['name']
    template_name= 'article/confirm_update.html'
    success_url= reverse_lazy('article:home')


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Contact, id=id_)

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        
        return super().form_valid(form)




