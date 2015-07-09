# gruvbox for pygments

[Gruvbox](https://github.com/morhetz/gruvbox) is an excellent "retro
groove color scheme" for Vim. This is an attempt at adapting it for use
as a [Pygments](http://pygments.org) theme.

Gruvbox is a highly customized Vim color scheme, and it can look quite
different when viewing different file formats (Ruby vs. Clojure is a
good example). This Pygments theme is designed to mirror, as closely
as possible, the Clojure file syntax highlighting in dark mode. Other
languages do still look quite nice with this Pygments theme, it's
just that they may not look very much like their corresponding syntax
highlighting with the Gruvbox color scheme in Vim.

To create this pygments theme, I used
[vim2pygments](https://github.com/honza/vim2pygments) to convert
`gruvbox.vim` into a pygments theme file, and then made a few additional
tweaks to the resulting `gruvbox.py` to get the Clojure syntax
highlighting looking as much as possible like it does in Vim. The
conversion process was a little trickier than usual, because the author
of Gruvbox utilized the power of Vimscript to do some clever things and
basically generate the highlighting information programmatically instead
of hard-coding it into the file like most Vim color schemes do. Because
vim2pygments needs to see a bunch of lines starting with `hi`, I had to
change the `execute` command that sources each would-be `hi` command
on-the-fly, and instead have it append each `hi` command to a temporary
file that vim2pygments could understand. It was hacky, but it worked.

# Usage / Installation

## Blog
If you just want to use the Gruvbox theme for the code blocks on your
Jekyll blog or whatever, simply replace your `pygments.css` with the one
in this repo and you're good to go. You may wish to make a backup of
your old css file if you ever change your mind.

For more general use with pygments, there are two methods of installing:

## Manual
Find your pygments installation path (on my system, it's located at
`/usr/local/lib/python2.7/site-packages/pygments`) and rename the
`style.py` from this repo to `gruvbox.py`, and move it into the `styles`
subdirectory of the path above.

## Automatic
For those who do not want to directly add to the source directories
of the project, clone this repo to a suitable place, for example,
`~/.local/scripts/gruvbox-pygments`, change directory to this location
and run:

    sudo python setup.py develop

This will hook in this style into `pygments` without editing the source
directories of `pygments` iteself. Do not delete this directory as this
where python will be looking for this style file.

# Uninstall

## Blog
Replace the `pygments.css` with your backup for the Jekyll blog or
whatever.

## Manual
Remove the `gruvbox.py` file from the installation path.

## Automatic
Remove just as you would any other python package. For example with `pip`:

    sudo pip uninstall gruvbox-pygments

You can now safely remove the directory containing this repo.

# Screenshot

!["gruvbox pygments theme"](https://github.com/daveyarwood/gruvbox-pygments/blob/master/screenshot.png?raw=true "gruvbox pygments theme")
