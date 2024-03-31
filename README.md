# stubborn
A Python library that detects version mismatches between code and stub dependencies.
# 🐐 Stubborn

`stubborn` is a Python library designed to detect and manage version mismatches between code and stubs for type-aware programming, particularly focusing on managing dependencies in Poetry projects.


# How to use it

Install `stubborn` with pip:
```bash
pip install git+ssh://git@github.com/agonzalezl/stubborn.git
```

And run it in your poetry project
```bash
python -m stubborn
```

If there is any missmatched version, you will get a result like this one:
```
Dependency issue found:
botocore@1.34.74 vs botocore-stubs@1.32.0
```


# Example usage in Github Workflow for PR comments

Create the file `.github/workflows/main.yml` with the following content:
```yml
name: Stubborn workflow

on:
  pull_request:
    branches: ['*']

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    
    - uses: actions/setup-python@v3
      with:
        python-version: "3.11"
    
    - name: Install dependencies and stubborn
      run: |
        python -m pip install --upgrade pip
        pip install git+http://git@github.com/agonzalezl/stubborn.git

    - name: Get missmatched versions
      # Generate a stubborn report and save it in a file
      run: |
        python -m stubborn >> stubborn-report.txt
        cat stubborn-report.txt

    - name: Check if stubborn file is empty
      id: check_stubborn_file
      run: |
        if [ -s "stubborn-report.txt" ]; then
          echo "isempty=false" >> $GITHUB_OUTPUT
        else
          echo "isempty=true" >> $GITHUB_OUTPUT
        fi

    - name: PR comment
      # Write the result in a PR comment
      uses: thollander/actions-comment-pull-request@bc14ce351a6a25022a490f2be0570c700083a7fe
      if: steps.check_stubborn_file.outputs.isempty != 'true'
      with:
        filePath: stubborn-report.txt
        comment_tag: stubborn-report
```

Read more [here](https://julienrenaux.fr/2019/12/20/github-actions-security-risk/) about why to use commit hash instead of version in Github actions.
