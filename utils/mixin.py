from django.contrib.auth.decorators import login_required
from django.views.generic import View

class LoginRequired(View):
    @classmethod
    def as_view(cls,**initkwargs):
        view = super(LoginRequired,cls).as_view(**initkwargs)
        return login_required(view)