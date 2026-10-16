from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'first_name': 'asmaa',  
        'last_name': 'ABU Jaber', 
        'student_id': 220231014,
        'address': 'palestine, Gaza', 
        'email': 'asmaaadnan2005.a@gmail.com', 
        'birth_date': datetime(2005, 10, 16), 
    }
    
    # هان بدنا نمرر البيانات إلى القالب 
    return render(request, 'pages/index.html', context)