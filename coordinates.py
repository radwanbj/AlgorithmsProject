from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="QuickDelivery")
clx_port_klang = geolocator.reverse("3.0319924887507144, 101.37344116244806")
pl_petaling_jaya = geolocator.reverse("3.112924170027219, 101.63982650389863")
gdex_batu_caves = geolocator.reverse("3.265154613796736, 101.68024844550233")
jt_kajang = geolocator.reverse("2.9441205329488325, 101.7901521759029")
dhl_sungai_buloh = geolocator.reverse("3.2127230893650065, 101.57467295692778")

print(clx_port_klang)
print(pl_petaling_jaya)
print(gdex_batu_caves)
print(jt_kajang)
print(dhl_sungai_buloh)
