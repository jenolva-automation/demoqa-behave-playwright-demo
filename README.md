# DemoQA Behave Playwright Demo

A test automation framework demonstrating BDD (Behavior-Driven Development) testing using Behave with Playwright for web automation on the DemoQA website.

## 🚀 Features

- **BDD Testing**: Gherkin feature files with natural language scenarios
- **Playwright Integration**: Fast and reliable web automation
- **Page Object Model**: Maintainable and reusable page components
- **Allure Reporting**: Rich test execution reports with screenshots
- **Cross-browser Support**: Chromium, Firefox, and WebKit support

## 📋 Prerequisites

- Python 3.8+
- Node.js (for Playwright browser installation)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jenolva-automation/demoqa-behave-playwright-demo.git
   cd demoqa-behave-playwright-demo
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   # source venv/bin/activate    # Linux/Mac
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## 🧪 Running Tests

### Run All Tests
```bash
behave features
```

### Run Specific Feature
```bash
behave features\navigate_home.feature
behave features\enter_text.feature
```

### Run with Allure Reporting
```bash
# Run tests with Allure formatter
behave features -f allure_behave.formatter:AllureFormatter -o allure-results

# Generate and serve Allure report
allure generate allure-results -o allure-report --clean
allure serve allure-results
```

### Run with Verbose Output
```bash
behave features --no-capture
```

## 📁 Project Structure

```
demoqa-behave-playwright-demo/
├── features/
│   ├── environment.py              # Test hooks and setup
│   ├── navigate_home.feature       # Home page navigation scenarios
│   ├── enter_text.feature          # Text input form scenarios
│   ├── pages/
│   │   ├── home_page.py            # Home page object model
│   │   ├── elements_page.py        # Elements page object model
│   │   └── textbox_page.py         # Text box form page object model
│   └── steps/
│       ├── navigate_home_steps.py  # Home navigation step definitions
│       ├── enter_textbox_steps.py  # Text box step definitions
│       └── test_step.py            # Additional step definitions
├── allure-results/                 # Test execution results (generated)
├── allure-report/                  # HTML test reports (generated)
├── venv/                          # Python virtual environment
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## 🎯 Test Scenarios

### Navigate Home Feature
- **Scenario**: User navigates to home page
  - Navigate to DemoQA homepage
  - Verify Elements heading is visible

### Enter Text Feature  
- **Scenario**: User navigates to Text Box section
  - Navigate to homepage
  - Click on Elements section
  - Click on Text Box option
  - Verify form fields and submit button are visible

## 🔧 Configuration

### Browser Settings
The framework uses Playwright's Chromium browser by default. Browser configuration is managed in `features/environment.py`:

```python
def before_scenario(context, scenario):
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
```

### Test Data
- **Target URL**: https://demoqa.com
- **Test Environment**: DemoQA Elements section

## 📊 Reporting

### Allure Reports
Generate comprehensive test reports with:
- Test execution timeline
- Step-by-step screenshots
- Error logs and stack traces
- Test statistics and trends

```bash
# Generate static HTML report
allure generate allure-results -o allure-report --clean

# Start local server with live report
allure serve allure-results
```

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'playwright'**
   ```bash
   pip install playwright
   playwright install
   ```

2. **Step definition not found**
   - Ensure step files are in `features/steps/` directory
   - Check for syntax errors in step definitions
   - Clear Python cache: `rm -rf features/steps/__pycache__`

3. **Browser launch issues**
   ```bash
   playwright install chromium
   ```

4. **Environment.py not loading**
   - Ensure `environment.py` is in `features/` directory
   - Check for Python syntax errors
   - Verify hook function names match Behave conventions

### Debug Mode
Run tests with verbose output to see detailed execution:
```bash
behave features --no-capture --verbose
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-test`)
3. Commit your changes (`git commit -am 'Add new test scenario'`)
4. Push to the branch (`git push origin feature/new-test`)
5. Create a Pull Request

## 📝 Dependencies

- **behave**: BDD framework for Python
- **playwright**: Web automation library
- **allure-behave**: Allure reporting integration
- **allure-python-commons**: Allure reporting utilities

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [DemoQA Website](https://demoqa.com)
- [Behave Documentation](https://behave.readthedocs.io/)
- [Playwright Python Documentation](https://playwright.dev/python/)
- [Allure Framework](https://docs.qameta.io/allure/)

---

**Author**: [jenolva-automation](https://github.com/jenolva-automation)  
**Project**: DemoQA Behave Playwright Demo  
**Version**: 1.0.0
