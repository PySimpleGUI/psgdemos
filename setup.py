import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="psgdemos",
    version="5.0.0",
    author="PySimpleSoft Inc.",
    description="Installs the full set of PySimpleGUI Demo Programs and the Demo Browser.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/PySimpleGUI/psgdemos",
    packages=['psgdemos'],
    license='Free To Use But Restricted',
    install_requires=['PySimpleGUI>=5'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Free To Use But Restricted",
        "Operating System :: OS Independent",
        "Framework :: PySimpleGUI",
        "Framework :: PySimpleGUI :: 5",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics",
    ],
    include_package_data=True,
    package_data={"":
["*","*.*"]
        },
entry_points={"gui_scripts": [
            "psgdemos=psgdemos.psgdemos:main"
],},
)

