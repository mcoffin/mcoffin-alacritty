#!/usr/bin/env python

import argparse
import shutil
import yaml

class Theme:
    def __init__(self, name):
        self.name = name
        self.filename = f'alacritty.{name}.yml'

    def config(self, base_filename = 'alacritty-base.yml'):
        with open(base_filename, 'r') as base_stream:
            base_config = yaml.safe_load(base_stream)
            with open(self.filename, 'r') as theme_stream:
                theme_config = yaml.safe_load(theme_stream)
                base_config['colors'] = theme_config['colors']
                return base_config

    def install(self, location = 'alacritty.yml'):
        config = self.config()
        with open(location, 'w') as out_stream:
            yaml.dump(config, out_stream)

def main():
    parser = argparse.ArgumentParser(description='mcoffin-alacritty installer')
    parser.add_argument('theme', metavar='THEME', type=str, nargs=1)

    args = parser.parse_args()

    theme = Theme(args.theme[0])
    theme.install()

if __name__ == '__main__':
    main()
