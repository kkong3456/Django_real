from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

# Create your views here.
class ProductList(ListView):
    model=Product
    template_name='product.html'
    #context_object_name='product_list' 템플릿 파일에 object_list가 아닌 product_list로 객체를 전달할 수있다.

class ProductCreate(FormView):
    template_name='register_product1.html'
    form_class=RegisterForm
    success_url='/product/'

class ProductDetail(DetailView):
    template_name='product_detail.html'
    queryset=Product.objects.all()
    context_object_name='product'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)

        context['form']=OrderForm(self.request)
        return context