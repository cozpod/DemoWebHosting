from cgitb import html
from black import E
from django.shortcuts import render,redirect
from matplotlib.style import context
from . forms import EmployeeForm
from . models import Employee
from django.forms.models import inlineformset_factory
from .import Registerform


# Create your views here.

def Employee_list(request):
    # context['workers'] = Worker.objects.all()
    # context={'Employee_list' = Employee.objects.all()}
    context={'Employee_list':Employee.objects.all()}
    return render(request,"CRUDAPP/Employee_list.html",context)

#Form Registrations
def Regform(request):
    form = Registerform.singup()
    if request.method=='POST':
        form = Registerform.singup(request.POST)
        html = 'we have recievde this form again'
    else:
        html='Welcome for first time'
    return render(request,'CRUDAPP\signup.html',{'html':html,'form':form})


# def manage_books(request):
#     author = Author()
#     BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
#     if request.method == "POST":
#         formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect(author.get_absolute_url())
#     else:
#         formset = BookInlineFormSet(instance=author)
#     return render_to_response("manage_books.html", {
#         "formset": formset,
#     })

def Employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"CRUDAPP/Employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
            # form = EmployeeForm(request.POST, request.FILES, instance=form)
            # formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/list')
    

def Employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
