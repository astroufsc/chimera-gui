from distutils.core import setup

setup(
    name='chimera-gui',
    version='0.0.1',
    packages=['chimera_gui', 'chimera_gui.modules'],
    scripts=['scripts/chimera-gui'],
    install_requires=['PyGTK', 'gdl', 'gtk-2.0', 'gobject', 'glib', 'cairo'],
    url='http://github.com/astroufsc/chimera-gui',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='PyGTK GUI for chimera'
)
