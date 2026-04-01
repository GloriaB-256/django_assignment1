from django.shortcuts import redirect, render
from student_app.models import Student

# Create your views here.
def homepage(request):
    
    all_students = Student.objects.all()
    context = {
        "students": all_students
    }

    return render(request, "index.html", context)

def addpage(request):
    if request.method == "POST":
        body = request.POST
        s_name = body.get("name")
        s_gender = body.get("gender")
        s_dob = body.get("dob")
        s_stream = body.get("stream")
        s_student_id = body.get("student_id")
        s_is_present = body.get("is_present")
        # converted from string to boolean
        if s_is_present == "True":
            s_is_present = True
        else:
            s_is_present = False
        s_date = body.get("date")

        new_student = Student(
            name = s_name,
            gender = s_gender,
            dob = s_dob,
            stream = s_stream,
            student_id = s_student_id,
            is_present = s_is_present,
            date = s_date,
        )

        new_student.save()
        return redirect("/")  

    return render(request, 'add.html')

def viewpage(request, student_id):
    selected_student = Student.objects.get(pk=student_id)
    context = {
        "student": selected_student
    }
    return render(request, "view.html", context)

def deletepage(request, student_id):
    selected_student = Student.objects.get(pk=student_id)
    
    if request.method == "POST":

        selected_student.delete()
        
        return redirect("/")
    
    context = {
        "student": selected_student
    }
    return render(request, "delete.html", context)

def editpage(request, student_id):
    selected_student = Student.objects.get(id=student_id)
    if request.method == "POST":
        body = request.POST
        s_name = body.get("name")
        s_gender = body.get("gender")
        s_dob = body.get("dob")
        s_stream = body.get("stream")
        s_student_id = body.get("student_id")
        s_is_present = body.get("is_present")
        # converted from string to boolean
        if s_is_present == "True":
            s_is_present = True
        else:
            s_is_present = False
        s_date = body.get("date")
        selected_student.name = s_name
        selected_student.gender = s_gender
        selected_student.dob = s_dob
        selected_student.stream = s_stream
        selected_student.student_id = s_student_id
        selected_student.is_present = s_is_present
        selected_student.date = s_date
        selected_student.save()
        return redirect("/")


    context = {
        "student": selected_student
    }
    return render (request, "edit.html", context)
