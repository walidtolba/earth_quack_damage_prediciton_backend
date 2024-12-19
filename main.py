import joblib
import json
import pandas as pd

def transformation(text):
    print(text)
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
    df['pred_intensity'] = 6.5
    return df

preprocessor_preds_loaded = joblib.load('preprocessor_pipeline.pkl')
rf_loaded = joblib.load('random_forest_model.pkl')

preprocessor_preds_loaded = joblib.load('preprocessor_pipeline.pkl')
rf_loaded = joblib.load('random_forest_model.pkl')

def predire_damage(X_predict):
    x_new_transformed = preprocessor_preds_loaded.transform(transformation(X_predict))
    return rf_loaded.predict(x_new_transformed)
    
y_new_pred = predire_damage("""
      [{"id": 1,
      "count_floors_pre_eq": 1,
      "age_building": 493,
      "plinth_area_sq_ft": 3847.45,
      "height_ft_pre_eq": 37.93,
      "land_surface_condition": "Flat",
      "foundation_type": "RC",
      "roof_type": "Bamboo/Timber-Light roof",
      "ground_floor_type": "Mud",
      "other_floor_type": "TImber/Bamboo-Mud",
      "position": "Attached-3 side",
      "plan_configuration": "Rectangular",
      "technical_solution_proposed": "Reconstruction",
      "has_superstructure": "stone_flag",
      "address": "789 Oak St",
      "latitude": 36.367641,
      "longitude": 6.612864}]
    """)

print(y_new_pred)