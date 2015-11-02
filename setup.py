from setuptools import setup

setup(name='tester',
      version='0.1.0',
      packages=['tester'],
      install_requires=['invoke'],
      entry_points={
          'console_scripts': ['tester = tester.main:program.run']
      })
