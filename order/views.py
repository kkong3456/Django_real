from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from fcuser.decorators import login_required
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.views.generic import ListView
from .models import Order
from fcuser.models import Fcuser
from django.db import transaction
from product.models import Product


# Create your views here.

@method_decorator(login_required,name='dispatch')
class OrderCreate(FormView):
    form_class=RegisterForm
    success_url='/product/'
    # template_name='index.html'  직접 /order/create를 치면 index.html이 나온다

    def form_valid(self,form):  #폼전달이 성공일때
        with transaction.atomic():
            prod=Product.objects.get(pk=form.data.get('product'))
            order=Order(
                quantity=form.data.get('quantity'),
                product=prod,
                fcuser=Fcuser.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock-=int(form.data.get('quantity'))
            prod.save()

        return super().form_valid(form)

    
    def form_invalid(self,form):   # 폼 전달이 실패할때.. 수량이 빈칸일때..등
        print(f'약오르지')

        return redirect('/product/'+str(form.data.get('product')))

    def get_form_kwargs(self,**kwargs):  #FormView에 있는 메소드로 인자값을 추가할때 사용함
        kw=super().get_form_kwargs(**kwargs)
        kw.update({
            'request':self.request
        })

        return kw

@method_decorator(login_required,name='dispatch')
class OrderList(ListView):
    template_name='order.html'
    context_object_name='order_list'

    def get_queryset(self,**kwargs):
        queryset=Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset
   

