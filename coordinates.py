import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDwySV8Ondv-FG-Eoew561u2mwl3MEEt0I')
customer = {1 : {'origin' : '3.3615395462207878,101.56318183511695', 'destination': '3.1000170516638885,101.53071480907951'}, 2 : {'origin' : '3.049398375759954,101.58546611160301', 'destination': '3.227994355250716,101.42730357605375'}, 3 : {'origin' : '3.141855957281073,101.76158583424586', 'destination': '2.9188704151716256,101.65251821655471'}}

def get_best_distance(org, dest):
    courier = {'clx_port_klang' : '3.0319924887507144, 101.37344116244806', 'pl_petaling_jaya' : '3.112924170027219, 101.63982650389863', 'gdex_batu_caves' : '3.265154613796736, 101.68024844550233', 'jt_kajang' : '2.9441205329488325, 101.7901521759029', 'dhl_sungai_buloh' : '3.2127230893650065, 101.574672956927783.2127230893650065, 101.57467295692778'}
    distanceList = {}
    for i in courier:
        dist1 = gmaps.distance_matrix(org, i, region='MY')
        dist2 = gmaps.distance_matrix(i, dest, region='MY')
        element1 = dist1['rows'][0]['elements'][0]['distance']['value']
        element2 = dist2['rows'][0]['elements'][0]['distance']['value']
        x = element1 + element2
        distanceList[i] = x

    print(distanceList)
    key_min = min(distanceList.keys(), key=(lambda k: distanceList[k]))
    print('Minimum Value: ',distanceList[key_min])
    print("\n")
   
get_best_distance(customer[1]['origin'], customer[1]['destination'])