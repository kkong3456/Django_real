from django import forms 
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction

class RegisterForm(forms.Form):
    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request=request

    quantity=forms.IntegerField(
        error_messages={
            'required':'수량을 입력해 주세요.'
        }, label='수량'
    )
    product=forms.IntegerField(  #product.id를 안보이게 전달하려는 구문
        error_messages={
            'required':'상품설명을 입력해주세요'
        },label='상품설명',widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data=super().clean()
        quantity=cleaned_data.get('quantity')
        product=cleaned_data.get('product')
        fcuser=self.request.session.get('user')
        #print(f'fcuser is {fcuser}')
        # print(f'self.request.session is {self.request.session}')

        if not(quantity and product):
            
            # with transaction.atomic():  # with안에 있는 것들은 transaction처리된다.
            #     prod=Product.objects.get(pk=product)

            #     order=Order(
            #         quantity=quantity,
            #         product=prod,
            #         fcuser=Fcuser.objects.get(email=fcuser)
            #     )
            #     order.save()
            #     prod.stock-=quantity
            #     prod.save()
        
            self.add_error('quantity','값이 없습니다.')
            self.add_error('product','상품이 없습니다.')