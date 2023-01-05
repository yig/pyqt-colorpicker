from setuptools import setup

setup(
    name='labcolorpicker',
    version='1.4.1',
    description='Open a visual LAB colorpicker from any project.',
    long_description='Open a visual LAB colorpicker from any project.\nFor more info visit '
                     'https://github.com/yig/pyqt-colorpicker',
    url='https://github.com/yig/pyqt-colorpicker',
    author='Yotam Gingold',
    author_email='yotam@yotamgingold.com',
    license='MIT',
    packages=['labcolorpicker'],
    install_requires=['qtpy','scikit-image','numpy'],
    keywords=["python", "color", "gui", "colorpicker", "visual"],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)