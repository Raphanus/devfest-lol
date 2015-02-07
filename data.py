from rawpi import *
from pprint import pprint

def rec_gms_to_kda(region,summoner):
    """
    Returns list of (k,d,a) tuples of last 10 games.
    """
    js = get_recent_games(region,summoner).json()
    kdas = []
    target = js['games']
    for game in target:
        stats = game['stats']
        kdas.append((stats['championsKilled'],
                stats['numDeaths'],
                stats['assists']))

    return kdas


if __name__ == "__main__":
    pprint(rec_gms_to_kda('NA', 'lexwraith'))
