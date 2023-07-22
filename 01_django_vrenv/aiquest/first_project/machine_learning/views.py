from django.shortcuts import render
from django.http import HttpResponse as hr

# Create your views here.
def machine(request):
    course = '(Machine Learning) From Study Mart '
    total_class = 25
    total_seat = 52
    course_duration = '14 month'
    teacher = ['saiful', 'jakir', 'shimul', 'sagor']
    
    # dictionary variable 
    t_details = {'what': 'Machine Learning dictionary',
                 'course': course, 
                 'tc': total_class, 
                 'st': total_seat, 
                 'cd': course_duration,
                 'teacher': teacher}
    
    
    return render(request,'machine_learning/machine_learning.html',
                  context= t_details)

def random(request):
    return render(request,'machine_learning/random_forest.html')

def dtree(request):
    return render(request,'machine_learning/dtree.html')

def knn(request):
    return render(request,'machine_learning/knn.html')
