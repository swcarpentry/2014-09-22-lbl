import sys

import res

if len(sys.argv) != 4:
    print 'Usage: mean_storage.py <filename> <res abbr> <year>'
    sys.exit()

filename = sys.argv[1]
abbr = sys.argv[2]
year = sys.argv[3]

rows = res.read_reservoir_data(filename)
rows = res.filter_reservoir(rows, abbr)

if len(rows) == 0:
    raise RuntimeError('We filtered all the reservoirs!')

rows = res.filter_year(rows, year)
ms = res.mean_storage(rows)

print ms
