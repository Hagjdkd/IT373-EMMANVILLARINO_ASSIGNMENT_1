from django.shortcuts import render

def home(request):
  return render(request, "home.html")

def about(request):
  context = {
    "name": "Emman Villarino",
    "student_id": "2023-08861",
  }
  return render(request, "about.html", context)