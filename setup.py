from setuptools import setup, find_packages

setup(
    name='email_classifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.25.0',
        'pandas==2.0.3',
        'matplotlib==3.7.1',
        'matplotlib-inline==0.1.6',
        'seaborn==0.12.2',
        'scikit-learn==1.3.0',
        'xgboost==2.1.3',
        'catboost==1.2.7',
        'joblib==1.3.1',
        'pandas-datareader==0.10.0',
        'flask==2.2.3'
    ],
    author="Chandra Kumar R",
    description="A package for classifying emails based on click probability",
    license="MIT"
)
