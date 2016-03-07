import json
import urllib2
import urllib
from google_polyline import *
import os
import api_keys

latlongs = [
# "40.458205 -79.925149",
# "40.465114 -79.957918",
# "40.487383 -79.918095",
# "40.488460 -79.936987",
# "40.503493 -79.947302",
# "40.488425 -79.937058",
# "40.486098 -79.913657",
# "40.471170 -79.908542",
# "40.465030 -79.919971",
# "40.463495 -79.930695",
# "40.465136 -79.957993",
# "40.458434 -79.965325",
# "40.488433 -79.937158",
# "40.488250 -79.925538",
# "40.507657 -79.946092",
# "40.497797 -79.943858",
# "40.491038 -79.957189",
# "40.484919 -79.971895"
"40.495470 -79.976233",
"40.504807 -79.969301",
"40.513746 -79.968041",
"40.516300 -79.974404",
"40.524550 -79.983125",
"40.535425 -79.977279",
"40.503490 -79.947289",
"40.583927 -79.881738",
"40.600822 -79.870779",
"40.607128 -79.850441",
"40.611769 -79.835263",
"40.623741 -79.832541",
"40.632406 -79.823185",
"40.649100 -79.797872",
"40.656498 -79.785616"
]

# Concatenates encoded polylines together.
def concat_polylines(polylines):
    line_coords = []
    for line in polylines:
        if(line_coords == []):
            line_coords += decode(line)
        else:
            line_coords += decode(line)[1:]

    return encode_coords(line_coords)

polylines = []

for i in range(len(latlongs)-1):
    start_addr = latlongs[i]
    end_addr = latlongs[i+1]

    # Get directions
    url = ("https://maps.googleapis.com/maps/api/directions/json?" +
    "origin=%s&destination=%s&avoid=highways&mode=walking&key=%s" % 
    (urllib2.quote(start_addr), urllib2.quote(end_addr), api_keys.google_key))

    data = json.load(urllib2.urlopen(url))
    polylines.append(data['routes'][0]['overview_polyline']['points'])

# Write end of day data to file for displaying.
data_file = open("recreated.txt", 'w')
data_file.write(concat_polylines(polylines))
data_file.close()
    
