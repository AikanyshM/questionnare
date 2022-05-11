from django.contrib import admin
from django.urls import path, include
from question import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('question', views.QuestionViewSet, basename='question')
router.register('answer', views.AnswerViewSet, basename='answer')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', views.AdminUserCreateAPIView.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('register/', views.UserCreateAPIView.as_view()),
    path('get-token/', obtain_auth_token),
    path('', include(router.urls)), 
    path('result/', views.ResultListCreateAPIView.as_view(), name="result"),
    

]
