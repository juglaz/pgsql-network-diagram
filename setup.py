from setuptools import setup

setup(
    name='pgsql-network-diagram',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    scripts=['sql_pipeline_diagram']                  # The name of your scipt, and also the command you'll be using for calling it
)

setup(name='pgsql-network-diagram',
      description='Parses SQL and builds an interactive table relational diagram using vis.js. Built on sqlparse and focused on PostgreSQL.',
      long_description='Parses SQL and builds an interactive table relational diagram using vis.js. Built on sqlparse and focused on PostgreSQL.',
      version='0.0.1',
      url='https://github.com/juglaz/pgsql-network-diagram',
      author='Alex Bellinson',
      author_email='nosnilleb@gmail.com',
      license='',
      classifiers=[
          'Programming Language :: Python :: 2.7'
      ],
      packages=['pgsql-network-diagram'],
      install_requires=[
          'sqlparse>=0.2.4',
          'json>=2.0.9'
      ],
      entry_points={
          'console_scripts': [
              'sqldiagram=sql_pipeline_diagram.main:run'
          ]
      }
)