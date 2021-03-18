from setuptools import setup

setup(
    name="front-end-web-server",
    version="0.1",
    long_description=__doc__,
    packages=["front-end-web-server"],
    include_package_data=True,  # include static and template data specified in MANIFEST.in
    zip_safe=False,  # prevent zip archive creation
    install_requires=["Flask", "pika", "python-dotenv"],
)
