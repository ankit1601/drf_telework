from django.db import models


# Create your models here.
class StaffData(models.Model):
    """
    This class will create employee model
    """
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    last_updt = models.DateTimeField(auto_now_add=True)
    last_updt_by = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'staff_data_tbl'


class StaffAccountModel(models.Model):
    salary = models.IntegerField()
    account_number = models.IntegerField()
    email = models.EmailField()
    staff = models.ForeignKey(StaffData, on_delete=models.CASCADE, related_name="staff")

    class Meta:
        db_table = 'staff_ac_tbl'
