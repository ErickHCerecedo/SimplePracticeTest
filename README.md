# SimplePractice Test Automation

Test automation framework for SimplePractice using Selenium and pytest.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Install Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install the following packages:
- `pytest` - Testing framework
- `selenium` - Web automation library
- `webdriver-manager` - Automatic driver management
- `pytest-html` - HTML report generation
- `pytest-xdist` - Parallel test execution
- `python-dotenv` - Environment variable management

## Configuration

### Environment Variables

For security, credentials can be configured using environment variables:

#### Windows (PowerShell)
```powershell
$env:SP_USERNAME="your_email@example.com"
$env:SP_PASSWORD="your_password"
```

#### Windows (CMD)
```cmd
set SP_USERNAME=your_email@example.com
set SP_PASSWORD=your_password
```

#### Linux/Mac
```bash
export SP_USERNAME="your_email@example.com"
export SP_PASSWORD="your_password"
```

#### Using .env file (optional)

If you prefer to use a `.env` file, create one in the project root:

```env
SP_USERNAME=your_email@example.com
SP_PASSWORD=your_password
```

**Note:** The `.env` file is in `.gitignore` and will not be committed to the repository.

## Running Tests

```bash
# Run all tests
pytest

# Run specific test files
pytest tests/test_login.py
pytest tests/test_tasks.py

# Run with markers
pytest -m positive
pytest -m negative

# Run with specific browser
pytest --browser=chrome
pytest --browser=firefox

# Run with detailed output
pytest -v -s
```

## Project Structure

```
SimplePracticeTest/
├── pages/          # Page Object Models
├── tests/          # Test cases
├── utils/          # Utilities
└── reports/        # Test reports
```
