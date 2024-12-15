import sys
import time

# Funkcja do odliczania czasu
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Pozostały czas: {timer}", end='\r')  # Nadpisuje linię
        time.sleep(1)
        seconds -= 1

    print("Czas minął!")

# Sprawdzenie, czy użytkownik podał czas w linii poleceń
if len(sys.argv) != 2:
    print("Proszę podać czas w sekundach.")
    sys.exit(1)

# Pobieramy czas z linii poleceń
try:
    time_in_seconds = int(sys.argv[1])
except ValueError:
    print("Czas musi być liczbą całkowitą.")
    sys.exit(1)

# Wywołanie funkcji odliczania
countdown(time_in_seconds)
