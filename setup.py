from setuptools import setup
from pathlib import Path

AUTHOR = "Jitendra Mishra"
AUTHOR_EMAIL = "jitendra29mishra@gmail.com"
URL = "https://github.com/jmishra01/Custom-button-in-Matplotlib-toolbar"
DOWNLOAD_URL = ""
CURRENT_DIRECTORY = Path(__file__).parent
long_description = (CURRENT_DIRECTORY / "README.md").read_text()
KEYWORDS = ['matplotlib', 'toolbar', 'tkinter', 'qt']

setup(
  name = 'custom_tool_button',
  packages = ['custom_tool_button'],
  version = '0.2',
  license='MIT',
  description=long_description,
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = AUTHOR,
  author_email = AUTHOR_EMAIL,
  url = URL,
  download_url = DOWNLOAD_URL,
  keywords = KEYWORDS,
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
