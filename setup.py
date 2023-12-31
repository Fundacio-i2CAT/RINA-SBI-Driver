import setuptools

setuptools.setup(
    name='rina',
    version='0.0.3',
    license= 'GNU General Public License version 3',
    author='David Sarabia',
    author_email='david.sarabia@i2cat.net',
    description='rina driver for implementing SDN controller',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",

    ],
    python_requires='>=3.6'
)