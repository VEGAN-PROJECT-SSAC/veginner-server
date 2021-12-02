from django import forms
import datetime
from django.forms.widgets import NumberInput

POST_SORT_CHOICES = [
    ("Vegan", "Vegan"),
    ("Lacto", "Lacto"),
    ("Ovo", "Ovo"),
    ("Lacto-Ovo", "Lacto-Ovo"),
    ("Pesco", "Pesco"),
    ("Pollo", "Pollo"),
    ("Flexitarian", "Flexitarian")
    ]


class PostForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today(), widget=NumberInput(attrs={'type': 'date'}), label='date', required=True)
    food_name = forms.CharField(max_length=50, label='food_name', required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label='content', required=True)
    post_vegan_type = forms.ChoiceField(choices=POST_SORT_CHOICES, label='post_vegan_type', required=True)
    image = forms.ImageField(label='image', required=True)

    def clean(self):
        now = datetime.date.today()
        form_data = self.cleaned_data
        if now < form_data["date"]:
            raise forms.ValidationError("오늘 날짜까지 입력할 수 있습니다.")
        if 'date' in self._errors:
            raise forms.ValidationError("date 에러")
        if 'food_name' in self._errors:
            raise forms.ValidationError("food_name 에러")
        if 'content' in self._errors:
            raise forms.ValidationError("content 에러")
        if 'post_vegan_type' in self._errors:
            raise forms.ValidationError("post_vegan_type 에러")
        if 'image' in self._errors:
            raise forms.ValidationError("image 에러")
        return form_data