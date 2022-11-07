from django.urls import path
from product.api import views


urlpatterns = [

#     ###################### EmployeeService ###################
    path("product", views.Products),
    path("product/create", views.createProduct),
    path("product/update/<int:id>", views.updateProduct),
    path("product/<int:id>", views.getProduct),
    path("product/delete/<int:id>", views.deleteProduct),


]