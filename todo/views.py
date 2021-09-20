from django.shortcuts import render ,HttpResponse ,redirect 
from todo.models import Taskdata
from django.contrib import messages
import random
import string

# Create your views here.

def taskList(request):
    if request.method == "POST":
        title= request.POST['title']
        desc= request.POST['desc']
        ins=Taskdata(TaskTitle=title , taskdesc=desc)
        ins.save()
        messages.success(request, 'your Task is being added Todo-List')

        
    return render(request,"tasks.html")
        
def taskfinal(request):
    allTasks = Taskdata.objects.all()
    #for item in allTasks:
      #  print(item.TaskTitle)
    context = {'Tasks':allTasks}

    return render(request,"tasklist.html", context)

def delete(request , Taskdata_id):
    item= Taskdata.objects.get(pk=Taskdata_id)
    item.delete()
    messages.success(request, 'your Task has been deleted successfullly')
    return redirect("tasks")

def passgen(request):
     if request.method=="POST":
        length=request.POST['length']
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        #symbols = string.punctuation
        all = lower + upper + num 
        len=int(length)
        temp = random.sample(all,len)
        password = "".join(temp)
        messages.success(request, "your password is generated !")
     else:
         password="Null"
      
     return render(request,"passgen.html",  {'password':password} )

def geoshare(request):
    return render(request,"geo.html", )