from setuptools import setup

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.0.1',
    description='Lorem Ipsum Dolor',
    license='MIT',
    py_modules=['{{ cookiecutter.project_name }}'],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_name }}={{ cookiecutter.project_name }}:hello',
         ],
    }
)

