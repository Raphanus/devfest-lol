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

def get_challengers(region="NA", queuetype="RANKED_SOLO_5x5"):
    """
    queuetype can be RANKED_TEAM_5x5 and RANKED_TEAM_3x3 too.
    """
    js = get_challenger_league_tiers(region,queuetype)
    return js

def get_all_challengers(region="NA"):
    queues = ["RANKED_SOLO_5X5",
            "RANKED_TEAM_5X5"]
    l_js = []
    for q in queues:
        l_js.append(get_challengers(region,q))
    pprint(l_js)

if __name__ == "__main__":
    #pprint(rec_gms_to_kda('lexwraith'))
    #pprint(ranked_stats("lexwraith"))
    g =  get_all_challengers()
