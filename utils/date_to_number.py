import datetime;

def date_to_number(date):
    ## map date to a number, make sure that the same date always maps to the same number
    ## day/month/year ---> day + (month-1)*31 
    day = int(date[-2:])
    month = int(date[-4:-2])

    return day+(month-1)*31