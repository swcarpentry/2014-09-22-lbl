import res


def test_read_reservoir_data():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)

    assert len(rows) == 6
    assert rows[0].abbr == 'KLM'
    assert rows[-1].abbr == 'NCM'


test_read_reservoir_data()
