from pygeocoder import Geocoder
import us

results = Geocoder.reverse_geocode(45.424571, -75.695661)
print us.states.lookup(results.administrative_area_level_1)