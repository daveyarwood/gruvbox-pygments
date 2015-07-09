from setuptools import setup, find_packages

setup(name='gruvbox-pygments',
      description='Pygments style using the gruvbox color scheme.',
      packages=find_packages(),
      entry_points="""
                   [pygments.styles]
                   gruvbox = gruvbox.style:GruvboxStyle
                   """
      )
