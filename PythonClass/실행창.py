from datetime import date
from dateutil.relativedelta import relativedelta
edt = date.today() + relativedelta(months=+3)
print(date.today(), edt)