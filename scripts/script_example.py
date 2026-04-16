# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "peanut-butter-and-jelly",
#     "pygreetings",
#     "pyospackage-agastya",
#     "pyospackage-feulloah",
#     "pyospackage-frankosuna",
#     "pyospackage-gancayco",
#     "pyospackage-glowing-couscous",
#     "pyospackage-jacksayshi",
#     "pyospackage-kushwaha",
#     "pyospackage-pancakereport",
#     "pyospackage-ycc",
# ]
#
# [tool.uv.sources]
# pyospackage-pancakereport = { git = "https://github.com/pancakereport/pyopensci-workshop-create-python-package.git" }
# pyospackage-jacksayshi = { git = "https://github.com/jacksayshi/pyopensci_jacksayshi.git" }
# pyospackage-ycc = { git = "https://github.com/miniyachi/pyosPackage_yc.git" }
# pygreetings = { git = "https://github.com/brunj7/pygreetings.git" }
# peanut-butter-and-jelly = { git = "https://github.com/srerickson/peanut-butter-and-jelly.git" }
# pyospackage-frankosuna = { git = "https://github.com/frankosuna/pyosPackage_frankosuna.git" }
# pyospackage-feulloah = { git = "https://github.com/feulloah/pyosPackage_feulloah.git" }
# pyospackage-glowing-couscous = { git = "https://github.com/kungfuchicken/pyosPackage-glowing-couscous.git" }
# pyospackage-agastya = { git = "https://github.com/Agastyarathee/pyos_Packages_rathee.git" }
# pyospackage-kushwaha = { git = "https://github.com/kush025priya-spec/shipit-project-PK.git" }
# pyospackage-gancayco = { git = "https://github.com/cagancayco/pyosPackage_gancayco.git" }
# ///

# NOTE: uv add --script example.py '-r requirements.txt' will add dependencies
# to the script file

import pkgutil

from pprint import pprint


pprint(list(pkgutil.iter_modules()))
