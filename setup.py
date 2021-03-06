from setuptools import setup
from setuptools import find_packages

setup(
    name='ehr-code-mappings',
    packages=find_packages(),
    version='0.1.0',
    license='MIT',
    description='A library for EHR code mappings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Filip Dabek',
    url='https://github.com/fdabek1/ehr-code-mappings',
    download_url='https://github.com/fdabek1/ehr-code-mappings/archive/v0.1.0.tar.gz',
    keywords=['ehr', 'icd', 'codes', 'mappings', 'mapping'],
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
