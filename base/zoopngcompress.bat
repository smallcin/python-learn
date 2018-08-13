
set path=%~d0%~p0
"%path%zoopng.exe" --force --verbose %1
"%path%zoopng.exe" --force --verbose --ordered --speed=1 --quality 10 %1
