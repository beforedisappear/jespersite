from django import forms
from .models import *

class AddArticleForm(forms.ModelForm):
   #констуктор для невыбранного значения формы
   def __init__(self, *args, **kwargs):
      super(AddArticleForm, self).__init__(*args, **kwargs)
      #self.fields['section'].empty_label = ' '
      self.fields["section"].choices = [("", ""),] + list(self.fields["section"].choices)[1:]
   
   class Meta:
      #связь формы с моделью
      model = articles
      #отображаемые поля
      fields = ['section', 'author', 'title', 'subtitle', 'text', 'content']
      widgets = {
         'title': forms.TextInput(attrs={'class': 'form-input'}),
         'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
      }
   