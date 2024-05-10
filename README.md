# Flask_template

Flask template es un proyecto open source que permite tener una guia rapida de como iniciar un proyecto de Flask con Python, con unos breves ejemplos.

# Requerimientos de Instalación

- Python 3.6 o superior
- Visual Studio Code
- Git terminal (bash)
- windows (preferible para los comandos)

# clonar repositorio

Clona este repositorio con este comando desde Git bash.

```bash
$ https://github.com/Jhoan5/Flask_template.git
```

# Instalación

Abrir Visual Studio Code para instalar y ejecutar aplicación de Flask. Esta instalación funciona en cualquier proyecto estruturado de la manera de este proyecto

1. Instalar ambiente virtual
   ```bash
   $ python3 -m venv .venv
   ```
2. Activar el ambiente virtual(windows)

   ```bash
   $ . .venv/Scripts/activate
   ```

3. Instalar Flask
   ```bash
   $ pip install Flask
   ```
4. Ejecutar aplicación, importante ejecutar desde la carpeta raíz. El app hace referencia al nombre del archivo principal que inicia Flask puede ser hello.py y seria hello en cambio de app. En esta aplicación usamos app.py por ello decimos app.
   ```bash
   $ Flask --app app run --debug
   ```
