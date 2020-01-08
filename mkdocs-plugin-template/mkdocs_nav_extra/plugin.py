import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from bs4 import BeautifulSoup

class NavExtra(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(mkdocs_utils.string_types, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    # def on_serve(self, server):
        # return server

    # def on_pre_build(self, config):
        # return

    # def on_files(self, files, config):
        # return files

    # def on_nav(self, nav, config, files):
        # return nav

    # def on_env(self, env, config, site_nav):
        # return env
    
    # def on_config(self, config):
        # return config

    # def on_post_build(self, config):
        # return

    # def on_pre_template(self, template, template_name, config):
        # return template

    # def on_template_context(self, context, template_name, config):
        # return context
    
    # def on_post_template(self, output_content, template_name, config):
        # return output_content
    
    # def on_pre_page(self, page, config, site_nav):
        # return page

    # def on_page_read_source(self, page, config):
        # return ""

    # def on_page_markdown(self, markdown, page, config, site_nav):
        # return markdown

    # def on_page_content(self, html, page, config, site_navigation=None, **kwargs):
                # return html

    # def on_page_context(self, context, page, config, nav):
        # return context

    def on_post_page(self, output_content, page, config):
        soup = BeautifulSoup(output_content, 'html.parser')
        nav_extra = soup.find("div", {"class": "sidebar"})
        if nav_extra:
            soup_toc = soup.find("nav", {"class" : "md-nav--secondary"})
            soup_toc.insert(0, nav_extra)
            print(soup)
        souped_html = soup.prettify(soup.original_encoding)
        return souped_html 

