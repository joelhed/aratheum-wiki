import jinja2
import os
import md2py
import re

def define_env(env):
    @env.macro
    def city(title, 
            image="",
            country="",
            region="",
            foundedyear="",
            foundedby="",
            government="",
            area="",
            population="",
            nicknames="",
            demonyms=""):
        a = locals()

        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template('templates/infobox_city.html')

        for k in a:
            a[k] = auto_link(str(a[k]), env.project_dir)

        return template.render(
                title=a['title'], 
                image=a['image'],
                country=a['country'],
                region=a['region'],
                foundedyear=a['foundedyear'],
                foundedby=a['foundedby'],
                government=a['government'],
                area=a['area'],
                population=a['population'],
                nicknames=a['nicknames'],
                demonyms=a['demonyms']
                )

    def calculate_link(match):
        link = match.group()[match.group().rfind('[')+1:match.group().rfind(']')-1]
        if '|' in link:
            title = link[link.find('|')+1:]
            file = link[:link.find('|')]
        else:
            file = link
            title = None
        print(file)
        print(title)
        project_root = os.path.join(env.project_dir, "docs")
        # Absolute URL of the linker
        # abs_linker_url = os.path.dirname(os.path.join(self.base_docs_url, self.page_url))
        
        # Find directory URL to target link
        # rel_link_url = ''
        # Walk through all files in docs directory to find a matching file
        abs_link_url = ''
        for root, dirs, files in os.walk(project_root):
            for name in files:
                # If we have a match, create the relative path from linker to the link
                if name == file:
                    # Absolute path to the file we want to link to
                    abs_link_url = os.path.dirname(os.path.join(root, name))
                    abs_link_url = os.path.join(abs_link_url, file)
                    # Constructing relative path from the linker to the link
                    rel_link_url = os.path.relpath(abs_link_url, project_root)

        if abs_link_url and os.path.exists(abs_link_url):
            md = open(abs_link_url, 'r').read()
            toc = md2py.md2py(md)
            if not title:
                title = str(toc.h1)
            return "<a href=\"" + "/" + rel_link_url[:rel_link_url.rfind('.')] + "\">" + title + "</a>"
        else:
            return link 

    def auto_link(string, project_root):

        regex = r'\[\[(.*?)\]\]'
        return re.sub(regex, calculate_link, string)
        
         
