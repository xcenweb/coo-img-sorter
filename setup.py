import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf8") as f:
    requires = f.read()

setuptools.setup(
    name='coo-img-sorter',
    version='0.0.1',
    license="MIT",
    author="xcenweb",
    author_email="xcenweb@qq.com",
    url="https://github.com/xcenweb/coo-img-sorter",

    keywords=["image", "sorter", "tools"],

    description="an image sorter. 灵活的图片分类工具",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=[
        "coo_img_sorter",
        "coo_img_sorter.util",
    ],

    python_requires=">=3.8",
    platforms=["all"],
    install_requires=requires.splitlines(),
)