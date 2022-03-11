import sqlite3
import math


class StdevFunc:
    def __init__(self):
        self.M = 0.0
        self.S = 0.0
        self.k = 1

    def step(self, value):
        if value is None:
            return
        tM = self.M
        self.M += (value - tM) / self.k
        self.S += (value - tM) * (value - self.M)
        self.k += 1

    def finalize(self):
        if self.k < 3:
            return None
        return math.sqrt(self.S / (self.k - 2))


# with sqlite3.connect(':memory:') as con:
#     con.create_aggregate("stdev", 1, StdevFunc)
#
#     cur = con.cursor()
#
#     cur.execute("create table test(i)")
#     cur.executemany("insert into test(i) values (?)", [(1,), (2,), (3,), (4,), (5,)])
#     cur.execute("insert into test(i) values (null)")
#     cur.execute("select avg(i) from test")
#     print("avg: %f" % cur.fetchone()[0])
#     cur.execute("select stdev(i) from test")
#     print("stdev: %f" % cur.fetchone()[0])