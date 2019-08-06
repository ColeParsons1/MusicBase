from __future__ import unicode_literals

from django.db import models


#DO NOT CHANGE ANY CODE ON THIS PAGE
#DO NOT CHANGE ANY CODE ON THIS PAGE
#DO NOT CHANGE ANY CODE ON THIS PAGE


class Artist(models.Model):
    Name = models.CharField(max_length=500)
    Stage_Name = models.CharField(max_length=250)
    Also_Known_As = models.CharField(max_length=250)
    Band_Members = models.CharField(max_length=500)
    Nationality = models.CharField(max_length=250)
    Birth_Date = models.CharField(max_length=250)
    Death_Date = models.CharField(max_length=250, blank=True)
    Star_Sign = models.CharField(max_length=25, blank=True)
    Currently = models.CharField(max_length=50, blank=True)
    Genre = models.CharField(max_length=1000)
    Bio = models.TextField(max_length=10000, blank=True)
    Artist_Image = models.FileField()
    Official_Website = models.CharField(max_length=500, blank=True)
    Spotify_Link = models.CharField(max_length=500, blank=True)
    Apple_Music = models.CharField(max_length=500, blank=True)
    SoundCloud_Link = models.CharField(max_length=500, blank=True)
    Bandcamp = models.CharField(max_length=500, blank=True)
    Twitter_Link = models.CharField(max_length=500, blank=True)
    Awards = models.CharField(max_length=500, blank=True)
    Contributions = models.CharField(max_length=50, blank=True)
    Personal_Quoute = models.TextField(max_length=1000, blank=True)
    Other_Notes = models.TextField(max_length=100, blank=True)
    Info_Sources = models.CharField(max_length=10000)
    
    
class Album(models.Model):
    Album_Name = models.CharField(max_length=500)
    Album_Image = models.FileField()
    Album_Artist = models.CharField(max_length=500)
    Album_Release_Date = models.CharField(max_length=500)
    Album_Primary_Genre = models.CharField(max_length=500)
    Album_Secondary_Genre = models.CharField(max_length=500)
    Album_Spotify_Link = models.CharField(max_length=500)
    Other_Album_Info = models.TextField(max_length=10000, blank=True)
    Language = models.CharField(max_length=500)
    Descriptors = models.CharField(max_length=500, blank=True)
    Track_1 = models.CharField(max_length=500)
    Track_2 = models.CharField(max_length=500)
    Track_3 = models.CharField(max_length=500)
    Track_4 = models.CharField(max_length=500, blank=True)
    Track_5 = models.CharField(max_length=500, blank=True)
    Track_6 = models.CharField(max_length=500, blank=True)
    Track_7 = models.CharField(max_length=500, blank=True)
    Track_8 = models.CharField(max_length=500, blank=True)
    Track_9 = models.CharField(max_length=500, blank=True)
    Track_10 = models.CharField(max_length=500, blank=True)
    Track_11 = models.CharField(max_length=500, blank=True)
    Track_12 = models.CharField(max_length=500, blank=True)
    Track_13 = models.CharField(max_length=500, blank=True)
    Track_14 = models.CharField(max_length=500, blank=True)
    Track_15 = models.CharField(max_length=500, blank=True)
    Track_16 = models.CharField(max_length=500, blank=True)
    Track_17 = models.CharField(max_length=500, blank=True)
    Track_18 = models.CharField(max_length=500, blank=True)
    Track_19 = models.CharField(max_length=500, blank=True)
    Track_20 = models.CharField(max_length=500, blank=True)
    Track_21 = models.CharField(max_length=500, blank=True)
    Track_22 = models.CharField(max_length=500, blank=True)
    Track_23 = models.CharField(max_length=500, blank=True)
    Track_24 = models.CharField(max_length=500, blank=True)
    Track_25 = models.CharField(max_length=500, blank=True)
    Track_26 = models.CharField(max_length=500, blank=True)
    Track_27 = models.CharField(max_length=500, blank=True)
    Track_28 = models.CharField(max_length=500, blank=True)
    Track_29 = models.CharField(max_length=500, blank=True)
    Track_30 = models.CharField(max_length=500, blank=True)
    Credits = models.CharField(max_length=500, blank=True)
    Awards = models.CharField(max_length=500, blank=True)
    Info_Sources = models.CharField(max_length=10000)
    
class Genre(models.Model):
    Genre_Name = models.CharField(max_length=500)
    Genre_History = models.TextField(max_length=10000, blank=True)
    Major_Influential_Albums = models.TextField(max_length=10000, blank=True)
    Major_Influential_Artists = models.CharField(max_length=500)
    Minor_Influential_Artists = models.CharField(max_length=500, blank=True)
    Info_Sources = models.CharField(max_length=10000)
    
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()   
    