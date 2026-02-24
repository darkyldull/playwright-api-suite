# Playwright Test Suite

Automated UI and API tests using Playwright and Python.

![Tests](https://github.com/darkyldull/playwright-api-suite/actions/workflows/tests.yml/badge.svg)

## What's tested

### UI Tests (saucedemo.com)
- Page title validation
- User authentication -> valid and invalid credentials
- Add to cart functionality
- Full checkout flow

### API Tests (restful-booker.herokuapp.com)
- GET booking
- POST create booking
- PUT update booking
- DELETE booking and verify resource is gone

## Tech Stack
- Python
- Playwright
- Pytest
- GitHub Actions (CI)

## Running tests
pip install -r requirements.txt
playwright install
pytest