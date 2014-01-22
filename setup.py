from distutils.core import setup

setup(
    name = "chopbook",
    version = "1.0",
    author = "Dan Macpherson",
    author_email = "dmacpher@redhat.com",
    description = ("Utility tool for uploading Publican books to Pressgang CCMS"),
    license = "LGPL",
    url = "https://github.com/pressgang-ccms/chopbook",
    scripts = ['src/chopbook']
)
