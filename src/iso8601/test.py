from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from datetime import date, datetime, time, timedelta
import unittest

from iso8601 import TimeZone, parse, parse_time


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse('2012'), date(2012, 1, 1))
        self.assertEqual(parse('2012-05-03'), date(2012, 5, 3))
        self.assertEqual(parse('20120503'), date(2012, 5, 3))
        self.assertEqual(parse('2012-05'), date(2012, 5, 1))

        # Week numbers
        self.assertEqual(parse('2012-W05'), date(2012, 1, 30))
        self.assertEqual(parse('2012W05'), date(2012, 1, 30))
        self.assertEqual(parse('2012-W05-5'), date(2012, 2, 3))
        self.assertEqual(parse('2012W055'), date(2012, 2, 3))

        # Ordinal days
        self.assertEqual(parse('2012-007'), date(2012, 1, 7))
        self.assertEqual(parse('2012007'), date(2012, 1, 7))

        # Times
        self.assertEqual(parse('00:00'), time(0, 0))
        self.assertEqual(parse('12:04:23'), time(12, 4, 23))
        self.assertEqual(parse('120423'), time(12, 4, 23))
        self.assertEqual(parse('12:04'), time(12, 4, 0))
        self.assertEqual(parse('1204'), date(1204, 1, 1))
        self.assertEqual(parse_time('1204'), time(12, 4, 0))
        self.assertEqual(parse('12'), time(12, 0, 0))
        self.assertEqual(parse('02'), time(2, 0, 0))
        self.assertEqual(parse('12:04:23.450686'), time(12, 4, 23, 450686))

        # Combined
        self.assertEqual(parse('2008-09-03T20:56:35.450686'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686))

        self.assertEqual(parse('2008-09-03T20:56:35.450686Z'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686,
                                   TimeZone(timedelta())))

        self.assertEqual(parse('2008-09-03T20:56:35.450686+01'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686,
                                   TimeZone(timedelta(minutes=60))))

        self.assertEqual(parse('2008-09-03T20:56:35.450686+0100'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686,
                                   TimeZone(timedelta(minutes=60))))

        self.assertEqual(parse('2008-09-03T20:56:35.450686+01:30'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686,
                                   TimeZone(timedelta(minutes=60 + 30))))

        self.assertEqual(parse('2008-09-03T20:56:35.450686-01:30'),
                          datetime(2008, 9, 3, 20, 56, 35, 450686,
                                   TimeZone(timedelta(minutes=-(60 + 30)))))

        self.assertEqual(parse('2013-03-28T02:30:24+00:00'),
                         datetime(2013, 3, 28, 2, 30, 24,
                                  tzinfo=TimeZone(timedelta(minutes=0))))


if __name__ == '__main__':
    unittest.main()
