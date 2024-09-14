# SScript-Archive

Archived versions of SScript, a Haxe Script library, so Psych Engine and other projects can be developed and compiled.

## Installation Instructions

### Via the included Python script (Recommended)

- Download and run `install.py` with the desired version (e.g `install.py 21.0.0`)
  - Requires `requests` (`pip install requests`)

### Install manually

1. Select a version from [the list](https://github.com/CobaltBar/SScript-Archive/tree/main/archives) and download it with the download button
2. Move this zip into your source directory
3. Go into your source code directory, open a terminal and write `haxelib install ZIPNAME.zip`

## Troubleshooting
### For manual instructions
**IF** moving SScript to your source directory creates more problems than it solves, run `haxelib remove SScript` in the same terminal/current working directory where it was installed

Follow these steps:

- Run `haxelib config` in the same terminal/current working directory and remember this path
- Open a new terminal at this path, navigate to it and open it using the taskbar, whichever way you prefer.
- Perform the install command there, with the file present in that directory.

If you are still getting the "SScript is not available, thanks to everyone for their support" message, make sure you read the instructions correctly.

## Recommended versions

### For Psych Engine

| Psych Version | SScript |
| -------- | ------- |
| 1.0b (Pre [HScript-Iris](https://www.github.com/crowplexus/HScript-Iris/)) | from 17.0.618 to 21.0.0 |
| 0.7.3    | 7.7.0 |
| 0.7.2    | 7.7.0 |
| 0.7.1h    | 4.0.1 |
| 0.7.1    | from 3.0.0 to 4.0.1 |
| [main](https://www.github.com/ShadowMario/FNF-PsychEngine/tree/main/) (as of Sep. 9, 2024) | 7.7.0 to 8.1.6 |

### For other projects

Please choose the version accordingly. To compare across versions, you can use a free software, like [Meld](https://meldmerge.org/).

## Issues

To report issues, open one in GitHub. Please follow the instructions carefully and only report issues if you can't figure it out.

For issues with specific versions, open an issue and tell us what's wrong with any version.

## Credits

- [Cobalt Bar](https://cobaltbar.github.io/) - Putting the collection together
- [tposejank](https://tposejank.carrd.co/) - SScript zips + verification
- [LarryFrosty](https://www.youtube.com/@larryfrosty) - SScript zips
- [Moonlight Catalyst](https://mooniecat.carrd.co/) - SScript zips
- [Lily](https://mcagabe19.pages.gay/) - Mobile SScript Patches

## Contributing

Read the [contributing guide](CONTRIBUTING.md).
