Archur
======
  
Generates random arch wallpapers from a text file!  
Based on [this reddit
thread](https://www.reddit.com/r/archlinux/comments/4gc2lw/some_arch_wallpapers_i_made/)
 
  
Depends on pillow

```
λ » archur -h
usage: archur.py [-h] -o OUTPUT [-t THEME] [--text TEXT] [-r RESOLUTION]
                 [-fg FOREGROUND_COLOR] [-bg BACKGROUND_COLOR]

Generate random Arch wallpaper

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name
  -t THEME, --theme THEME
                        The theme to use, else random. 'black' or 'solarized'
  --text TEXT           Text on the picture, or random
  -r RESOLUTION, --resolution RESOLUTION
                        Sets the resolution of the image. Example: 1920x1080
  -fg FOREGROUND_COLOR, --foreground-color FOREGROUND_COLOR
                        Color for the text and the logo.
  -bg BACKGROUND_COLOR, --background-color BACKGROUND_COLOR
                        Color for the background.
```
