import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

repo_name = 'text_summarizer'
author_user_name = 'martinezreices'
src_repo = 'text_summarizer'
author_email = 'nmr407@gmail.com'

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description='Text summary NLP application',
    long_description='text/markdown',
    url=f'https://github.com/martinezreices/text_summarizer',
    project_urls={
        'Bug Tracker':f'https://github.com/martinezreices/text_summarizer/issues',
        },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)