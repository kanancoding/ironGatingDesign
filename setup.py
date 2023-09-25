from setuptools import setup, find_packages


setup(
    name='ironGatingDesign',
    version='0.1.0',
    license='MIT',
    author="Anan Khongchuai",
    author_email='anankh2025@gmail.com',
    packages=['ironGatingDesign'],
    # packages=find_packages('src'),
    # package_dir={'': 'src'},
    url='https://github.com/kanancoding/ironGatingDesign',
    keywords='gating design',
    install_requires=[
          'numpy',
      ],

)