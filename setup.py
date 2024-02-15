from setuptools import setup, find_packages

setup(
    name='jogo-da-forca',
    version='0.1.0',
    author='Eric',
    author_email='ericshantos13@gmail.com',
    description='Minha primeira iniciativa em Python: um jogo-da-forca',
    url='https://github.com/ericshantos/jogo-da-forca',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any external dependencies here if needed
    ],
    scripts=[
        'src/forca/definicoes_da_forca.py',
        'src/sorteio_palavra/definicoes_sorteio_da_palavra.py',
    ],
)
