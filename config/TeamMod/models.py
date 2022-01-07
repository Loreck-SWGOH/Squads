from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class GearLevels(models.Model):
    level = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ModSets(models.Model):
    SWGOHPk = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ModStats(models.Model):
    statID = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    divisor = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Mods(models.Model):
    modID = models.CharField(primary_key=True, max_length=50)
    slot = models.PositiveIntegerField()
    dots = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    set = models.ForeignKey(ModSets, on_delete=models.CASCADE)
    primaryStatType = models.ForeignKey(ModStats, on_delete=models.CASCADE,
                                        related_name='primaryStatModSet')
    primaryStatValue = models.PositiveIntegerField()
    secondaryStat1Type = models.ForeignKey(ModStats, on_delete=models.CASCADE, null=True,
                                        related_name='secondaryStat1ModSet')
    secondaryStat1Value = models.PositiveIntegerField()
    secondaryStat2Type = models.ForeignKey(ModStats, on_delete=models.CASCADE, null=True,
                                        related_name='secondaryStat2ModSet')
    secondaryStat2Value = models.PositiveIntegerField()
    secondaryStat3Type = models.ForeignKey(ModStats, on_delete=models.CASCADE, null=True,
                                        related_name='secondaryStat3ModSet')
    secondaryStat3Value = models.PositiveIntegerField()
    secondaryStat4Type = models.ForeignKey(ModStats, on_delete=models.CASCADE, null=True,
                                        related_name='secondaryStat4ModSet')
    secondaryStat4Value = models.PositiveIntegerField()


class Players(models.Model):
    allyCode = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Characters(models.Model):
    SWGOHPk = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HasActivated_EquippedWith(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    gearLevel = models.ForeignKey(GearLevels, on_delete=models.CASCADE)
    numOfGear = models.PositiveIntegerField()
    modSlot1 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot1ActivatedSet')
    modSlot2 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot2ActivatedSet')
    modSlot3 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot3ActivatedSet')
    modSlot4 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot4ActivatedSet')
    modSlot5 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot5ActivatedSet')
    modSlot6 = models.ForeignKey(Mods, on_delete=models.CASCADE,
                                related_name='modSlot6ActivatedSet')
    
    class Meta:
        unique_together = (("player", "character"),)
