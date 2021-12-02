from setuptools import setup

def readme():
    with open('README.md') as file:
        return file.read()

setup(
    name='revclassifier',
    version='0.1',
    description='revclassifier uses online training to provide classes for revenue entries',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU GPLv3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Neural Network :: Classifier',
    ],
    keywords='funniest joke comedy flying circus',
    url='https://github.com/MaKaNu/RevClassifier',
    author='MaKaNu',
    author_email='matti.kaupenjohann@fh-dortmund.de',
    license='GNU GPLv3',
    packages=['revclassifier'],
    zip_safe=False
)