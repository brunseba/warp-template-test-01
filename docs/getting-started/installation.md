# Installation

This guide will help you set up the documentation environment for the Template Documentation project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: Required for MkDocs and its plugins
- **Git**: For version control and git-based plugins
- **Google Chrome**: Required for PDF export functionality

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/template-doc.git
cd template-doc
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

Test that everything is working correctly:

```bash
mkdocs --version
```

You should see output similar to:
```
mkdocs, version 1.5.3 from /path/to/python/site-packages/mkdocs (Python 3.x)
```

## Additional Setup

### PDF Export Setup

For PDF export functionality, you need:

1. **Google Chrome**: The PDF plugin uses Chrome's headless mode
2. **Environment Variable**: Set `ENABLE_PDF_EXPORT=1` when building

### Git Integration Setup

The git-based plugins require:

1. A properly initialized git repository
2. At least one commit in the repository
3. Proper git configuration (user.name and user.email)

Configure git if not already done:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` when running mkdocs
**Solution**: Ensure you've activated your virtual environment and installed all dependencies

**Issue**: PDF export not working
**Solution**: 
- Verify Google Chrome is installed
- Check the Chrome path in `mkdocs.yml`
- Ensure the `ENABLE_PDF_EXPORT` environment variable is set

**Issue**: Git plugins not working
**Solution**: 
- Ensure you're in a git repository
- Make sure you have at least one commit
- Verify git configuration is set up

### Getting Help

If you encounter issues:

1. Check the [MkDocs documentation](https://www.mkdocs.org/)
2. Review the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
3. Open an issue in the project repository

## Next Steps

Once installation is complete, proceed to the [Quick Start Guide](quick-start.md) to begin using the documentation system.
