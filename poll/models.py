from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BoothData2014(models.Model):
    polling_booth_number = models.IntegerField(primary_key=True)
    polling_booth_name = models.CharField(max_length=255)
    winner_2014 = models.CharField(max_length=255)
    first_runner_up_other_than_INC_and_BJP = models.CharField(
        max_length=255, blank=True, null=True
    )
    margin_percent = models.FloatField(blank=True, null=True)
    margin = models.CharField(blank=True, null=True, max_length=5)
    total = models.IntegerField(blank=True, null=True)
    BJP_votes = models.IntegerField(blank=True, null=True)
    BJP_percent_vote = models.FloatField(blank=True, null=True)
    INC_votes = models.IntegerField(blank=True, null=True)
    INC_percent_votes = models.FloatField(blank=True, null=True)
    Dadarao_Kisansro_Uikey = models.IntegerField(blank=True, null=True)
    Deashmukh_Nilesh_Madhukarrao = models.IntegerField(blank=True, null=True)
    Sandeep_Dilip_Kale = models.IntegerField(blank=True, null=True)
    Prashant_Gokuldasji_Kathane = models.IntegerField(blank=True, null=True)
    Dnyaneshwar_Narayan_Maddavi = models.IntegerField(blank=True, null=True)
    Arvind_Shamrao_Lillore = models.IntegerField(blank=True, null=True)
    Arun_Ajabrao_Pachare = models.IntegerField(blank=True, null=True)
    Topale_Rupchand_Bhuraji = models.IntegerField(blank=True, null=True)
    Tarachand_Sonbaji_Nehare = models.IntegerField(blank=True, null=True)
    Dilip_Shamraoji_Potfode = models.IntegerField(blank=True, null=True)
    Nikose_Wasudeo_Shamrao = models.IntegerField(blank=True, null=True)
    Sanjay_Dhondbaji_Tule = models.IntegerField(blank=True, null=True)
    wapnil_Alias_Bala_Rameshrao_Jagtap = models.IntegerField(blank=True, null=True)
    NOTA = models.IntegerField(blank=True, null=True)
    no_of_tendered_votes = models.CharField(blank=True, null=True, max_length=5)
    no_of_votes_gotten_by_3rd_parties = models.IntegerField(blank=True, null=True)


class BoothData2019(models.Model):
    polling_booth_number = models.IntegerField(primary_key=True)
    polling_booth_name = models.CharField(max_length=255)
    winner_2019 = models.CharField(max_length=255)
    margin_percent = models.FloatField()
    margin = models.IntegerField()
    total_voters = models.IntegerField()
    BJP_votes = models.IntegerField()
    BJP_percent_votes = models.CharField(max_length=10, null=True, blank=True)
    INC_votes = models.IntegerField()
    INC_percent_votes = models.CharField(max_length=10, null=True, blank=True)
    Adv_Chandrashekar_Dongre = models.IntegerField()
    Topale_Rupachand = models.IntegerField()
    Rahul_Parasanji_Tayde = models.IntegerField()
    Sanjay_Ambadas_Wankhede = models.IntegerField()
    Avinash_Suresh_Badhiye = models.IntegerField()
    Deepak_M_Madavi = models.IntegerField()
    Dilip_Shamraoji_Potfode = models.IntegerField()
    Vilas_Vinayakrao_Kailuke = models.IntegerField()
    NOTA = models.IntegerField()
    no_of_votes_got_by_3rd_parties = models.IntegerField()
    BJP_booth_strength = models.CharField(max_length=255)
    INC_booth_strength = models.CharField(max_length=255)
