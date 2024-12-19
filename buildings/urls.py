from django.urls import path
from .views import GetBuildingDataView, GetBuildingPredictionDataView

urlpatterns = [
    path('get_building_data/', GetBuildingDataView.as_view(), name='get_building_data'),
    path('get_building_prediction_data/', GetBuildingPredictionDataView.as_view(), name='get_building_prediction_data'),

]
