from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): #model을 form으로 바꿔주는 것.
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']



