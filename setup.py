from setuptools import setup, find_packages

setup(
    name='recently_visited_page_middleware',
    version='0.1.1',
    author='Abiola Adeshina',
    author_email='abiolaadeshinaadedayo@gmail.com',
    description='Django middleware for tracking recently visited pages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Abiorh001/recently_visited_page_middleware.git',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
