# Quantium Development Environment Setup

This guide will help you set up your local development environment for the Quantium project.

## Prerequisites

- Python 3.9 installed on your machine
- Git installed on your machine
- A code editor (PyCharm Community Edition recommended, or VS Code, Sublime, etc.)

## Setup Instructions

### 1. Fork and Clone the Repository

1. Fork this repository to your GitHub account
2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/quantium-starter-repo.git
   cd quantium-starter-repo
   ```

### 2. Create a Python 3.9 Virtual Environment

Virtual environments help manage project dependencies in isolation.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies

With your virtual environment activated, install the required packages:

```bash
# Install core dependencies (pandas and dash)
pip install -r requirements.txt

# Install dash testing dependencies
pip install "dash[testing]"
```

This will install:
- **pandas**: Data analysis and manipulation library
- **dash**: Framework for building web applications
- **dash[testing]**: Testing dependencies including selenium, requests, beautifulsoup4, lxml, percy, and waitress

### 4. Verify Installation

Check that packages are installed correctly:
```bash
pip list
```

You should see pandas, dash, and related testing packages in the output.

### 5. Open Project in Your IDE

#### PyCharm Community Edition (Recommended)
1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Open PyCharm and select "Open" to open the project folder
3. Configure the Python interpreter to use your virtual environment:
   - Go to File → Settings → Project → Python Interpreter
   - Click the gear icon → Add
   - Select "Existing environment" and browse to your `venv` folder

#### VS Code
1. Open the project folder in VS Code
2. Install the Python extension if not already installed
3. Select your virtual environment:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your `venv` folder

### 6. Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## Troubleshooting

### Python Version Issues
Make sure you're using Python 3.9. Check your version:
```bash
python --version
```

If you have multiple Python versions, you may need to use `python3.9` explicitly.

### Virtual Environment Not Activating
- On Windows, if you get an execution policy error, run:
  ```bash
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### Package Installation Failures
- Make sure your virtual environment is activated
- Try upgrading pip: `pip install --upgrade pip`
- On some systems, you may need to install additional system dependencies

## Resources

- [Git Book (Chapters 1-2)](https://git-scm.com/book/en/v2)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [PyCharm Documentation](https://www.jetbrains.com/pycharm/learn/)
- [Dash Documentation](https://dash.plotly.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Next Steps

Once your environment is set up, you're ready to start developing!

1. Explore the project structure
2. Check out the data in the `data/` folder
3. Start building your Dash application

Happy coding! 🚀
