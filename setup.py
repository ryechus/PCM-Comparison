from setuptools import setup
setup(name='pcmreader',
	  version='0.1',
	  py_modules=['e3', 'pcmreader'],
	  description="This program takes two files and compares\
	  \ntheir PCM frames over the first second",
	  author="Michael Hardin",
	  install_requires=["audiotools"],
	  dependency_links=[
	  	"https://github.com/ryechus/python-audio-tools/tarball/master#egg=audiotools"
	  ],
      entry_points = {
              'console_scripts': [
                  'pcmreader = pcmreader:main',
              ],
          },
	  )