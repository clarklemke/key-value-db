from distutils.core import setup

setup(
    name="key-value-db",
    version="0.1",
    description="simple key-value database",
    author="Clark Lemke",
    author_email="clarklemke@gmail.com",
    url="https://github.com/clarklemke/key-value-db",
    py_modules=["keyvaluedb", "server"],
    install_requires=["h11"],
)
