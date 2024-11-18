from cx_Freeze import setup, Executable

setup(
    name="Sleep",
    version="1.0",
    description="Opis twojej aplikacji",
    executables=[Executable("sleep.py")]
)
