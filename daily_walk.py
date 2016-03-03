import json
import urllib2
import urllib
import random
from google_polyline import *
import tweepy
from time import sleep, strftime
import os
import math
import api_keys

TWEET_ON = False
MAX_DISTANCE = 1000
NUM_HOURS = 8
DATA_FILE_PATH = "/var/www/html/walker"
NUM_TRIES = 3
MIN_ANGLE = 70

class TwitterAPI:
    def __init__(self):
        consumer_key = api_keys.twitter_c_k
        consumer_secret = api_keys.twitter_c_s
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = api_keys.twitter_a_t
        access_token_secret = api_keys.twitter_a_t_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        if(TWEET_ON):
            for i in range(NUM_TRIES):
                try:
                    self.api.update_status(status=message)
                    break
                except:
                    sleep(60)
        else:
            print("TWEET: " + message)

    def tweet_img(self, url, message):
        if(TWEET_ON):
            for i in range(NUM_TRIES):
                try:
                    urllib.urlretrieve(url, "img_upload.png")
                    fn = os.path.abspath("./img_upload.png")
                    self.api.update_with_media(fn, status=message)
                    break
                except:
                    sleep(60)
        else:
            print("IMAGE TWEET:" + message)

def address_from_latlng(lat, lng):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s" % (lat, lng, api_keys.google_key)
    data = json.load(urllib2.urlopen(url))
    return data['results'][0]['formatted_address']

def concat_polylines(polylines):
    line_coords = []
    for line in polylines:
        if(line_coords == []):
            line_coords += decode(line)
        else:
            line_coords += decode(line)[1:]

    return encode_coords(line_coords)

def dir_angle(latlong1, latlong2, latlong3):
    lat_mag1 = latlong1[0] - latlong2[0]
    lng_mag1 = latlong1[1] - latlong2[1]
    lat_mag2 = latlong3[0] - latlong2[0]
    lng_mag2 = latlong3[1] - latlong2[1]

    dot_p = (lat_mag1 * lat_mag2) + (lng_mag1 * lng_mag2)
    mag1 = math.sqrt(lat_mag1**2 + lng_mag1**2)
    mag2 = math.sqrt(lat_mag2**2 + lng_mag2**2)
    angle = math.degrees(math.acos(dot_p/(mag1*mag2)))
    return angle

twitter = TwitterAPI()

latlong_file = open("latlong.txt", "r")
(lat,lng) = latlong_file.read().strip().split(" ")
latlong_file.close()
lat = float(lat)
lng = float(lng)

init_address = address_from_latlng(lat, lng)
twitter.tweet("Today we are starting from: %s." % init_address)

coords = []
polylines = []
time = 0
i = 0
last_lat = 0
last_lng = 0
while(time < (3600*NUM_HOURS)):
    start_addr = str(lat) + " " + str(lng)
    angle = 0
    while(angle < MIN_ANGLE):
        new_lat = lat + round((random.random()/5 - 0.1), 6)
        new_lng = lng + round((random.random()/5 - 0.04), 6)
        angle = dir_angle((last_lat, last_lng), (lat, lng), (new_lat, new_lng))

    last_lat = lat
    last_lng = lng
    
    for j in range(NUM_TRIES):
        try:
            end_addr = str(new_lat) + " " + str(new_lng)
            # Get directions
            url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&avoid=highways&mode=walking&key=%s" % (urllib2.quote(start_addr), urllib2.quote(end_addr), api_keys.google_key)
            data = json.load(urllib2.urlopen(url))

            # Move along directions until we are over 1000 Meters from the starting location
            steps = data['routes'][0]['legs'][0]['steps']
            break
        except:
            pass
        
    distance = 0
    delta_time = 0
    for step in steps:
        distance += step['distance']['value']
        lat = step['end_location']['lat']
        lng = step['end_location']['lng']
        coords.append(str(lat) + ", " + str(lng))
        polylines.append(step['polyline']['points'])
        delta_time += step['duration']['value']
        eta = step['duration']['text']
        if(distance > MAX_DISTANCE):
            break

    address = address_from_latlng(lat, lng)
    hours, remainder = divmod(delta_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    time += delta_time
    i += 1
    
    tweet = "%d) Heading to Addr: %s, ETA: %d Minutes" % (i, address, hours*60 + minutes)
    url = "https://maps.googleapis.com/maps/api/staticmap?zoom=15&size=506x253&scale=1&maptype=roadmap&markers=color:blue%7C" + "%s,%s"  % (str(lat), str(lng)) + "&key=" + api_keys.google_key
    twitter.tweet_img(url ,tweet[:140])
    #print len(tweet)
    if(TWEET_ON):
        sleep(delta_time)
    latlong_file = open("latlong.txt", "w")
    latlong_file.write(str(lat) + " " + str(lng))
    latlong_file.close()
        
#for coord in coords:
#    print(coord)

if(TWEET_ON):
    date_suffix = strftime("%Y-%m-%d")
else:
    date_suffix = "test"
    
data_file = open(DATA_FILE_PATH + "/data" + date_suffix + ".txt", 'w')
data_file.write(concat_polylines(polylines))
data_file.close()
    
twitter.tweet("I'm done for today, you can find today's walk at jlareau.club.cc.cmu.edu/walker/results.html?date=" + date_suffix)
