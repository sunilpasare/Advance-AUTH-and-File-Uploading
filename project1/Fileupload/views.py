from django.shortcuts import render,redirect
from .models import Document
from .forms import DocumentForm

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form= DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=DocumentForm()
    return render(request,'Fileupload/newfileupload.html',{
        'form':form
    })

def showfileview(request):
    file=Document.objects.all()
    template_name='Fileupload/showfile.html'
    context={'file':file}
    return render(request,template_name,context)
 