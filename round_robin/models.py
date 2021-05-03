from django.db import models

# Create your models here.


class Competitor(models.Model):
    name = models.CharField(max_length=200)


class Tournament(models.Model):
    description = models.CharField(max_length=200)


class TournamentCompetitor(models.Model):
    id_competitor = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    id_tournament = models.ForeignKey(Competitor, on_delete=models.CASCADE)


class TournamentRound(models.Model):
    id_tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    winner_points = models.IntegerField()
    looser_points = models.IntegerField()


class Match(models.Model):
    description = models.CharField(max_length=200)
    id_winner = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    winner_points = models.IntegerField()
    looser_points = models.IntegerField()


class CompetitorMatch(models.Model):
    id_competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    id_match = models.ForeignKey(Match, on_delete=models.CASCADE)
