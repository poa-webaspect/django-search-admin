from django.db import models

import re 

class Company(models.Model):
    personal_number = models.CharField(max_length=11)
    
    def __str__(self):
        return self.personal_number
        
class VacancyManager(models.Manager):

    def filter_by_personal_number(self, personal_number):
       m = re.match(r"(?P<company_number>.{2}\d+)-(?P<vacancy_number>\d+)", personal_number)
       if m:
           return self.get_queryset().filter(
               personal_number=int(m.group('vacancy_number')),
               owner__personal_number=m.group('company_number')
           )
       else:
           return self.none()
           
class Vacancy(models.Model):
    owner = models.ForeignKey(Company)
    personal_number = models.PositiveIntegerField()
    
    objects = VacancyManager()
    
    def __str__(self):
        return '%s-%d' % (self.owner.personal_number, self.personal_number)
    
    def get_personal_number(self):
        return "{}-{}".format(self.owner.personal_number, self.personal_number)
