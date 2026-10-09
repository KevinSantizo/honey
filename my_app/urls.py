from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-data/', views.SendHoneyCombData.as_view(), name='send-data'),
    
    # WebSocket vital signs endpoints
    path('height/', views.SendHeightSocketMessage.as_view(), name='height'),
    path('weight/', views.SendWeightSocketMessage.as_view(), name='weight'),
    path('esfigmo/', views.SendPressureSocketMessage.as_view(), name='esfigmo'),
    path('oxygen/', views.SendOxygenSocketMessage.as_view(), name='oxygen'),
    path('temperature/', views.SendTemperatureSocketMessage.as_view(), name='temperature'),
    path('stethoscope/', views.SendEstetoSocketMessage.as_view(), name='stethoscope'),
    
    # WebSocket cabin control endpoints
    path('patient-exit/', views.SendPatientExitSocketMessage.as_view(), name='patient-exit'),
    path('activate-emergency/', views.SendActivateEmergencySocketMessage.as_view(), name='activate-emergency'),
    path('deactivate-emergency/', views.SendDeactivateEmergencySocketMessage.as_view(), name='deactivate-emergency'),
    path('take-call/', views.TakeCallSocketMessage.as_view(), name='take-call'),
    path('end-call/', views.EndCallSocketMessage.as_view(), name='end-call'),
    path('get-devices/', views.GetDiveces.as_view(), name='get-devices'),
    path('switch-derm-camera/', views.SendDermCameraSocketMessage.as_view(), name='switch-derm-camera'),
    path('open-door/', views.OpenDoorSocketMessage.as_view(), name='open-door'),
    path('close-door/', views.CloseDoorSocketMessage.as_view(), name='close-door'),
    path('turn-on-light/', views.TurnOnLightSocketMessage.as_view(), name='turn-on-light'),
    path('turn-off-light/', views.TurnOffLightSocketMessage.as_view(), name='turn-off-light'),
    path('turn-on-ventilation/', views.TurnOnVentilationSocketMessage.as_view(), name='turn-on-ventilation'),
    path('turn-off-ventilation/', views.TurnOffVentilationSocketMessage.as_view(), name='turn-off-ventilation'),
]