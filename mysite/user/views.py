from django.shortcuts import render, HttpResponse
from .models import User, Contact
from django.views.generic import CreateView
from django.utils.translation import gettext as _
from django.core.paginator import Paginator
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



def home(request):
    text  = _("So'ngi dars ")
    news = User.objects.all().order_by('-id')
    paginator = Paginator(news, 3)  # Show 3 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home.html", {"page_obj": page_obj, "taxt":text})
   # return render(request, 'home.html', {'news':news, 'text':text, 'lang':lang  })

class PostDetailView(DetailView):
    model = User
    template_name = "detail.html"
    context_object_name = "new"


class  CreateNew(CreateView):
    model = User
    fields = "__all__"
    template_name = 'new.html'

def Login(request):
    return HttpResponse("""<h1>Login</h1>""")


class RegisterUser(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))




def contact(request):
    if request.method == 'POST':
        model = Contact()
        model.name = request.POST.get('name')
        model.subject = request.POST.get('subject')
        model.number = request.POST.get('number')
        model.tg_name = request.POST.get('tg_name')


        model.save()
        return render(request, "contact.html")

    else:
        return render(request, "contact.html")




