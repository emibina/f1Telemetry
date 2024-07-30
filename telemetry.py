from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from fastf1.ergast import Ergast
from pathlib import Path

def get_data(year_name, circuit_name, session_name, driver_name):
    session = fastf1.get_session(int(year_name), circuit_name, session_name)
    session.load()
    driver = session.laps.pick_driver(driver_name)
    full_data = driver.get_telemetry()
    Path("./Telemetry").mkdir(parents=True, exist_ok=True)
    full_data.to_csv(f'./Telemetry/{driver_name}_{session_name}_{year_name}_{circuit_name}_car_data.csv', index=False, float_format='%.8f')

def get_season(year_name):
    ergast = Ergast()
    season = ergast.get_race_schedule(year_name)
    return season['raceName'].tolist()

def get_drivers(year_name, circuit_name, session_name):
    session = fastf1.get_session(int(year_name), circuit_name, session_name)
    session.load()
    drivers_num = session.drivers
    drivers_name = []
    for driver in drivers_num:
        drivers_name.append(session.laps.pick_driver(driver)['Driver'].iloc[0])
    return drivers_name, drivers_num