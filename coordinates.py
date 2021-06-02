import googlemaps
from os import getenv
akey = getenv('API_KEY')
gmaps = googlemaps.Client(akey)

hi = "Hello, World!"

def get_best_distance(org, dest):
    courier = {'clx_port_klang': '3.0319924887507144, 101.37344116244806', 'pl_petaling_jaya': '3.112924170027219, 101.63982650389863', 'gdex_batu_caves': '3.265154613796736, 101.68024844550233',
               'jt_kajang': '2.9441205329488325, 101.7901521759029', 'dhl_sungai_buloh': '3.2127230893650065, 101.57467295692778'}
    distanceList = {}
    for i in courier:
        dist1 = gmaps.distance_matrix(org, i, region='MY')
        dist2 = gmaps.distance_matrix(i, dest, region='MY')
        element1 = dist1['rows'][0]['elements'][0]['distance']['value']
        element2 = dist2['rows'][0]['elements'][0]['distance']['value']
        x = element1 + element2
        distanceList[i] = x
    distanceList = sorted(distanceList.items(), key=lambda x: x[1])
    print(courier[distanceList[0][0]])
    return distanceList, courier[distanceList[0][0]]
