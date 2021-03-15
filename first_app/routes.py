from django.urls import path
from . import views

urlpatterns = [
#  / - redirects to the "/blogs" route with a method called "root"
    path('', views.root),
#  /blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
    path('blogs', views.index),
#  /blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
    path('blogs/new', views.new),
#  /blogs/create - redirect to the "/" route with a method called "create"
    path('blogs/create', views.create),
#  /blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')
    path('blogs/<int:number>', views.show),
#  /blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
    path('blogs/<int:number>/edit', views.edit),
#  /blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"
    path('blogs/<int:number>/delete', views.destroy),
#  (**Bonus**) /blogs/json - return a JsonResponse with title and content keys.
    path('blogs/json', views.json)
]
