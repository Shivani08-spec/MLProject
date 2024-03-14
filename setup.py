# setup script is the centre of all the activity in building, distributing and installing modules using the Distutils.
# thsi file will we responsible in creating my Machine learning application  as a package..


# it will automatically find out all the packages that will be present in the ML aplication that we have created
from setuptools import find_packages  

setup(
name='mlproject',
version='0.0.1',
author='Shivani',
author_email='shivanir03443@gmail.com',
packages=find_packages(),
install_requires=['pandas', 'numpy','seaborn']



)