from django.core.management.base import BaseCommand
from buildings.models import Building
import random

class Command(BaseCommand):
    help = "Populate the Building table with random data."

    def handle(self, *args, **kwargs):
        # Choices for model fields
        land_conditions = ['Flat', 'Moderate slope', 'Steep slope']
        foundation_types = ['Other', 'Mud mortar-Stone/Brick', 'Cement-Stone/Brick', 'RC']
        roof_types = ['Bamboo/Timber-Light roof', 'Bamboo/Timber-Heavy roof', 'RCC/RB/RBC']
        ground_floor_types = ['Mud', 'Brick/Stone', 'RC', 'Timber', 'Other']
        other_floor_types = ['Not applicable', 'TImber/Bamboo-Mud', 'Timber-Planck', 'RCC/RB/RBC']
        positions = ['Not attached', 'Attached-1 side', 'Attached-2 side', 'Attached-3 side']
        plan_configurations = [
            'Rectangular', 'L-shape', 'Square', 'T-shape', 'Multi-projected', 'H-shape',
            'U-shape', 'Others', 'E-shape', 'Building with Central Courtyard'
        ]
        technical_solutions = ['Major repair', 'Reconstruction', 'Minor repair', 'No need']
        superstructures = [
            'adobe_mud', 'mud_mortar_stone', 'stone_flag', 'cement_mortar_stone', 
            'mud_mortar_brick', 'cement_mortar_brick', 'timber', 'rc_non_engineered', 
            'rc_engineered', 'other'
        ]
        addresses = ['Zouaghi', 'Sidi Mabrouk', 'Bossof', 'Jbel El Wahch']

        # Generate 100 random building records
        for _ in range(100):
            Building.objects.create(
                count_floors_pre_eq=random.randint(1, 9),
                age_building=random.randint(0, 999),
                plinth_area_sq_ft=round(random.uniform(70, 5000), 2),
                height_ft_pre_eq=round(random.uniform(6, 99), 2),
                land_surface_condition=random.choice(land_conditions),
                foundation_type=random.choice(foundation_types),
                roof_type=random.choice(roof_types),
                ground_floor_type=random.choice(ground_floor_types),
                other_floor_type=random.choice(other_floor_types),
                position=random.choice(positions),
                plan_configuration=random.choice(plan_configurations),
                technical_solution_proposed=random.choice(technical_solutions),
                has_superstructure=random.choice(superstructures),
                address=random.choice(addresses),
                latitude=round(random.uniform(36.362, 36.368), 6),
                longitude=round(random.uniform(6.6100, 6.6180), 6)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Building table with random data.'))
