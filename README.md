# JekHELP

`jekhelp` is a command line tool that helps resizing pictures and creating picture gallery files for websites built with Jekyll.

## Setup

* Clone the repo and `cd` into it
* Install with `pip install .`
* Create a configuration file `~/.config/jekhelp/config.yaml` and set `site_root` to your Jekyll site's source directory (eg. to `~/myblog_source`)

## Usage

`jekhelp --help` and `jekhelp thumbs --help` should reveal all possibilities.

Please open an issue in case you're missing something in the online help. Thank you!

# Bash version

You'll also find the predecessors of above's tool in this repo. They are written purely in bash-compatible code. I don't use and maintain them anymore but leave them here for reference.

* `jekallery.sh` generates Jekyll collection files (.md) for a photo gallery
* `thumbs.sh` generates smaller version of pictures that can be used for the Jekyll gallery
