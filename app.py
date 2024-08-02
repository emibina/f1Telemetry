import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import telemetry

# Creazione della finestra principale
root = tk.Tk()
root.title("Interfaccia di download CSV")

# Creazione dei frame per le label e le entry box
frame_anno = ttk.Frame(root, padding="10")
frame_anno.grid(row=0, column=0, sticky=(tk.W, tk.E))

frame_circuito = ttk.Frame(root, padding="10")
frame_circuito.grid(row=1, column=0, sticky=(tk.W, tk.E))

frame_sessione = ttk.Frame(root, padding="10")
frame_sessione.grid(row=2, column=0, sticky=(tk.W, tk.E))

frame_pilota = ttk.Frame(root, padding="10")
frame_pilota.grid(row=3, column=0, sticky=(tk.W, tk.E))

# Creazione delle label
label_anno = ttk.Label(frame_anno, text="Anno")
label_anno.pack(side="left")

label_circuito = ttk.Label(frame_circuito, text="Circuito")
label_circuito.pack(side="left")

label_sessione = ttk.Label(frame_sessione, text="Sessione")
label_sessione.pack(side="left")

label_pilota = ttk.Label(frame_pilota, text="Pilota")
label_pilota.pack(side="left")

YEARS = [
"2018",
"2019",
"2020",
"2021",
"2022",
"2023",
"2024"
]

SESSIONS = ['Q', 'R']

CIRCUITS = telemetry.get_season(YEARS[0])

DRIVERS = telemetry.get_drivers(YEARS[0], CIRCUITS[0], SESSIONS[0])[0]

def update_circuit(race):
    clicked_circuit.set(race)
    drivers_name, drivers_num = telemetry.get_drivers(click.get(), clicked_circuit.get(), clicked_session.get())
    entry_pilota['menu'].delete(0, 'end')
    clicked_pilota.set(drivers_name[0])
    for driver in drivers_name:
        entry_pilota['menu'].add_command(label = driver, command=lambda value=driver: clicked_pilota.set(value))
    

def pick_races(year):
    races = telemetry.get_season(year)
    entry_circuito['menu'].delete(0, 'end')
    click.set(year)
    clicked_circuit.set(races[0])
    for race in races:
        entry_circuito['menu'].add_command(label = race, command=lambda value=race: update_circuit(value))

click = StringVar()
click.set(YEARS[0])
# Creazione delle entry box
entry_anno = ttk.OptionMenu(frame_anno, click, YEARS[0], *YEARS, command = lambda x: pick_races(x))
entry_anno.pack(side="left")

clicked_circuit = StringVar()
clicked_circuit.set(CIRCUITS[0])

entry_circuito = ttk.OptionMenu(frame_circuito, clicked_circuit, CIRCUITS[0], *CIRCUITS)
entry_circuito.pack(side="left")

clicked_session = StringVar()
clicked_session.set(SESSIONS[0])

entry_sessione = ttk.OptionMenu(frame_sessione, clicked_session, SESSIONS[0], *SESSIONS)
entry_sessione.pack(side="left")

clicked_pilota = StringVar()
clicked_pilota.set(DRIVERS[0])

entry_pilota = ttk.OptionMenu(frame_pilota, clicked_pilota, DRIVERS[0], *DRIVERS)
entry_pilota.pack(side="left")

# Creazione del bottone per il download
button_download = ttk.Button(root, text="Download CSV", command=lambda : telemetry.get_data(click.get(), clicked_circuit.get(), clicked_session.get(), clicked_pilota.get()))
button_download.grid(row=4, column=0, pady=10)

# Avvio del loop principale dell'interfaccia
root.mainloop()