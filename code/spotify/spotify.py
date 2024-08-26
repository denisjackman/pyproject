"""
    Spotify API example
    based on
    https://www.youtube.com/watch?v=WAmEZBEeNmg
    documentation is here
    https://developer.spotify.com/documentation/web-api
    Country code is from the list here
    https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
"""
import os
import sys
import base64
import json
from requests import post, get
# import wikipediaapi

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

SPOTIFY_SEARCH_URL = 'https://api.spotify.com/v1/'
SPOTIFY_BASE_URL = 'https://accounts.spotify.com/api/token'


def get_token(gt_id, gt_secret):
    """ get the token """
    gt_base_url = SPOTIFY_BASE_URL
    gt_auth_str = f'{gt_id}:{gt_secret}'
    gt_auth_bytes = gt_auth_str.encode('utf-8')
    gt_auth_base64 = str(base64.b64encode(gt_auth_bytes), 'utf-8')
    gt_headers = {'Authorization': f'Basic {gt_auth_base64}',
                  'Content-Type': 'application/x-www-form-urlencoded'}
    gt_data = {'grant_type': 'client_credentials'}
    gt_result = post(gt_base_url, headers=gt_headers, data=gt_data, timeout=5)
    gt_json_result = json.loads(gt_result.content)
    gt_token = gt_json_result['access_token']
    return gt_token


def get_auth_header(gat_token):
    """ get the auth header """
    gat_auth_header = {'Authorization': f'Bearer {gat_token}'}
    return gat_auth_header


def search_for_artist(gsa_token, gsa_artist):
    """ search for an artist """
    gsa_search_url = f'{SPOTIFY_SEARCH_URL}search?'
    gsa_headers = get_auth_header(gsa_token)
    gsa_search_query = f'q={gsa_artist}&type=artist&limit=1'
    gsa_query_url = f'{gsa_search_url}{gsa_search_query}'
    gsa_result = get(gsa_query_url, headers=gsa_headers, timeout=5)
    gsa_json_result = json.loads(gsa_result.content)["artists"]["items"]
    if len(gsa_json_result) == 0:
        return None
    return gsa_json_result[0]


def get_details_by_artist(gdba_token, gdba_url):
    ''' get the details by the artist '''
    gdba_headers = get_auth_header(gdba_token)
    gdba_result = get(gdba_url, headers=gdba_headers, timeout=5)
    gdba_json_result = json.loads(gdba_result.content)
    return gdba_json_result


def get_songs_by_artist(gsba_token, gsba_artist_id):
    ''' get the songs by the artist '''
    gsba_search_url = f'{SPOTIFY_SEARCH_URL}artists/{gsba_artist_id}/top-tracks?country=GB'
    gsba_headers = get_auth_header(gsba_token)
    gsba_result = get(gsba_search_url, headers=gsba_headers, timeout=5)
    gsba_json_result = json.loads(gsba_result.content)["tracks"]
    return gsba_json_result


def main():
    """ This is the main function """
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    client_id = credid["SpotifyClientID"]
    client_secret = credid["SpotifyClientSecret"]
    token = get_token(client_id, client_secret)
    result = search_for_artist(token, "Blondie")
    bresult = search_for_artist(token, "ACDC")
    cresult = search_for_artist(token, "ABloxoie")
    result_id = result["id"]
    bresult_id = bresult["id"]
    result_songs = get_songs_by_artist(token, result_id)
    print(f'[-] client_id               : {client_id}')
    print(f'[-] client_secret           : {client_secret}')
    print(f'[-] token                   : {token}')
    print(f'[-] search artist           : {result["name"]}')
    print(f'[-] link                    : {get_details_by_artist(token, result["href"])}')
    print(f'[-] search artist           : {bresult["name"]}')
    if cresult is None:
        print('[-] search artist            : Artist not found')
    else:
        print(f'[-] search artist       : {cresult["name"]}')
    print(f'[-] artist id (Blondie)     : {result_id}')
    print(f'[-] artist id (ACDC)        : {bresult_id}')
    for idx, song in enumerate(result_songs):
        print(f'[-] song {idx} (Blondie)    : {song["name"]}')


if __name__ == '__main__':
    main()
