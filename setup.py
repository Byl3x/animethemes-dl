import setuptools
with open("README.md", "r") as f:
    long_description = f.read()
setuptools.setup(
        name="animethemes-dl",
        author="thesadru",
        author_email="", # add email
        version="git", #change to current version
        keywords=["anime", "download", "op", "ed"],
        long_description_content_type="text/markdown",
        description="Downloads anime themes from theme.moe using an animethemes-api. Supports Batch download and MAL connecting.",
        python_requires=">=3.6",
        license="MIT",
        install_requires=["pySmartDl", "eyed3", "requests", "colorama"],
        scripts=['animethemes-dl'],
        py_modules=["printer", "downloader", "globals", "animethemes"],
        )
