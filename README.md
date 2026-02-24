# Playwright UI Test Suite

Automated end-to-end tests for a web application using Playwright and Python.

## What's tested
- Page title validation
- User authentication (valid and invalid credentials)
- Add to cart functionality
- Full checkout flow

## Tech Stack
- Python
- Playwright
- Pytest
- GitHub Actions (CI)

## Running tests
pip install -r requirements.txt
playwright install
pytest

## CI
Tests run automatically on every push via GitHub Actions.
