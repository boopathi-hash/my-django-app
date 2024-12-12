from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods  
from django.template import loader
from myapp.templates.form import StdForm 
from myapp.templates.functions import handle_uploaded_file  
from myapp.templates.fu_form import StudentForm   
from myapp.models import Employee  
from reportlab.pdfgen import canvas
import datetime
import csv

# Create your views here.


def hello(request):
    return HttpResponse("<h1>Hello World</h1>");

def index(request):
    now = datetime.datetime.now()
    html =  "<html><body><h3>Now time is... %s.</h3></body></html>" % now    
    return HttpResponse(html);

def index(request):
    template = loader.get_template("index.html") 
    return HttpResponse(template.render())
    
def bootstrapdemo(request):
    template = loader.get_template("bootstrap.html")
    return HttpResponse(template.render())



@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')  



 
  
def form(request):  
    stu =  StdForm()  
    return render(request,"form.html",{'form':stu})   



def fuform(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"file_upload.html",{'form':student})     
    
from django.shortcuts import render  
from django.http import HttpResponse  
  
def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  

def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);   

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);   

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response  

def getemp(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    employees = Employee.objects.all()
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.eid,employee.ename,employee.econtact])  
    return response  

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello World, Javatpoint.")  
    p.showPage()   
    p.save()  
    return response   