# 이 폼이 뷰에서 활용되는 방식
from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)