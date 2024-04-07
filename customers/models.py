from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string
from django.contrib.staticfiles.templatetags.staticfiles import static

class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    
    BLOOD_CHOICES = [
        ("A+", "A+"),
        ("B+", "B+"),
        ("AB+", "AB+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("AB-", "AB-"),
    ]
    
    SESSION_CHOICES = [
        ("1998-1999", "1998"),
        ("1999-2000", "1999"),
        ("2000-2001", "2000"),
        ("2001-2002", "2001"),
        ("2002-2003", "2002"),
        ("2003-2004", "2003"),
        ("2004-2005", "2004"),
        ("2005-2006", "2005"),
        ("2006-2007", "2006"),
        ("2007-2008", "2007"),
        ("2008-2009", "2008"),
        ("2009-2010", "2009"),
        ("2010-2011", "2010"),
        ("2011-2012", "2011"),
        ("2012-2013", "2012"),
        ("2013-2014", "2013"),
        ("2014-2015", "2014"),
        ("2015-2016", "2015"),
        ("2016-2017", "2016"),
        ("2017-2018", "2017"),
        ("2018-2019", "2018"),
        ("2019-2020", "2019"),
        ("2020-2021", "2020"),
        ("2021-2022", "2021"),
        ("2022-2023", "2022"),
        ("2023-2024", "2023"),
        ("2024-2025", "2024"),
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="customers/profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    father = models.CharField(max_length=30, null=True, blank=True)
    mother = models.CharField(max_length=30, null=True, blank=True)
    blood = models.CharField(max_length=3, choices=BLOOD_CHOICES, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    work = models.CharField(max_length=255, null=True, blank=True)
    work_sector = models.CharField(max_length=255, null=True, blank=True)
    work_address = models.CharField(max_length=255, null=True, blank=True)
    session = models.CharField(max_length=30, choices=SESSION_CHOICES, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def generate_default_password():
        return get_random_string(length=12)

    password = models.CharField(max_length=128, default=generate_default_password)
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return static('assets/img/team/default-profile-picture.png')






class Gallery(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to="customers/gallery/", null=True, blank=True)

class Faculty(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="customers/profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return static('assets/img/team/default-profile-picture.png')
