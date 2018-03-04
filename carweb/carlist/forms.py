from django import forms
from carlist.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','car_make','car_model','car_price','car_lease')

        widgets = {
            'car_make':forms.TextInput(attrs={'class':'textinputclass'}),
            'car_model':forms.TextInput(attrs={'class':'textinputclass postcontent'})
        }
