from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm


# Create your views here.

class OrderCreate(FormView):
    form_class=RegisterForm
    success_url='/product/'


    def form_invalid(self,form):   # 폼 전달이 실패할때.. 수량이 빈칸일때..등
        print(f'약오르지')
        return redirect('/product/'+str(form.product))

    def get_form_kwargs(self,**kwargs):  #FormView에 있는 메소드로 인자값을 추가할때 사용함
        kw=super().get_form_kwargs(**kwargs)
        kw.update({
            'request':self.request
        })

        return kw

