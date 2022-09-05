from django.contrib.auth import login, authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

User = get_user_model()


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args,
                                                       **kwargs)
        # self.fields['first_name'].required = True
        # self.fields['last_name'].required = True

    class Meta:
        model = User
        # fields = ('username', 'email', 'first_name', 'last_name')
        fields = ('username', 'email')



def signup(request):
    if request.method == 'POST':
        return render(request, 'user/signup.html', {'form': form})
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        users = User.objects.all()
        return render(request, 'user/list_users.html', {'object_list': users})
