from django import forms 
from .models import Order

class OrderForm(forms.Form):
    quantity=forms.IntegerField(
        error_messages={
            'required':'수량을 입력해 주세요.'
        }, label='수량'
    )
    product=forms.IntergerField(
        error_messages={
            'required':'상품설명을 입력해주세요'
        },label='상품설명',widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data=super().clean()