from distutils.core import setup
setup(
  name = 'anti_debug',         # How you named your package folder (MyLib)
  packages = ['anti_debug'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy way to prevent your program from being cracked/decompiled.',   # Give a short description about your library
  author = '6Ex',                   # Type in your name
  author_email = '6exlovesyou@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/0nly6Ex/AntiDebug',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['antidebug', 'crack', 'decompile'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'os',
          'sys',
          'time',
          'httpx',
          'winreg',
          'psutil',
          'threading',
          'subprocess',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
