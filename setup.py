from setuptools import setup, find_packages

setup(
    name='DUD-E Classifier',
    version='0.0.1',
    description='Basic ML Methods for classifying DUD-E Data',
    license='BSD 3-clause license',
    maintainer='AndreiRoibu, Jakke-Neiro',
    maintainer_email='andrei-claudiu.roibu@dtc.ox.ac.uk, jakke.neiro@dtc.ox.ac.uk',
    install_requires=[
        'numpy',
        'matplotlib',
	    'scikit-learn',
	    'ipython',
        'pandas',
        'jupyter'
    ],
)
