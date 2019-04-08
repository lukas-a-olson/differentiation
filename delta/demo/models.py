from django.db import models


class Section(models.Model):
    section_id = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.section_id)


class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    
    GENDERS = {
        ('f', "F"),
        ('m', "M")
    }
    
    gender = models.CharField(choices=GENDERS, max_length=1)
    
    RACE_ETHNICITIES = {
        ('hisp', "Hispanic/Latino"),
        ('native', "American Indian or Alaska Native"),
        ('asian', "Asian"),
        ('black', "Black or African American"),
        ('nhpi', "Native Hawaiian or Other Pacific Islander"),
        ('white', "White"),
        ('two+', "Two or more races")
    }
    
    race_ethnicity = models.CharField(choices=RACE_ETHNICITIES, max_length=100)
    sped_status = models.BooleanField()

    def __str__(self):
        return self.last_name+', '+self.first_name


class Assignment(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.FloatField(default=1.0)
    points_possible = models.IntegerField(default=100)
    
    CATEGORIES = {
        ('essay', "Essay"),
        ('nbch', "Notebook Check"),
        ('test', "Test"),
        ('quiz', "Quiz"),
        ('proj', "Project"),
        ('hmwk', "Homework"),
        ('excr', "Extra Credit")
    }
    
    category = models.CharField(choices=CATEGORIES, max_length=20)

    def __str__(self):
        return self.name


class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    points = models.FloatField()

    def __str__(self):
        return str(self.points)

    def get_percent(self):
        return self.points / self.assignment.points_possible * 100

    def get_weighted_grade(self):
        return self.get_percent() * self.assignment.weight
