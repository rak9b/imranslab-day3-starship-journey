render:
powershell -ExecutionPolicy Bypass -File render.ps1

format:
black .

clean:
rm -rf media
