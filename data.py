from rawpi import *
from pprint import pprint
import json

def rec_gms_to_kda(summoner, region="na"):
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

    return json.dumps(kdas)

def ranked_stats(summoner, region="NA", season="SEASON2014"):
    js = get_ranked_stats(region, summoner, season)
    return js 

if __name__ == "__main__":
    #pprint(rec_gms_to_kda('lexwraith'))
    pprint(ranked_stats("lexwraith"))
