from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):  #UserCreationForm을 상속받아서 새로운 클래스를 만듦
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
