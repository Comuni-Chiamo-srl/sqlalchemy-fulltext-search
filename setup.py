"""
SQLAlchemy FullText Search
"""

from setuptools import setup, Command


setup(
        name='SQLAlchemy-FullText-Search',
        version='0.2.6',
        url='https://github.com/Comuni-Chiamo-srl/sqlalchemy-fulltext-search.git',
        license='BSD',
        author='Meng Zhuo, Alejandro Mesa, Comuni-Chiamo',
        author_email='mengzhuo1203@gmail.com, alejom99@gmail.com, matteo@comuni-chiamo.com, davide@comuni-chiamo.com',
        description=('Provide FullText for MYSQL & SQLAlchemy model'),
        long_description = __doc__,
        packages=['sqlalchemy_fulltext'],
        zip_safe=False,
        include_package_data=True,
        platforms='any',
        install_requires=['SQLAlchemy>=1.4',],
            classifiers=[
                        'Environment :: Web Environment',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python :: 2.7',
                        'Programming Language :: Python :: 3.4',
                        'Programming Language :: Python :: 3.6',
                        'Programming Language :: Python :: 3.8',
                        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                        'Topic :: Software Development :: Libraries :: Python Modules']
)
