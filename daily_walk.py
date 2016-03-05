import json
import urllib2
import urllib
import random
from google_polyline import *
from time import sleep, strftime
import os
import math
import api_keys
import twitter_api

# Tweets to twitter if True, prints to console if false
TWEET_ON = True
SLEEP_ON = True


# Rough maximum distance to travel per tweet. 
MAX_DISTANCE = 1000

# Number of hours to travel each day.
NUM_HOURS = 8

# Where to write the encoded polyline at the end of the day
DATA_FILE_PATH = "/var/www/html/walker"

# Number of times to retry any action if it fails for some random reason
NUM_TRIES = 3

# Minimum angle between previous bearing and new bearing in degrees.
MIN_ANGLE = 70

# Uses google's geocoding API to get a human readable address from (lat,long)
def address_from_latlng(lat, lng):
    url = ("https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s" % 
        (lat, lng, api_keys.google_key))
    data = json.load(urllib2.urlopen(url))
    return data['results'][0]['formatted_address']

# Concatenates encoded polylines together.
def concat_polylines(polylines):
    line_coords = []
    for line in polylines:
        if(line_coords == []):
            line_coords += decode(line)
        else:
            line_coords += decode(line)[1:]

    return encode_coords(line_coords)

# Finds the angle between the two vectors defined by 2->1 and 2->3
def vector_angle(latlong1, latlong2, latlong3):
    lat_mag1 = latlong1[0] - latlong2[0]
    lng_mag1 = latlong1[1] - latlong2[1]
    lat_mag2 = latlong3[0] - latlong2[0]
    lng_mag2 = latlong3[1] - latlong2[1]

    dot_p = (lat_mag1 * lat_mag2) + (lng_mag1 * lng_mag2)
    mag1 = math.sqrt(lat_mag1**2 + lng_mag1**2)
    mag2 = math.sqrt(lat_mag2**2 + lng_mag2**2)
    angle = math.degrees(math.acos(dot_p/(mag1*mag2)))
    return angle

# Instanstiate instance of the tweepy twitter API
twitter = twitter_api.TwitterAPI(TWEET_ON, NUM_TRIES)

# Get yesterday's lat/long pair and start there. 
latlong_file = open("latlong.txt", "r")
(lat,lng) = latlong_file.read().strip().split(" ")
(lat, lng) = (float(lat), float(lng))
latlong_file.close()

# Send out starting tweet
init_address = address_from_latlng(lat, lng)
twitter.tweet("Today we are starting from: %s." % init_address)

# Various variable intitialization
polylines = []
time = 0
tweet_num = 0
# Bias it generally away from pittsburgh
last_lat = 40.5354588 
last_lng = -79.9772996

# Loop until we have walked for over NUM_HOURS hours.
while(time < (3600*NUM_HOURS)):
    start_addr = str(lat) + " " + str(lng)
    angle = 0
    # Generate a new lat/long such that we meet min angle requirements
    while(angle < MIN_ANGLE):
        new_lat = lat + round((random.random()/5 - 0.1), 6)
        new_lng = lng + round((random.random()/5 - 0.04), 6)
        angle = vector_angle((last_lat, last_lng), (lat, lng), (new_lat, new_lng))

    # Set these for calculating next angle requirement.
    last_lat = lat
    last_lng = lng
    
    # Retry because sometimes we put the point in a body of water and fail.
    for j in range(NUM_TRIES):
        try:
            end_addr = str(new_lat) + " " + str(new_lng)
            # Get directions
            url = ("https://maps.googleapis.com/maps/api/directions/json?" +
            "origin=%s&destination=%s&avoid=highways&mode=walking&key=%s" % 
            (urllib2.quote(start_addr), urllib2.quote(end_addr), api_keys.google_key))

            data = json.load(urllib2.urlopen(url))
            steps = data['routes'][0]['legs'][0]['steps']
            break
        except:
            pass
        
    distance = 0
    delta_time = 0 # Keep track of time this leg takes
    polylines_in_route = []

    # Move until we are over MAX_DISTANCE meters from the starting location
    for step in steps:
        lat = step['end_location']['lat']
        lng = step['end_location']['lng']

        # add to all the accumulators
        distance += step['distance']['value']
        delta_time += step['duration']['value']
        polylines.append(step['polyline']['points'])
        polylines_in_route.append(step['polyline']['points'])

        if(distance > MAX_DISTANCE):
            break

    # Keep track of all of the final info about the trip. 
    address = address_from_latlng(lat, lng)
    hours, remainder = divmod(delta_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    time += delta_time
    tweet_num += 1
    
    # Make the main tweet text
    tweet = ("%d) Heading to %s, ETA: %d Minutes\nLink: http://maps.google.com/?q=%f,%f." % 
            (tweet_num, address, hours*60 + minutes, lat, lng))

    # Generate static image for main tweet, oh god, so many parameters
    url = ("https://maps.googleapis.com/maps/api/staticmap?" + 
        "zoom=14&size=506x253&scale=1&maptype=roadmap&markers=color:blue|" +
        "%f,%f&center=%f,%f&path=weight:3|color:red|enc:%s&key=%s" % 
    (lat, lng,lat, lng, concat_polylines(polylines_in_route), api_keys.google_key))

    twitter.tweet_img(url ,tweet[:140])
    print len(tweet)

    #Oh right this is a real time bot, time to sleep.
    if(SLEEP_ON):
        sleep(delta_time)
    latlong_file = open("latlong.txt", "w")
    latlong_file.write(str(lat) + " " + str(lng))
    latlong_file.close()

    # 99.9% of the time, when we are not sleeping, we are testing
    if(SLEEP_ON):
        date_suffix = strftime("%Y-%m-%d")
    else:
        date_suffix = "test"

# Write end of day data to file for displaying.
data_file = open(DATA_FILE_PATH + "/data" + date_suffix + ".txt", 'w')
data_file.write(concat_polylines(polylines))
data_file.close()
    
# We are done for the day, let the world know.
twitter.tweet("I'm done for today." + strftime("%Y-%m-%d") + " You can find today's walk at jlareau.club.cc.cmu.edu/walker/results.html?date=" + date_suffix)
