import numpy.testing as npt

import res


def test_read_reservoir_data():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)

    assert len(rows) == 6
    assert rows[0].abbr == 'KLM'
    assert rows[-1].abbr == 'NCM'


def test_filter_reservoir():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)
    abbr = 'SPB'

    filtered_rows = res.filter_reservoir(rows, abbr)

    assert len(filtered_rows) == 2
    assert filtered_rows[0].abbr == abbr
    assert filtered_rows[1].abbr == abbr


def test_filter_year():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)
    year = 2005

    filtered_rows = res.filter_year(rows, year)

    assert len(filtered_rows) == 3
    for r in filtered_rows:
        assert r.month[-4:] == str(year)

    year = '2007'

    filtered_rows = res.filter_year(rows, year)

    assert len(filtered_rows) == 1
    assert filtered_rows[0].month[-4:] == year


def test_mean_storage():
    filename = 'reservoir_storage_small.dat'
    rows = res.read_reservoir_data(filename)
    abbr = 'NCM'
    year = 2008
    rows = res.filter_year(rows, year)
    rows = res.filter_reservoir(rows, abbr)

    assert res.mean_storage(rows) == 175560

    rows = res.read_reservoir_data(filename)
    abbr = 'KLM'
    year = 2005
    rows = res.filter_year(rows, year)
    rows = res.filter_reservoir(rows, abbr)

    npt.assert_allclose(res.mean_storage(rows), 388917.333333333)
