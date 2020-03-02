import logging as logger
import datetime, pandas as pd, time

def add_task(futureDate):
    logger.debug("Task Added into Queue")
    current_date = datetime.datetime.now()
    future_date = pd.to_datetime(futureDate)
    duration = (future_date-current_date).total_seconds()
    when_to_stop = abs(int(duration))
    while when_to_stop >0:
        m,s = divmod(when_to_stop,60)
        h,m = divmod(m,60)
        logger.debug(str(h).zfill(2) + ":" + str(m).zfill(2)+ ":" + str(s).zfill(2))
        time.sleep(1)
        when_to_stop-=1
    return True


