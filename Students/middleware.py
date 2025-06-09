from django.conf import settings
import datetime
from django.shortcuts import redirect


class CustomSessionAutoLogoutMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response

    def __call__(self, request , *args, **kwds):
        
        user_id = request.session.get('student_id')
        user_id = request.session.get('teacher_login')
        if not user_id:
            return self.get_response(request)
        
        curretn_time = datetime.datetime.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            last_activity = datetime.datetime.strptime(last_activity , "%Y-%m-%d %H:%M:%S.%f")
            inactivity = (curretn_time - last_activity).seconds

            if inactivity > 600:
                request.session.flush()
                return redirect('Home')
        
        request.session['last_activity']  = str(curretn_time)
    
        return self.get_response(request)

