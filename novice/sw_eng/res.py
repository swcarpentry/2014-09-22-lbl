from collections import namedtuple

ResRow = namedtuple(
    'ResRow',
    ('name', 'abbr', 'alt', 'lat', 'lon', 'county', 'month', 'storage'))


def read_reservoir_data(filename):
    rows = []

    f = open(filename)
    f.readline()

    for line in f:
        name,abbr,altitude,lat,lon,county,month,storage = line.split(',')
        altitude = int(altitude)
        lat = float(lat)
        lon = float(lon)
        storage = int(storage)
        new_row = ResRow(name,abbr,altitude,lat,lon,county,month,storage)
        rows.append(new_row)

    f.close()

    return rows
