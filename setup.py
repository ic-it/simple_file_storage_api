from setuptools import find_packages, setup


REQUIREMENTS_FILE = "./requirements.txt"

reqs = [
    r.split("#")[0] for r in map(str.strip, open(REQUIREMENTS_FILE, "r").read().split("\n")) if r
]

setup(
    name="Simple file storage API",
    version="0.0.1",
    author="Illia Chaban",
    install_requires=reqs,
    packages=find_packages(),
    description="Simple file storage written specifically for the AVO-cado-team/chatapi",
    entry_points={
        "console_scripts": ["simple_file_storage_api=simple_file_storage_api.__main__:run"]
    },
)
