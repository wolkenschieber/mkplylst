# General usage

```
usage: mkplylist.py [-h] -s SOURCE_DIRECTORY [-t TARGET_DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE_DIRECTORY, --source_directory SOURCE_DIRECTORY
                        mp3 files root directory
  -t TARGET_DIRECTORY, --target_directory TARGET_DIRECTORY
                        Target directory for playlist. If not set, playlists are created in mp3 files direcotory.
```

# One playlist in each directory under `SOURCE_DIRECTORY`

```
mkplylist.py -s /mnt/storage/nfs/Music/Playlists
```

This will create an `m3u`-file in each subdirectory containing media files. Media files are referenced through filename only.

# All playlists in `TARGET_DIRECTORY`

```
mkplylist.py -s /mnt/storage/nfs/Music/Playlists -t /mnt/storage/nfs/Music/m3u
```

This will place all playlists in the target directory. Media files are referenced with absolte paths.
