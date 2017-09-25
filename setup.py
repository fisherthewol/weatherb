from setuptools import setup

setup(name="weatherb",
      license="MIT",
      packages=["weatherb"],
      include_package_data=True
      install_requires=["weatherb",
                        "praw",
                        "urllib",
                        "json"]
)
