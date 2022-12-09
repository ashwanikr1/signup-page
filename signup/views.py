from django.shortcuts import render

import psycopg2 as pg
# Create your views here.
first_name=''
last_name=''
email=''
pwd=''

def signupPage(request):
    global first_name,last_name,email,pwd
    if request.method == "post":
        m=pg.connect(host="localhost",user="ashwani",password="Test@4321",database="users")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                first_name=value
            if key=="last_name":
                last_name=value
            if key=="email":
                email=value
            if key=="password":
                password=value

        c="insert into users Values('{}','{}','{}','{}')".format(first_name,last_name,email,pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request,'signup.html')

    
