from setuptools import setup, find_packages

setup(
    name='pyosrd',
    version='0.0.3',
    url='https://github.com/y-plus/pyOSRD.git',
    author='Renan HILBERT',
    author_email='renan.hilbert@gmail.com',
    description='Python package to interact with Open Source Railway Designer',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["*.jar"]},
    python_requires=">=3.10",
    setup_requires=["wheel"],
    install_requires=[
        'networkx >= 3.0',
        'matplotlib>= 3.6.3',
        'pandas',
        "python-dotenv",
        "folium",
        "plotly",
        "haversine",
        "typing-inspect>=0.8.0",
        "typing_extensions>=4.5.0",
        'railjson_generator @ git+ssh://git@github.com/osrd-project/osrd.git#subdirectory=python/railjson_generator',  # noqa
        'ipython',
    ],
)
