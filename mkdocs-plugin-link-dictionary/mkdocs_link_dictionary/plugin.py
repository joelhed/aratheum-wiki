import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class LinkDictionary(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(mkdocs_utils.string_types, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_files(self, files, config):
        f = open(".dictionary", "w")
        for file in files.documentation_pages():
            filename = os.path.basename(file.src_path)
            f.write(filename + "\t/\tlanguage:markdown\n")
        f.close()
