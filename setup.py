from distutils.core import setup

setup(
        name='integral-ddosa-worker',
        version='1.0',
        py_modules= ['restddosaworker','ddosaauth','ddasentry','ddalogzio','ddalogstash'],
        package_data     = {
            "": [
                "*.txt",
                "*.md",
                "*.rst",
                "*.py"
                ]
            },
        license='Creative Commons Attribution-Noncommercial-Share Alike license',
        long_description=open('README.md').read(),
        )
