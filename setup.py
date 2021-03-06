"""Setup module for catkin_tools_fetch."""
import os
import sys
from stat import ST_MODE
from distutils import log
from setuptools import setup
from setuptools.command.install import install

VERSION_STRING = "0.0.6"

PACKAGE_NAME = "homework_checker"

# Setup installation dependencies
INSTALL_REQUIRES = [
    "ruamel.yaml",
    "schema",
    "setuptools",
    "cpplint",
    "datetime",
]

if sys.version_info[0] == 2 and sys.version_info[1] <= 6:
    INSTALL_REQUIRES.append("argparse")


class PermissiveInstall(install):
    """A class for permissive install."""

    def run(self):
        """Run the install procedure."""
        install.run(self)
        if os.name == "posix":
            for file in self.get_outputs():
                # all installed files should be readable for anybody
                mode = ((os.stat(file)[ST_MODE]) | 0o444) & 0o7777
                log.info("changing permissions of %s to %o" % (file, mode))
                os.chmod(file, mode)


GITHUB_URL = "https://github.com/PRBonn/{}".format(PACKAGE_NAME)

setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=VERSION_STRING,
    install_requires=INSTALL_REQUIRES,
    setup_requires=["nose>=1.0"],
    author="Igor Bogoslavskyi",
    author_email="igor.bogoslavskyi@uni-bonn.de",
    maintainer="Igor Bogoslavskyi",
    maintainer_email="igor.bogoslavskyi@uni-bonn.de",
    keywords=["ipb", "homework-checker"],
    license="Apache 2.0",
    url=GITHUB_URL,
    download_url=GITHUB_URL + "/tarball/" + VERSION_STRING,
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
    description="""A generic homework checker.""",
    long_description=open("README.md").read(),
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "check_homework = homework_checker.check_homework:main",
            "print_repo_name = homework_checker.print_repo_name:main",
        ],
    },
    cmdclass={"install": PermissiveInstall},
)
