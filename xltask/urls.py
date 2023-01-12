from django.urls import path
from xltask import registration,employee_api
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', registration.start, name="home" ),
    path('dashboard', registration.dashboard, name="dashboard" ),
    path('signup', registration.register, name="signup"),
    path('signin', registration.signin, name="signin"),
    path('signout', registration.signout, name="signout"),
    path('excel', registration.Excel_store,name="excel"),
    path('save', registration.save_data,name="save"),

    # api  urls
    path('api/emp/', employee_api.Emp_list),
    path('api/emp/<int:id>', employee_api.Emp_details),
    path('api/dep/', employee_api.Dep_list),

]

