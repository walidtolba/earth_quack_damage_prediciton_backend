from django.db import models

class Building(models.Model):
    # Integer fields with constraints
    count_floors_pre_eq = models.PositiveSmallIntegerField(
        verbose_name="Number of Floors Before Earthquake",
        choices=[(i, str(i)) for i in range(1, 10)],
        help_text="Number of floors ranging from 1 to 9."
    )
    age_building = models.PositiveSmallIntegerField(
        verbose_name="Building Age",
        help_text="Building age in years (0 to 999).",
    )
    
    # Float fields with constraints
    plinth_area_sq_ft = models.FloatField(
        verbose_name="Plinth Area (sq. ft.)",
        help_text="Plinth area in square feet (70 to 5000).",
    )
    height_ft_pre_eq = models.FloatField(
        verbose_name="Height Before Earthquake (ft)",
        help_text="Building height in feet (6 to 99).",
    )

    # Char fields with choices
    LAND_SURFACE_CHOICES = [
        ('Flat', 'Flat'),
        ('Moderate slope', 'Moderate slope'),
        ('Steep slope', 'Steep slope'),
    ]
    land_surface_condition = models.CharField(
        max_length=20,
        choices=LAND_SURFACE_CHOICES,
        verbose_name="Land Surface Condition",
    )

    FOUNDATION_TYPE_CHOICES = [
        ('Other', 'Other'),
        ('Mud mortar-Stone/Brick', 'Mud mortar-Stone/Brick'),
        ('Cement-Stone/Brick', 'Cement-Stone/Brick'),
        ('RC', 'RC'),
    ]
    foundation_type = models.CharField(
        max_length=30,
        choices=FOUNDATION_TYPE_CHOICES,
        verbose_name="Foundation Type",
    )

    ROOF_TYPE_CHOICES = [
        ('Bamboo/Timber-Light roof', 'Bamboo/Timber-Light roof'),
        ('Bamboo/Timber-Heavy roof', 'Bamboo/Timber-Heavy roof'),
        ('RCC/RB/RBC', 'RCC/RB/RBC'),
    ]
    roof_type = models.CharField(
        max_length=30,
        choices=ROOF_TYPE_CHOICES,
        verbose_name="Roof Type",
    )

    GROUND_FLOOR_CHOICES = [
        ('Mud', 'Mud'),
        ('Brick/Stone', 'Brick/Stone'),
        ('RC', 'RC'),
        ('Timber', 'Timber'),
        ('Other', 'Other'),
    ]
    ground_floor_type = models.CharField(
        max_length=20,
        choices=GROUND_FLOOR_CHOICES,
        verbose_name="Ground Floor Type",
    )

    OTHER_FLOOR_CHOICES = [
        ('Not applicable', 'Not applicable'),
        ('TImber/Bamboo-Mud', 'TImber/Bamboo-Mud'),
        ('Timber-Planck', 'Timber-Planck'),
        ('RCC/RB/RBC', 'RCC/RB/RBC'),
    ]
    other_floor_type = models.CharField(
        max_length=30,
        choices=OTHER_FLOOR_CHOICES,
        verbose_name="Other Floor Type",
    )

    POSITION_CHOICES = [
        ('Not attached', 'Not attached'),
        ('Attached-1 side', 'Attached-1 side'),
        ('Attached-2 side', 'Attached-2 side'),
        ('Attached-3 side', 'Attached-3 side'),
    ]
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        verbose_name="Position",
    )

    PLAN_CONFIGURATION_CHOICES = [
        ('Rectangular', 'Rectangular'),
        ('L-shape', 'L-shape'),
        ('Square', 'Square'),
        ('T-shape', 'T-shape'),
        ('Multi-projected', 'Multi-projected'),
        ('H-shape', 'H-shape'),
        ('U-shape', 'U-shape'),
        ('Others', 'Others'),
        ('E-shape', 'E-shape'),
        ('Building with Central Courtyard', 'Building with Central Courtyard'),
    ]
    plan_configuration = models.CharField(
        max_length=50,
        choices=PLAN_CONFIGURATION_CHOICES,
        verbose_name="Plan Configuration",
    )

    TECHNICAL_SOLUTION_CHOICES = [
        ('Major repair', 'Major repair'),
        ('Reconstruction', 'Reconstruction'),
        ('Minor repair', 'Minor repair'),
        ('No need', 'No need'),
    ]
    technical_solution_proposed = models.CharField(
        max_length=20,
        choices=TECHNICAL_SOLUTION_CHOICES,
        verbose_name="Proposed Technical Solution",
    )

    HAS_SUPERSTRUCTURE_CHOICES = [
        ('adobe_mud', 'Adobe Mud'),
        ('mud_mortar_stone', 'Mud Mortar Stone'),
        ('stone_flag', 'Stone Flag'),
        ('cement_mortar_stone', 'Cement Mortar Stone'),
        ('mud_mortar_brick', 'Mud Mortar Brick'),
        ('cement_mortar_brick', 'Cement Mortar Brick'),
        ('timber', 'Timber'),
        ('rc_non_engineered', 'RC Non-Engineered'),
        ('rc_engineered', 'RC Engineered'),
        ('other', 'Other'),
    ]
    has_superstructure = models.CharField(
        max_length=30,
        choices=HAS_SUPERSTRUCTURE_CHOICES,
        verbose_name="Has Superstructure",
    )

    # Address and location fields
    address = models.TextField(verbose_name="Address")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    def __str__(self):
        return f"{self.address} - {self.latitude}, {self.longitude}"
