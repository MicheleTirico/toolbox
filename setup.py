import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.2',
    python_required="3.10",
    author='Michele Tirico',
    author_mail="tirico.michele@outlook.com",
    description='set of tools for handle files and geo processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MicheleTirico/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/MicheleTirico/toolbox/issues"
    },
    license='MIT',
    packages=['src'],
    install_requires=['requests'],
)