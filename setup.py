from setuptools import setup, find_packages

setup(
    name="korean_noise_augmentation",
    version="0.1.0",
    description="Korean noise generator",
    url="https://github.com/oh-gnues-iohc/korean-noise-augmentation",
    author_email="choiseungho1019@gmail.com",
    license="Apache License",
    packages=find_packages(),
    install_requires=["tqdm"]
)

