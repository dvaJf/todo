from .models import Task
from django.forms import ModelForm, TextInput, Textarea,DateInput,ChoiceField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title",'text',"deadline"]
        widgets = {'title':TextInput(attrs={
                                    'placeholder':'Введите название...'}),
                   'text':Textarea(attrs={
                                    'placeholder':'Введите описание...'}),
                   'deadline':DateInput(attrs={'type': 'date'}),}

User=get_user_model()
class UserCreationForm1(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User