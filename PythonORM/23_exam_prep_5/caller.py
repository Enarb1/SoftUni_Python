import os
from urllib.request import parse_http_list

import django
from datetime import date, datetime

from django.db.models import Q, Count
from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match
# Create queries within functions

def populate_db():
    players_data = [
        {"full_name": "Roger Federer", "birth_date": date(1981, 8, 8), "country": "Switzerland", "ranking": 3},
        {"full_name": "Rafael Nadal", "birth_date": date(1986, 6, 3), "country": "Spain", "ranking": 2},
        {"full_name": "Novak Djokovic", "birth_date": date(1987, 5, 22), "country": "Serbia", "ranking": 1},
        {"full_name": "Andy Murray", "birth_date": date(1987, 5, 15), "country": "United Kingdom", "ranking": 10},
    ]

    players = [TennisPlayer.objects.get_or_create(**player)[0] for player in players_data]

    tournaments_data = [
        {"name": "Wimbledon", "location": "London, UK", "prize_money": 2500000.00, "start_date": date(2024, 6, 24),
         "surface_type": "Grass"},
        {"name": "Roland Garros", "location": "Paris, France", "prize_money": 2300000.00,
         "start_date": date(2024, 5, 26), "surface_type": "Clay"},
        {"name": "US Open", "location": "New York, USA", "prize_money": 3000000.00, "start_date": date(2024, 8, 26),
         "surface_type": "Hard Court"},
    ]

    tournaments = [Tournament.objects.get_or_create(**tournament)[0] for tournament in tournaments_data]

    matches_data = [
        {"score": "6-3 6-4 6-2", "summary": "Federer dominated the match with precision.",
         "date_played": timezone.now(), "tournament": tournaments[0], "winner": players[0]},
        {"score": "7-5 3-6 7-6 6-4", "summary": "Nadal claimed victory after a tough battle.",
         "date_played": timezone.now(), "tournament": tournaments[1], "winner": players[1]},
        {"score": "6-2 6-1 6-3", "summary": "Djokovic cruised to an easy win.", "date_played": timezone.now(),
         "tournament": tournaments[2], "winner": players[2]},
    ]

    for match_data in matches_data:
        match, created = Match.objects.get_or_create(
            score=match_data['score'],
            summary=match_data['summary'],
            date_played=match_data['date_played'],
            tournament=match_data['tournament'],
            winner=match_data['winner']
        )
        match.players.set(players)

    print("Database successfully populated with sample data!")

def get_tennis_players(search_name=None, search_country=None):

    if not search_name and not search_country:
        return ""

    query = Q()

    if search_name:
        query &= Q(full_name__icontains=search_name)
    if search_country:
        query &= Q(country__icontains=search_country)

    players = TennisPlayer.objects.filter(query).order_by("ranking")

    if not players.exists():
        return ""

    result = []

    for p in players:
        result.append(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}")

    return "\n".join(result)

def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if player is None:
        return ""

    return f"Top Tennis Player: {player.full_name} with {player.won_matches.count()} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(
        matches_count=Count("player_matches")).order_by("-matches_count","ranking").first()

    if not player or not Match.objects.exists():
        return ""

    return f"Tennis Player: {player.full_name} with {player.matches_count} matches played."

def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(
        surface_type__icontains=surface).annotate(
        num_matches=Count('tournament_matches')).order_by("-start_date")

    if not tournaments.exists():
        return ""

    result = []

    for t in tournaments:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}")

    return "\n".join(result)

def get_latest_match_info():
    latest_match = Match.objects.order_by('-date_played', '-id').first()

    if not latest_match:
        return ""

    players = " vs ".join(latest_match.players.order_by("full_name").values_list("full_name", flat=True))

    winner = latest_match.winner.full_name if latest_match.winner else "TBA"

    return (
        f"Latest match played on: {latest_match.date_played}, "
        f"tournament: {latest_match.tournament.name}, "
        f"score: {latest_match.score}, "
        f"players: {players}, "
        f"winner: {winner}, "
        f"summary: {latest_match.summary}")

def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None \
            or not Tournament.objects.exists() \
            or not Tournament.objects.filter(name=tournament_name).exists() \
            or not Tournament.objects.filter(name=tournament_name).prefetch_related(
        "tournament_matches").annotate(count=Count("tournament_matches")).filter(count__gt=0).exists():
        return "No matches found."

    tournament_matches = Match.objects.filter(tournament__name=tournament_name).order_by("-date_played")


    result = []

    for match in tournament_matches:
        winner = match.winner.full_name if match.winner else "TBA"
        result.append(f"Match played on: {match.date_played}, score: {match.score}, winner: {winner}")

    return "\n".join(result)
