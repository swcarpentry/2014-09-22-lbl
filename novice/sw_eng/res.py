from collections import namedtuple

ResRow = namedtuple(
    'ResRow',
    ('name', 'abbr', 'alt', 'lat', 'lon', 'county', 'month', 'storage'))


def read_reservoir_data(filename):
    rows = []

    f = open(filename)
    f.readline()

    for line in f:
        name, abbr, altitude, lat, lon, county, month, storage = line.split(',')
        altitude = int(altitude)
        lat = float(lat)
        lon = float(lon)
        storage = int(storage)
        new_row = ResRow(name, abbr, altitude, lat, lon, county, month, storage)
        rows.append(new_row)

    f.close()

    return rows


def filter_reservoir(rows, abbr):
    """
    Keep only the rows that match a reservoir abbreviation.

    """
    filtered_rows = []

    for row in rows:
        if row.abbr == abbr:
            filtered_rows.append(row)

    return filtered_rows


def filter_year(rows, filter_year):
    """
    Keep only the rows that match a year.

    """
    filtered_rows = []

    for row in rows:
        month, year = row.month.split('/')
        if int(year) == int(filter_year):
            filtered_rows.append(row)

    return filtered_rows
