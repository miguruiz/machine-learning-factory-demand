SCRIPT_REAL(
'
import pandas as pd

dates = _arg1
time_series = _arg2
fake_today = _arg3
period_to_forecast = _arg4

return period_to_forecast
',

ATTR([Order Date]),
ATTR([Units Ordered]),
MIN([Fake_today]),
ATTR([Period_to_forecast_in_days]))