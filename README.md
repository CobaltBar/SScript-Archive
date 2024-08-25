# SScript-Archive

Archived versions of SScript so PsychEngine can be compiled

## Installation Instructions

### Via the included Python script (Recommended)
- Download and run `install.py` with the desired version (e.g `install.py 21.0.0`)
  - Requires `requests` (`pip install requests`)

### Install manually
1. Select a version from [the list](https://github.com/CobaltBar/SScript-Archive/tree/main/archives) and download it with the download button
2. Extract it to an external directory
3. Go into your source code directory, open a terminal and write `haxelib config`, remember this path
4. Don't close the terminal yet, write `haxelib remove SScript` if you already have SScript and it **does not work**
5. Go to the path given by step 3, and create the `SScript` folder again
6. Copy the `.current` file and the version folder into this new `SScript` folder
7. Restart your terminal and build again. If you can't compile, make sure you got the correct version and you followed the instructions correctly.

## Credits

- [Cobalt Bar](https://cobaltbar.github.io/) - Putting the collection together
- [tposejank](https://tposejank.carrd.co/) - SScript zips + verification
- [LarryFrosty](https://www.youtube.com/@larryfrosty) - SScript zips
- [Moonlight Catalyst](https://mooniecat.carrd.co/) - SScript zips
- [Lily](https://mcagabe19.pages.gay/) - Mobile SScript Patches
