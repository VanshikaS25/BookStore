from django.db import models

# Create your models here.

class Product(models.Model):
    part_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    age = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    Landfill_Waste_Saved = models.IntegerField(default=0)
    Energy_Saved = models.IntegerField(default=0)
    Remanufacturing_Potential = models.FloatField(default=0.0)
    New_Parts_Carbon_Footprint = models.IntegerField(default=0)
    Recycled_Parts_Carbon_Footprint = models.IntegerField(default=0)
    Energy_Consumption_New_Parts = models.IntegerField(default=0)
    Renewable_Material_Content = models.FloatField(default=0)
    Carbon_Footprint_Saved = models.IntegerField(default=0)
    Energy_Consumption_Saved = models.IntegerField(default=0)
    Remanufacturing_Potential = models.FloatField(default=0)
    is_Sold = models.BooleanField(default=False)
    #manufacturer = models.ForeignKey('manufacturer', on_delete=models.CASCADE)
    Percentage_recycled = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.part_name