import random
from rest_framework.views import APIView
from rest_framework.response import Response
from buildings.models import Building
from buildings.serializers import BuildingSerializer
import joblib
import pandas as pd

import joblib
import json
import pandas as pd

def transformation(text, intesity):
    json_data = json.loads(text)

    for i in range(len(json_data)):
        del json_data[i]["technical_solution_proposed"]
        del json_data[i]["address"]
        del json_data[i]["latitude"]
        del json_data[i]["longitude"]
        del json_data[i]["id"]

    df = pd.DataFrame(json_data)

    # List of possible superstructure types
    superstructure_types = [
        "adobe_mud",
        "mud_mortar_stone",
        "stone_flag",
        "cement_mortar_stone",
        "mud_mortar_brick",
        "cement_mortar_brick",
        "timber",
        "rc_non_engineered",
        "rc_engineered",
        "other"
    ]

    for structure in superstructure_types:
        df[f"has_superstructure_{structure}"] = (
            df["has_superstructure"].apply(lambda x: 1 if x == structure else 0)
        )

    df = df.drop(columns=["has_superstructure"])
    df['pred_intensity'] = intesity
    return df

preprocessor_preds_loaded = joblib.load('preprocessor_pipeline.pkl')
rf_loaded = joblib.load('random_forest_model.pkl')

preprocessor_preds_loaded = joblib.load('preprocessor_pipeline.pkl')
rf_loaded = joblib.load('random_forest_model.pkl')

def predire_damage(X_predict, intesity):
    x_new_transformed = preprocessor_preds_loaded.transform(transformation(X_predict, intesity))
    return rf_loaded.predict(x_new_transformed)

# def convert_to_dataframe(data):
#     superstructure_fields = [
#         "has_superstructure_adobe_mud",
#         "has_superstructure_mud_mortar_stone",
#         "has_superstructure_stone_flag",
#         "has_superstructure_cement_mortar_stone",
#         "has_superstructure_mud_mortar_brick",
#         "has_superstructure_cement_mortar_brick",
#         "has_superstructure_timber",
#         "has_superstructure_rc_non_engineered",
#         "has_superstructure_rc_engineered",
#         "has_superstructure_other"
#     ]
    
#     converted_data = {field: [0] for field in superstructure_fields}

#     superstructure_value = data["has_superstructure"]
#     if superstructure_value:
#         converted_data[f"has_superstructure_{superstructure_value}"] = [1]
    
#     converted_data.update({
#         "count_floors_pre_eq": [data["count_floors_pre_eq"]],
#         "age_building": [data["age_building"]],
#         "plinth_area_sq_ft": [data["plinth_area_sq_ft"]],
#         "height_ft_pre_eq": [data["height_ft_pre_eq"]],
#         "land_surface_condition": [data["land_surface_condition"]],
#         "foundation_type": [data["foundation_type"]],
#         "roof_type": [data["roof_type"]],
#         "ground_floor_type": [data["ground_floor_type"]],
#         "other_floor_type": [data["other_floor_type"]],
#         "position": [data["position"]],
#         "plan_configuration": [data["plan_configuration"]],
#         "pred_intensity": [6.5]
#     })
    
#     df = pd.DataFrame(converted_data)
#     return df


# def predict_damage_levels(total_buildings):
#     import pandas as pd

# # Creating the DataFrame with one row as described
#     data = {
#     "count_floors_pre_eq": [1],
#     "age_building": [10],
#     "plinth_area_sq_ft": [1500],
#     "height_ft_pre_eq": [30],
#     "land_surface_condition": ['Good'],
#     "foundation_type": ['Cement'],
#     "roof_type": ['Concrete'],
#     "ground_floor_type": ['Brick'],
#     "other_floor_type": ['Wood'],
#     "position": ['Central'],
#     "plan_configuration": ['Rectangular'],
#     "has_superstructure_adobe_mud": [0],
#     "has_superstructure_mud_mortar_stone": [1],
#     "has_superstructure_stone_flag": [0],
#     "has_superstructure_cement_mortar_stone": [1],
#     "has_superstructure_mud_mortar_brick": [0],
#     "has_superstructure_cement_mortar_brick": [0],
#     "has_superstructure_timber": [0],
#     "has_superstructure_rc_non_engineered": [1],
#     "has_superstructure_rc_engineered": [0],
#     "has_superstructure_other": [0],
#     "pred_intensity": [6.5]
# }

#     df = pd.DataFrame(convert_to_dataframe(data))
#     x_new_transformed = preprocessor_preds_loaded.transform(df)
#     predictions = rf_loaded.predict(x_new_transformed)

#     return predictions



# """
#  #   Column                                  Non-Null Count   Dtype  
# ---  ------                                  --------------   -----  
#  0   count_floors_pre_eq                     102844 non-null  int64  
#  1   age_building                            102844 non-null  int64  
#  2   plinth_area_sq_ft                       102844 non-null  int64  
#  3   height_ft_pre_eq                        102844 non-null  int64  
#  4   land_surface_condition                  102844 non-null  object 
#  5   foundation_type                         102844 non-null  object 
#  6   roof_type                               102844 non-null  object 
#  7   ground_floor_type                       102844 non-null  object 
#  8   other_floor_type                        102844 non-null  object 
#  9   position                                102844 non-null  object 
#  10  plan_configuration                      102844 non-null  object 
#  11  has_superstructure_adobe_mud            102844 non-null  int64  
#  12  has_superstructure_mud_mortar_stone     102844 non-null  int64  
#  13  has_superstructure_stone_flag           102844 non-null  int64  
#  14  has_superstructure_cement_mortar_stone  102844 non-null  int64  
#  15  has_superstructure_mud_mortar_brick     102844 non-null  int64  
#  16  has_superstructure_cement_mortar_brick  102844 non-null  int64  
#  17  has_superstructure_timber               102844 non-null  int64  
#  18  has_superstructure_rc_non_engineered    102844 non-null  int64  
#  19  has_superstructure_rc_engineered        102844 non-null  int64  
#  20  has_superstructure_other                102844 non-null  int64  
#  21  pred_intensity                          102844 non-null  float64
# """



class GetBuildingDataView(APIView):
    queryset = Building.objects.all()
    def get(self, request):
        # Fetch up to 20 building records from the database
        buildings = Building.objects.all()
        # Serialize building data
        serializer = BuildingSerializer(buildings, many=True)

        # Calculate statistics
        total_buildings = len(buildings)
        in_danger = 0  # Example logic
        not_in_danger = 1 - in_danger

        # Generate damage levels
        damage_levels = [0 for _ in range(total_buildings)]

        # Build response
        response_data = {
            "statistics": {
                "in_danger": round(in_danger, 2),
                "not_in_danger": round(not_in_danger, 2),
            },
            "buildings": serializer.data,
            "damage_level_predicted": damage_levels
        }

        return Response(response_data)
    

class GetBuildingPredictionDataView(APIView):
    queryset = Building.objects.all()
    def get(self, request):
        buildings = Building.objects.all()

        serializer = BuildingSerializer(buildings, many=True)

        total_buildings = len(buildings)
        print(buildings)
        in_danger = random.random()  # Example logic
        not_in_danger = 1 - in_danger

        intensity = float(request.GET.get('intensity', 5))
        print(intensity)
        damage_levels = [x + 1 for x in predire_damage(json.dumps(serializer.data), intensity)]
        in_danger = len([x for x in damage_levels if x >= 3]) / len(damage_levels)  # Example logic
        not_in_danger = 1 - in_danger

        # Build response
        response_data = {
            "statistics": {
                "in_danger": round(in_danger, 2),
                "not_in_danger": round(not_in_danger, 2),
            },
            "buildings": serializer.data,
            "damage_level_predicted": damage_levels
        }

        return Response(response_data)



