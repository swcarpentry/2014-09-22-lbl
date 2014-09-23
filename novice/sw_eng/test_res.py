import res


def test_read_reservoir_data():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)

    if len(rows) != 6:
        print 'Rows was not 6 lines long!!'
    if rows[0].abbr != 'KLM':
        print 'First row abbreviation is not KLM!'
    if rows[-1].abbr != 'NCM':
        print 'Last row abbreviation is not NCM!'


test_read_reservoir_data()
