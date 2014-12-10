
from setuptools import setup, find_packages
setup(
    name='django-nocaptcha-recaptcha',
    version='0.0.1',
    description='Django nocaptcha recaptcha form field/widget app.',
    long_description=open('README.md', 'r').read(),
    author='Imaginary Landscape',
    author_email='jjasinski@imgescape.com',
    keywords = ['django', 'recaptcha', 'field', 'nocaptcha'],
    license='BSD',
    url='https://github.com/ImaginaryLandscape/django-nocaptcha-recaptcha',
    packages=find_packages(),
    tests_require=[
        'django-setuptest>=0.1',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)