from .forms import SignUpForm

def signup_form(request):
    return {'signup_form': SignUpForm()}