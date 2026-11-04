# Playwright UI Automation Framework

[![UI Tests](https://github.com/hamdi-ayedi/playwright-ui-automation/actions/workflows/ui-tests.yml/badge.svg)](https://github.com/hamdi-ayedi/playwright-ui-automation/actions/workflows/ui-tests.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Python-2EAD33.svg)](https://playwright.dev/python/)

End-to-end UI test automation framework built with **Playwright + Python + Pytest**, following the **Page Object Model (POM)** design pattern. Tests run automatically on every push through **GitHub Actions**.

The application under test is [Swag Labs](https://www.saucedemo.com) — a public e-commerce demo site.

## Why this project

This framework mirrors a real QA automation setup used in industry:

- **Page Object Model** — locators and actions live in page classes, so a UI change is fixed in one place, not across every test.
- **Reusable fixtures** — login is centralised in a Pytest fixture and shared across tests.
- **Test markers** — tests are tagged `smoke` and `regression` to run the right subset at the right time.
- **CI/CD** — every push triggers the full suite on GitHub Actions, with an HTML report saved as a build artifact.

## Project structure

```
playwright-ui-automation/
├── pages/                  # Page Object Model
│   ├── base_page.py        # shared navigation helpers
│   ├── login_page.py       # login screen
│   └── inventory_page.py   # products / cart
├── tests/
│   ├── test_login.py       # valid / invalid login scenarios
│   └── test_cart.py        # add-to-cart scenarios
├── .github/workflows/
│   └── ui-tests.yml        # CI pipeline
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Getting started

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install the Playwright browser
playwright install chromium

# 3. Run all tests (headless)
pytest

# Run only smoke tests
pytest -m smoke

# Watch the browser while tests run
pytest --headed
```

An HTML report (`report.html`) is generated after each run.

## Test coverage

| Area  | Scenarios |
|-------|-----------|
| Login | valid login, locked-out user, wrong password |
| Cart  | add single item, add multiple items |

## Tech stack

Python · Playwright · Pytest · pytest-html · GitHub Actions

---

Built by **Hamdi Ayedi** — QA Engineer · [LinkedIn](https://linkedin.com/in/ayedi-hamdi) · [GitHub](https://github.com/hamdi-ayedi)
