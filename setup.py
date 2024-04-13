from setuptools import setup, find_packages

setup(
    name = 'jogo-da-forca',
    version = '0.2.0',
    author = 'Eric',
    author_email = 'ericshantos13@gmail.com',
    description = 'Minha primeira iniciativa em Python: um jogo-da-forca',
    url = 'https://github.com/ericshantos/jogo-da-forca',
    packages = find_packages(where = 'src'),
    package_dir = {'':'src'},
    install_requires=[
        'forca',
        'sorteio_palavra',
    ],
    scripts = [
        'forca/definicoes_da_forca.py',
        'requisicao_decionario_aberto/requisicao_dicionario_aberto.py'
    ]
)
