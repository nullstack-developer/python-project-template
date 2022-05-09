# Python Project Template

###Tools

- formatter: black + isort
- linter: flake8
- type checker: mypy
- test: pytest
- command: makefile
- dependency manager: poetry
- logging: logging

### Detail

- poetry
    - pytest
    - pytest-cov
    - isort
        
        ```bash
        profile = "black"
        ```
        
    - black
    - mypy
        
        ```bash
        show_error_context = "True"
        show_column_numbers = "True"
        show_error_codes = "True"
        pretty = "True"
        ```
        
    - flake8
        
        ```bash
        ignore = E203, E266, E501, W503, W605
        max-line-length = 88
        max-complexity = 10
        select = B,C,E,F,W
        per-file-ignores = __init__.py:F401
        exclude = __pycache__, .venv, .git
        ```
        
    - pre-commit
- github action
    - ci-test
    ref : [https://github.com/marketplace/actions/install-poetry-action](https://github.com/marketplace/actions/install-poetry-action)
- pre-commit
    1. hooks
    ref : https://github.com/pre-commit/pre-commit-hooks
        - check-added-large-files
        - check-json
        - check-merge-conflict
        - check-yaml
        - end-of-file-fixer
        - pretty-format-json
        - trailing-whitespace
    2. isort
    3. black
    4. mypy
    5. flake8
    6. pytest
- makefile
    - setup
    - clean
        - rm
            - build dist **.tgz **.egg-info .pytest_cache .mypy_cache __pycache__
    - format
        - isort
        - black
    - typecheck
        - mypy
    - lint
        - flake8
    - test
- .gitmessage.txt
    - udacity git-styleguide
    ref : [https://udacity.github.io/git-styleguide/](https://udacity.github.io/git-styleguide/)
    

추가로 wemakepython, monkeytype 을 고려해보았으나 다음과 같은 이유로 제외하였습니다.

- wemakepython - 너무 엄격합니다. template으로서 자유도를 보장해야하므로 적합하지 않다고 판단하였습니다. 필요시 추가해서 사용하면 됩니다.
- monkeytype - 사용 방법이 불친절합니다.(전체에 적용하는 명령어가 없음) linter, formatter의 역할이 아닙니다. 개발자가 의도하지않은 결과를 출력할 수 있습니다.
