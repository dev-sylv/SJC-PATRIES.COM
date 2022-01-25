from Snacks_App.models import *
import datetime

def footer_date(request):
    return{'date_footer': datetime.datetime.now()}