from setuptools import setup, find_packages

setup(
    name="serving-runtime-pytorch",
    version=open("version").read(),
    author="Hydrosphere",
    packages=find_packages(),
    include_package_data=True,
    license="LICENSE.txt",
    install_requires=[
        "hydro-serving-grpc==0.1.4",
        "numpy==1.14.3",
        "torch==0.4.0"
    ],
    test_suites=['tests'],
    tests_require=[
        'pytest', 'pylint', 'requests-mock', 'mock>=2.0.0'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    entry_points={
        'console_scripts': [
            'serve-pytorch=src.main:run'
        ]
    }
)