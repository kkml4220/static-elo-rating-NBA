import os

TEAMS = [
    'ATL', 'BKN', 'BOS', 'CHA', 'CHI',
    'CLE', 'DAL', 'DEN', 'DET', 'GSW',
    'HOU', 'IND', 'LAC', 'LAL', 'MEM',
    'MIA', 'MIL', 'MIN', 'NOP', 'NYK',
    'OKC', 'ORL', 'PHI', 'PHX', 'POR',
    'SAC', 'SAS', 'TOR', 'UTA', 'WAS'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# default I/O directory
INPUT_DIR = "input"
OUTPUT_DIR = "output"


# Game
GAME_COLUMN_DATE = "DATE"
GAME_COLUMN_HOME = "HOME"
GAME_COLUMN_AWAY = "AWAY"
GAME_COLUMN_HOME_SCORE = "HSCORE"
GAME_COLUMN_AWAY_SCORE = "ASCORE"