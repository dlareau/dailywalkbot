from google_polyline import *
import fileinput
from glob import glob

def concat_polylines(polylines):
    line_coords = []
    for line in polylines:
        if(line_coords == []):
            line_coords += decode(line)
        else:
            line_coords += decode(line)[1:]

    return encode_coords(line_coords)

fnames = sorted(glob('data20*.txt'))
polylines = [line for line in fileinput.input(fnames)]

data_file = open("data.txt", 'w')
data_file.write(concat_polylines(polylines))
data_file.close()
