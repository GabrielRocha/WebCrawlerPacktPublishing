from datetime import datetime
import os


def write_log(path, title=None, status=None):
    with open(os.path.join(path, "log"), "a+") as log:
            log.write("{date} -- Book: {title} -- Status: {status}\n".format(date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                                                             title=title,
                                                                             status=status))