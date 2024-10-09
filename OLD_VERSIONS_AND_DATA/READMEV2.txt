Compilar con pygbag , pygbag main.py , el archivo ha de renombrarse como main.py.
ejecutarlo desde el directorio en el que esta el main.
Ha de ejecutarse desde la CMD o Powershell.

Instalar pygbag desde CMD , recuerda añadir python al path para usar -> pip install pygbag.
Alternativas a posibles errores:
py -m pip install pygbag
python -m pip install pygbag

funcion: 

async def main():
	while True:

		await asyncio.sleep(0) 
asyncio.run(main())

Importar : Import asyncio

WEB WABS:
https://itch.io/c/2563651/pygame-wasm

Seleccionar en el apartado Kind of project:
HTML - DESDE ZIP 

El zip a subir sera la carpeta web , que estara dentro de build tras hacer pygbag game.py.
Se ha de comprimir si o si en zip.
