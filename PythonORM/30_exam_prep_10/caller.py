import os
from datetime import date

import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions


def get_tennis_players(search_name=None, search_country=None):

    if search_name is None and search_country is None:
        return ""

    query = Q()
    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_country:
        query &= Q(country__icontains=search_country)

    t_players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not t_players.exists():
        return ""

    result = []
    for tp in t_players:
        result.append(f"Tennis Player: {tp.full_name}, country: {tp.country}, ranking: {tp.ranking}")

    return "\n".join(result)


def get_top_tennis_player():

    if not TennisPlayer.objects.all().exists():
        return ""

    top_p = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    return f"Top Tennis Player: {top_p.full_name} with {top_p.wins_count} wins."


def get_tennis_player_by_matches_count():

    if not Match.objects.all().exists() or not TennisPlayer.objects.all().exists():
        return ""

    tp = TennisPlayer.objects.annotate(matches_count=Count('matches')).order_by('-matches_count', 'ranking').first()

    return f"Tennis Player: {tp.full_name} with {tp.matches_count} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(
        surface_type__icontains=surface).annotate(
        num_matches=Count('matches')).order_by("-start_date")

    if not tournaments.exists():
        return ""

    result = []

    for t in tournaments:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}")

    return "\n".join(result)


def get_latest_match_info():
    match = Match.objects.order_by('date_played').last()

    if not match:
        return ""

    players = " vs ".join(match.players.order_by('full_name').values_list('full_name', flat=True))
    winner = match.winner or "TBA"

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {players}, "
            f"winner: {winner}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None):

    if not tournament_name:
        return "No matches found."

    tournament = Tournament.objects.filter(name=tournament_name).first()

    if not tournament or not Tournament.objects.all().exists() or not tournament.matches.exists():
        return "No matches found."

    matches = tournament.matches.order_by('-date_played')
    result = []

    for m in matches:
        winner = m.winner or "TBA"
        result.append(
            f"Match played on: {m.date_played}, "
            f"score: {m.score}, "
            f"winner: {winner}")

    return "\n".join(result)


print(get_tournaments_by_surface_type('ay'))






