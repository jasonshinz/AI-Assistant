import time


class TimeService:

    def now(self):

        t = time.localtime()

        return "{:02}:{:02}:{:02}".format(
            t[3],
            t[4],
            t[5]
        )