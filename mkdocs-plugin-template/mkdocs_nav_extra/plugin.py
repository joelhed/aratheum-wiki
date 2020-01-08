import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

from bs4 import BeautifulSoup
import markdown

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
            soup_toc = soup.find("div", {"data-md-component" : "toc"})
            
            if soup_toc:
                scrollwrap = soup_toc.findNext("div", {"class" : "md-sidebar__scrollwrap"})
                if scrollwrap:
                    scrollwrap.insert(0, nav_extra)
            else:
                print("WARNING: Table of Contents sidebar not found")
        
        
        for link in soup.findAll("a", {"class" : None}, href=lambda x: not x.startswith('http') ):
            md_src_path = link['href'][3:-1] + ".md"
            md_link_path = os.path.join(os.path.dirname(page.file.abs_src_path), md_src_path )
            if os.path.isfile(md_link_path):
                print(md_link_path + " exists, attempting to create tooltip text")
                input_file = codecs.open(md_link_path, mode="r", encoding="utf-8")
                text = input_file.read()
                html = markdown.markdown(text)
                link_soup = BeautifulSoup(html, 'html.parser')
                print(link_soup.prettify(link_soup.original_encoding))

        souped_html = soup.prettify(soup.original_encoding)
        return souped_html 

