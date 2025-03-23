from Frutipedia.fruitipediaApp import views
from django.urls import path, include

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.CreateFruitView.as_view(), name='create_fruit'),
    path('create-category/', views.create_category_view, name='create_category'),
    path('<int:pk>/', include([
        path('edit-fruite/',views.edit_view, name='edit_fruit' ),
        path('delete-fruite/',views.DeleteFruitView.as_view(), name='delete_fruit' ),
        path('details-fruit/',views.details_view, name='details_fruit'),
    ]))
)