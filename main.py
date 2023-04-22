import os
import time
import tkinter as tk
import threading

# Funkcja, która uśpi komputer po zadanym czasie w sekundach
def sleep_computer_after_time(seconds):
    time_left = seconds
    while time_left > 0 and not stop_timer:
        time.sleep(1)  # Czekaj 1 sekundę
        time_left -= 1
        remaining_time = "Pozostały czas do uśpienia: {} sekund".format(time_left)
        status_label.config(text=remaining_time)  # Aktualizacja pozostałego czasu
    if not stop_timer:
        os.system("pmset sleepnow")  # Uśpij komputer

# Funkcja obsługująca zdarzenie naciśnięcia przycisku "Uśpij komputer"
def on_sleep_button_click():
    global stop_timer
    stop_timer = False
    try:
        time_limit = int(time_entry.get())  # Pobierz wartość z pola wprowadzania
        if time_limit == 0:
            sleep_computer_now()
        elif time_limit > 0 and time_limit <= 18000:
            # Uruchom wątek odliczania czasu
            countdown_thread = threading.Thread(target=sleep_computer_after_time, args=(time_limit,))
            countdown_thread.start()
        else:
            status_label.config(text="Czas musi być pomiędzy 1 a 18000 sekundami (5 godzin)")
    except ValueError:
        status_label.config(text="Czas musi być liczbą całkowitą")

# Funkcja uśpienia komputera natychmiastowo
def sleep_computer_now():
    status_label.config(text="Komputer zostanie uśpiony natychmiastowo")
    time.sleep(1)  # Czekaj 1 sekundę
    os.system("pmset sleepnow")  # Uśpij komputer

# Funkcja obsługująca zdarzenie naciśnięcia przycisku "Przerwij"
def on_cancel_button_click():
    global stop_timer
    stop_timer = True  # Zatrzymaj odliczanie czasu
    status_label.config(text="Uśpienie przerwane")

# Tworzenie okna głównego
window = tk.Tk()
window.title("Uśpij komputer ® gramszu 2023 ")  # Tytuł okna
window.geometry("500x350")  # Rozmiar okna

# Dodanie elementów interfejsu graficznego
time_label = tk.Label(text="Wprowadź czas do uśpienia (w sekundach, max. 18000):")
time_label.pack(pady=10)
time_entry = tk.Entry()  # Pole wprowadzania czasu
time_entry.pack(pady=5)
sleep_button = tk.Button(text="Uśpij komputer", command=on_sleep_button_click)
sleep_button.pack(pady=10)
sleep_now_button = tk.Button(text="Spij teraz", command=sleep_computer_now)
sleep_now_button.pack(pady=10)
cancel_button = tk.Button(text="Przerwij", command=on_cancel_button_click)
cancel_button.pack(pady=10)
status_label = tk.Label(text="")  # Etykieta wyświetl
status_label = tk.Label(text="")  # Etykieta wyświetlająca status
status_label.pack(pady=10)

# Uruchomienie pętli obsługi zdarzeń
window.mainloop()  # Pętla obsługi zdarzeń dla okna
