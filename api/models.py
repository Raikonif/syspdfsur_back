from django.db import models


# Create your models here.
class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.SmallIntegerField()
    age = models.SmallIntegerField()

    def __str__(self):
        return f"""
        PATIENT
        ID: {self.id}
        Name and Last Name: {self.first_name} + " " + {self.last_name}
        Gender: {"Male" if self.gender == 1 else "Female"}
        Age: {self.age}
        """


class Diagnosis(models.Model):
    id: models.BigAutoField(primary_key=True)
    patient_id = models.BigIntegerField()
    medic_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    type = models.SmallAutoField()
    description = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    difficulty = models.SmallIntegerField()
    part_of_body = models.CharField(max_length=50)

    def __str__(self):
        return f"""
        DIAGNOSIS
        ID: {self.id}
        Patient ID: {self.patient_id}
        Name: {self.name}
        Type: {"Histopatology" if self.type == 1 else "Citology" if self.type == 3 else "PAP"}
        Description: {self.description}
        Diagnosis: {self.diagnosis}
        Difficulty: {"Easy" if self.difficulty == 1 else "Medium" if self.difficulty == 3 else "Hard"}
        Part of Body: {self.part_of_body}
        """


class SubDiagnosis(models.Model):
    id = models.BigAutoField(primary_key=True)
    diagnosis_id = models.BigIntegerField()
    name = models.CharField(max_length=50)


class Histopatology(SubDiagnosis):
    description = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)


class Citology(SubDiagnosis):
    type_of_cell = models.CharField(max_length=50)
    validation = models.SmallIntegerField()


class PAP(SubDiagnosis):
    type_of_result = models.CharField(max_length=50)
    recept = models.SmallIntegerField()


class Medic(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"""
        MEDIC
        ID: {self.id}
        Name and Last Name: {self.first_name} + " " + {self.last_name}
        """


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.SmallIntegerField()
