import setuptools

setuptools.setup(
    name="elastic7-doc-manager",
    use_scm_version=True,
    maintainer="mongodb",
    description="Elastic7 plugin for mongo-connector",
    platforms=["any"],
    author="anna herlihy",
    author_email="mongodb-user@googlegroups.com, tharun@nineleaps.com",
    url="https://github.com/tmpaul06/elastic7-doc-manager",
    install_requires=["mongo-connector>=2.5.0", "importlib_metadata"],
    python_requires=">=3.4",
    extras_require=[
        "boto3>=1.4.0",
        "requests-aws-sign>=0.1.2"
        "elasticsearch~7"
    ],
    packages=["mongo_connector", "mongo_connector.doc_managers"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
    ],
    keywords=["mongo-connector", "mongodb", "elastic", "elasticsearch"],
    setup_requires=["setuptools_scm>=1.15"],
)
