from setuptools import setup

with open('README.rst', 'r') as readme:
    readme_text = readme.read()

setup(
    name='pyseqtest',
    version='1.0.1',
    description='Teste unitário sequencial',
    py_modules=['pyseqtest'],
    author='jaedsonpys',
    author_email='imunknowuser@protonmail.com',
    long_description=readme_text,
    long_description_content_type='text/x-rst'
)
