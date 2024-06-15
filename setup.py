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
    description=' Tex summary NLP application',
    long_description='text/markdon',
    url=f'github.com/martinezreices/text_summarizer',
    project_urls={
        'bug tracker':f'github.com/martinezreices/text_summarizer/issues',
        },
    package_dir=('','src'),
    packages=setuptools.find_packages(where='src')
)

