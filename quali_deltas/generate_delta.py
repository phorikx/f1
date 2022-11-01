#%%
import fastf1 as ff1
import pandas as pd
import matplotlib.pyplot as plt

ff1.Cache.enable_cache('cache')

quali = ff1.get_session(2021, 'Turkey', 'Q')
laps = quali.load_laps(with_telemetry=True)

drivers = laps.Driver.unique()
laptimes = []

for driver in drivers:
    laptimes.append(laps.pick_driver(driver).pick_fastest().LapTime.total_seconds())

min_laptime = min(laptimes)
for i, laptime in enumerate(laptimes):
    laptimes[i] = (laptime/min_laptime -1) * 100

df = pd.DataFrame({'drivers':drivers, 'laptimes': laptimes})

df.plot(x='drivers', y='laptimes', kind='scatter')
plt.show
