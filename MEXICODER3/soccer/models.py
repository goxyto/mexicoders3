from django.db import models

POSITIONS = (
    ("GK", "Goal Keeper"),
    ("DF", "Defender"),
    ("DF", "Defender"),
    ("MF", "Midfielder"),
    ("FW", "Forward"),
)

class League(models.Model):
    name = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    edition = models.IntegerField()
    #TODO: add more fields

    def __unicode__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length = 100)
    leagues = models.ManyToManyField(League)
    #TODO: add more fields

    def coach(self):
        """
        Returns the coach (if exist) of curren Team
        """
        try:
            return Coach.objects.get(club = self.id).full_name()
        except:
            return "No coach yet"

    def __unicode__(self):
        return self.name

class Person(models.Model):
    """
    This model will be used for reusing code for Coach and Player
    """
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    club = models.ForeignKey(Club)
    #TODO: add more fields

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.full_name()

class Coach(Person):
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    #TODO: add more fields

class Player(Person):
    rating = models.IntegerField(default = 0)
    foot = models.CharField(choices = (("R", "Right"), ("L", "Left")), max_length = 2)
    pace = models.IntegerField(default = 0)
    shooting = models.IntegerField(default = 0)
    passing = models.IntegerField(default = 0)
    dribbling = models.IntegerField(default = 0)
    defending = models.IntegerField(default = 0)
    heading = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    age = models.IntegerField(default = 0)
    position = models.CharField(help_text = "Select the best position of this player", choices = POSITIONS, max_length = 2)
    #TODO: add more fields
