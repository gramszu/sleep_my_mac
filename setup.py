import os
import subprocess

def run_command(command):
    """Uruchamia polecenie w terminalu i wyświetla wynik."""
    try:
        result = subprocess.run(command, shell=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Błąd: {e.stderr}")
        return None

def is_git_repo():
    """Sprawdza, czy bieżący katalog to repozytorium Git."""
    return run_command("git rev-parse --is-inside-work-tree") == "true"

def main():
    print("=== Git Automat ===")

    # Sprawdzenie, czy jesteś w repozytorium Git
    if not is_git_repo():
        print("Nie znajdujesz się w repozytorium Git. Przejdź do odpowiedniego katalogu.")
        return

    # Wyświetl zmodyfikowane pliki
    print("\nZmodyfikowane pliki:")
    run_command("git status -s")
    
    # Zapytaj o pliki do dodania
    files_to_add = input("\nPodaj pliki do dodania (oddzielone spacją) lub wpisz '.' aby dodać wszystkie: ").strip()
    if not files_to_add:
        print("Nie podano plików do dodania. Kończę.")
        return

    # Dodaj pliki do staging
    print("\nDodawanie wybranych plików...")
    run_command(f"git add {files_to_add}")

    # Zapytaj o treść commita
    commit_message = input("Podaj treść commita: ").strip()
    if not commit_message:
        print("Nie podano treści commita. Kończę.")
        return

    # Commituj zmiany
    print("\nCommitowanie zmian...")
    run_command(f'git commit -m "{commit_message}"')

    # Wysyłanie zmian na zdalne repozytorium
    print("\nWysyłanie zmian na zdalne repozytorium...")
    run_command("git push")

    print("\nWszystko gotowe! Wybrane pliki zostały zapisane i wysłane.")

if __name__ == "__main__":
    main()
