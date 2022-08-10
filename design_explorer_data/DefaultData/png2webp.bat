REM #Download dwebp (WebP decoder tool) https://developers.google.com/speed/webp/download
REM #Run 
for %%f in (*.png) do cwebp.exe "%%f" -o "%%~nf.webp" -lossless
PAUSE