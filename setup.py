import setuptools
import shutil

from setuptools.command.sdist import sdist
from wheel.bdist_wheel import bdist_wheel

with open("README.md", "r") as fh:
    long_description = fh.read()

# Remove build folder 
#shutil.rmtree('build')

def clean_folders():    
    print('Removing temporary folders.')

    TMP_FOLDERS = ['visualist.egg-info', 'build']
    for folder in TMP_FOLDERS:
        shutil.rmtree(folder)

class SdistCommand(sdist):
    """Custom build command."""

    def run(self):        
        sdist.run(self)

class BdistWheelCommand(bdist_wheel):
    """Custom build command."""

    def run(self):        
        bdist_wheel.run(self)
        clean_folders()

setuptools.setup(
    name="visualist",
    version="0.2.0",
    author="Thiago Nepomuceno",
    author_email="thi.nepo@gmail.com",
    description="A simple library to visualize lists.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    #url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    #entry_points={
    #    'console_scripts': ['autoiot=bin.autoiot_cli:main'],
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Pillow>=7.1.1'
    ],
    cmdclass={
        'sdist': SdistCommand,
        'bdist_wheel': BdistWheelCommand
    }
)