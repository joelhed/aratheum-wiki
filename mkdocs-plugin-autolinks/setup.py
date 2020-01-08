from setuptools import setup, find_packages

setup(
    name='mkdocs-autolinks-plugin',
    version='0.1',
    packages=find_packages(),
    author='Zach Hannum',
    description='Calculate relative links.',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'autolinks = mkdocs_autolinks_plugin.plugin:AutoLinksPlugin',
        ]
    },
)
