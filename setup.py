from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="price_alert",
    version="1.0.0",
    description="GUI application is used get price alert for amazon and flipkart through email-id",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/Price-Alert",
    author="Akhil",
    author_email="MadeWithPY009@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["PyQt4>=4.11.4","requests>=2.22.0","urllib3>=1.25.9","bs4>=0.0.1"],
    scripts=["price_alert.py"],
    package_data={'data': ['logo.png','icon.ico']},
    include_package_data=True,
)
