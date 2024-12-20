from django.shortcuts import render

# Create your views here.
from myapp.forms import Feedbackform
# Create your views here.
def formview(request):
    f = Feedbackform()
    if (request.method == "POST"):
        f =Feedbackform(request.POST  )
        if f.is_valid():

            name = f.cleaned_data['name']
            id = f.cleaned_data['id']
            email = f.cleaned_data['email']
            dept = f.cleaned_data['dept']
            batch = f.cleaned_data['batch']
            feedback = f.cleaned_data['feedback']
            d= {'name':name,'id':id,'email':email,'dept':dept,'batch':batch,'feedback':feedback}
            return render(request,'htmlpages/output.html',d)
    d={'form':f}
    return render(request,'htmlpages/input.html',d)
