#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from os import walk
from os import path


def iterate_dirs(source_dir_path, target_dir_path=None):
    for (root, dirs, files) in walk(source_dir_path):
        if not "attic" in root:
            media_files = get_file_list(root, files, target_dir_path is None)
            if len(media_files) > 0:
                playlist_dir = target_dir_path if target_dir_path else root
                playlist_path = path.join(playlist_dir, path.basename(root) + ".m3u")
                write_playlist(playlist_path, media_files)


def get_file_list(root, files, relative=True):
    media_files = []
    for file in files:
        extension = path.splitext(file)[1]
        if extension in ['.mp4', '.mp3', '.mkv', '.aac']:
            media_file = file if relative else path.join(root, file)
            media_files.append(media_file)
    media_files.sort()
    return media_files


def write_playlist(playlist_path, files):
    with open(playlist_path, 'w', encoding='utf-8') as p:
        for f in files:
            print(f, file=p)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--source_directory", required=True, help="mp3 files root directory")
    parser.add_argument("-t", "--target_directory", required=False,
                        help="Target directory for playlist. If not set, playlists are created in mp3 files direcotory.")
    parser.set_defaults(sort_by_files=False)
    return parser.parse_args()


def main():
    args = parse_arguments()
    source_directory = path.abspath(args.source_directory)
    target_directory = args.target_directory
    iterate_dirs(source_directory, target_directory)


if __name__ == '__main__':
    main()
