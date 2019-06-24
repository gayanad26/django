from django.shortcuts import render,redirect
from .forms import BookForms,ModelBookForms,SearchForm
from home2.models import Book
from django.utils import timezone   #to import timezone from settings.py
from django.contrib import messages

# Create your views here.
#def form_view(request):
 #   form = CustomForms()
  #  context = {
   #     "head":"Custom form created here using python",
    #    "forms":form
        
    #}
    #return render(request,'forms.html',context)

def form_view(request):
    context = None
    msg = None
    form = None
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid(): #if the form has some values
            #book = Book(name=form.cleaned_data('name'),purchase_date=form.cleaned_data('purchase_date'),genre=form.cleaned_data('genre'),author=form.cleaned_data('author'))
            book = Book.objects.create(
                name=form.cleaned_data.get('name'), 
                purchase_date=form.cleaned_data.get('pur_date'),
                #genre=form.cleaned_data.get('genre'),
                author=form.cleaned_data.get('author')
            )
            book.save()
            msg = 'Book Added Successfully'
        else:
            msg = form.errors             
    else:
        form = BookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})


def model_view(request):
    msg = ''
    
    if request.method == 'POST':
        form = ModelBookForms(request.POST)
        if form.is_valid(): #if the form has some values
            form.save()
            # book = Book(name=form.cleaned_data('name'),purchase_date=form.cleaned_data('purchase_date'),genre=form.cleaned_data('genre'),author=form.cleaned_data('author'))
            # book = Book.objects.create(
            #    name=form.cleaned_data.get('name'), 
            #    purchase_date=form.cleaned_data.get('pur_date'),
            #     genre=form.cleaned_data.get('genre'),
            #    author=form.cleaned_data.get('author')
            # )
            # book.save()
            msg = 'Book Added Successfully'
        else:
            msg = form.errors             
    else:
        form = ModelBookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})


def html_form(request):
    value=''
    if request.method == 'POST':
        value == request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        return render(request,'design.html',{'value':value})


def booksearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            book = Book.objects.filter(name__contains=q,purchase_date__lte=timezone.now)
            return render(request,'showtables.html',{'book':book,'form':SearchForm()})
    else:
        form = SearchForm()
        book = Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})


def deletebook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+' Successfully!')
    
    return redirect('/')


def editbook(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully!')
            return redirect('/')
    else:
        f = ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':f})