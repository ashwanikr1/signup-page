from django.shortcuts import render

import psycopg2 as pg
# Create your views here.

email=''
pwd=''

def loginPage(request):
    global email,pwd
    if request.method == "post":
        m=pg.connect(host="localhost",user="ashwani",password="Test@4321",database="users")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="password":
                pwd=value

        c="select * from users where email='{}' and password='{}'".format(email,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
    
    return render(request,'login.html')
