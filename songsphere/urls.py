from django.urls import path


from . import views

urlpatterns = [
path('index/',views.index,name='Home'),
    path('english/',views.English,name='English'),
    path('english/<int:id>',views.songpost,name='songpost'),
path('telugu/',views.Telugu,name='Telugu'),
path('telugu/<int:id>',views.songpost,name='songpost'),
path('hindi/',views.Hindi,name='Hindi'),
path('hindi/<int:id>',views.songpost,name='songpost'),
path('pop/',views.Pop,name='Pop'),
path('pop/<int:id>',views.songpost,name='songpost'),
path('rock/',views.Rock,name='Rock'),
path('rock/<int:id>',views.songpost,name='songpost'),
path('melody/',views.Melody,name='Melody'),
path('melody/<int:id>',views.songpost,name='songpost'),

path('login',views.login,name='Login'),
path('register', views.register, name='Register')
]