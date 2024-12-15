import os
import sys
import time

def main():
    # Sprawdzenie, czy podano argument w linii poleceń
    if len(sys.argv) != 2:
        print("Użycie: python sleep_timer.py <czas w minutach>")
        sys.exit(1)

    try:
        # Pobranie czasu z argumentu i przeliczenie na sekundy
        sleep_time_minutes = int(sys.argv[1])
        if sleep_time_minutes <= 0:
            raise ValueError
        sleep_time_seconds = sleep_time_minutes * 60
    except ValueError:
        print("Podaj prawidłową wartość czasu (liczba dodatnia).")
        sys.exit(1)

    print(f"MacBook uśpi się za {sleep_time_minutes} minut.")

    # Odliczanie
    for remaining_seconds in range(sleep_time_seconds, 0, -1):
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        sys.stdout.write(f"\rCzas do uśpienia: {minutes} minut {seconds} sekund")
        sys.stdout.flush()
        time.sleep(1)

    # Usypianie MacBooka
    print("\nUsypianie MacBooka...")
    os.system("pmset sleepnow")

if __name__ == "__main__":
    main()
