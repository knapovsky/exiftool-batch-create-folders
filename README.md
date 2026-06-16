# ExifTool Batch Create Folders

A small Python script that reads image captions with ExifTool, creates folders named after those captions, and moves images into the matching folders.

> Status: personal batch-processing utility.
>
> The script moves files. Test on a copy of your images first.

## What it does

`XML/create-folders.py`:

1. lists files in `../Pictures`
2. reads each file's XMP caption using ExifTool
3. creates a destination folder under `../Folders` named after the caption
4. moves the image into that folder

## Requirements

- Python 3
- ExifTool installed at `/opt/homebrew/bin/exiftool` or script edited for your system

On macOS with Homebrew:

```bash
brew install exiftool
```

## Repository structure

```text
.
├── XML/create-folders.py
├── README.md
└── .gitignore
```

## Expected working layout

The script expects this layout relative to the `XML/` directory:

```text
project-root/
├── Folders/       # Destination folders are created here
├── Pictures/      # Source images are read and moved from here
└── XML/
    └── create-folders.py
```

## Usage

```bash
cd XML
python3 create-folders.py
```

## Safety notes

- The script moves files with `shutil.move()`.
- Destination folder names come from image captions; review captions first.
- Existing folders are tolerated, but name collisions are not handled robustly.
- Hard-coded paths should be edited before use.

## License

No explicit license is included. Treat the code as all rights reserved unless a license is added by the repository owner.
