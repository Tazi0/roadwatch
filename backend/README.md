# Handige SAM commands
- `sam init`
- `sam build`
- `sam deploy`
- `sam build --cached --parallel --skip-pull-image; sam deploy;`
- Synchronize the initial project with a development environment:
  - `sam sync --watch`
  - `sam sync --stack-name "Opdracht4-4" --watch`
- Start monitoring for logs:
  - `sam logs`
  - `sam logs --include-traces --tail`

# Tests
- `pytest`
- Coverage:
  - `coverage run -m pytest`
  - `coverage run --source={app source directory} -m pytest {your unitttest sources} -rap --junitxml target/testreport-app.xml`
  - `coverage xml -o target/coverage-app.xml`
  
  - `coverage run -m pytest -rap --junitxml target/testreport-app.xml && coverage xml -o target/coverage-app.xml`
- Behave:
  - `behave ./tests/features`
  - `behave -f pretty ./tests/features`