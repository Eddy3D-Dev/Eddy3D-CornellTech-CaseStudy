REM #Download dwebp (WebP decoder tool) https://developers.google.com/speed/webp/download
REM #Run 
for %%f in (*.webp) do dwebp.exe -o "%%~nf.png" "%%f"
PAUSE