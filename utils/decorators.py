from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            try:
                if request.user.profile.role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            except:
                pass
            raise PermissionDenied
        return wrapped
    return decorator