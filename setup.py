import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="auroraandroidappagent",
    version="0.0.1",
    author="sj",
    author_email="songjian@codeorder.cn",
    description="用Python写的管理极光VPN的Android客户端软件。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/songjian/aurora-android-app-agent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.28.1',
        'psutil==5.9.2',
        'uiautomator2==2.16.19'
    ],
    python_requires='>=3'
)