# Template Documentation

[![Documentation Status](https://img.shields.io/badge/docs-mkdocs-blue.svg)](https://your-domain.com)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![MkDocs](https://img.shields.io/badge/mkdocs-1.5+-green.svg)](https://mkdocs.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive MkDocs documentation template with advanced features including git revision tracking, PDF export, automatic TOC generation, and conventional commit integration.

## ✨ Features

- **📝 Modern Design**: Built with Material for MkDocs theme
- **🔄 Git Integration**: Automatic revision tracking and contributor information
- **📄 PDF Export**: Generate PDF versions of your documentation
- **📋 Table of Contents**: Automatic TOC generation and navigation
- **🔍 Advanced Search**: Full-text search capabilities
- **📊 Mermaid Diagrams**: Support for flowcharts and diagrams
- **⚡ Fast Building**: Optimized for quick builds and deployments
- **🏷️ Conventional Commits**: Structured commit messages for better changelog generation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- Google Chrome (for PDF export)
- [Task](https://taskfile.dev/#/installation) (optional but recommended)

### Installation

#### Option 1: Using Task (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/template-doc.git
   cd template-doc
   ```

2. **Set up everything with one command**:
   ```bash
   task setup
   ```

3. **Start development server**:
   ```bash
   task serve
   ```

4. **Open your browser** to `http://localhost:8000`

#### Option 2: Manual Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/template-doc.git
   cd template-doc
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start development server**:
   ```bash
   mkdocs serve
   ```

5. **Open your browser** to `http://localhost:8000`

## 📖 Documentation Structure

```
docs/
├── index.md                    # Homepage
├── getting-started/            # Getting started guides
│   ├── installation.md
│   ├── quick-start.md
│   └── configuration.md
├── user-guide/                 # User documentation
│   ├── overview.md
│   ├── features.md
│   └── best-practices.md
├── api/                        # API reference
│   ├── introduction.md
│   └── endpoints.md
└── contributing/               # Contribution guidelines
    ├── guidelines.md
    └── development.md
```

## 🔧 Configuration

### Basic Setup

The main configuration is in `mkdocs.yml`. Key sections include:

- **Site Information**: Name, description, URL
- **Theme Configuration**: Material theme with custom colors
- **Plugins**: Git integration, PDF export, search, etc.
- **Navigation**: Site structure and menu organization

### Git Integration

The template includes two git-based plugins:

1. **git-revision-date-localized**: Shows last update dates
2. **git-committers**: Displays page contributors

These plugins automatically track:
- When pages were last modified
- Who contributed to each page
- Git revision information

### PDF Export

Generate PDF documentation:

```bash
ENABLE_PDF_EXPORT=1 mkdocs build
```

The PDF will be generated at `site/pdf/documentation.pdf`.

### Conventional Commits

This project uses conventional commits for structured commit messages:

```bash
# Examples
git commit -m "feat: add new documentation section"
git commit -m "fix: resolve navigation issue"
git commit -m "docs: update installation guide"
```

## 🔧 Code Quality & Pre-commit

This template includes comprehensive code quality tools and pre-commit hooks for multiple languages:

### Pre-commit Setup

1. **Install pre-commit hooks**:
   ```bash
   task pre-commit-install
   ```

2. **Run checks manually**:
   ```bash
   task pre-commit-run
   ```

### Supported Languages & Tools

- **Python**: Black, isort, flake8, bandit, mypy
- **JavaScript/TypeScript**: ESLint, Prettier
- **CSS/SCSS**: Stylelint
- **Markdown**: markdownlint, prettier
- **YAML/JSON**: yamllint, prettier
- **Shell Scripts**: shellcheck
- **Docker**: hadolint
- **Go**: gofmt, golangci-lint
- **Rust**: rustfmt, clippy
- **Java**: google-java-format
- **SQL**: sqlfluff
- **Security**: detect-secrets

### Automatic Changelog

Generate changelogs automatically from conventional commits:

```bash
# Generate changelog
task changelog-generate

# Preview without writing
task changelog-preview

# Force generation
task changelog-force
```

## 🛠️ Development

### Using Task (Recommended)

This project includes a comprehensive `Taskfile.yml` for easy task management:

```bash
# Show all available tasks
task help

# Quick setup for new contributors
task quick-start

# Start development server
task serve

# Build documentation
task build

# Build with PDF export
task build-pdf

# Run all checks
task check

# Clean build artifacts
task clean
```

#### Key Task Commands

| Task | Description |
|------|-------------|
| `task setup` | Set up development environment |
| `task serve` | Start development server |
| `task build` | Build documentation |
| `task build-pdf` | Build with PDF export |
| `task check` | Run all validation checks |
| `task clean` | Clean build artifacts |
| `task pre-commit-install` | Install pre-commit hooks |
| `task pre-commit-run` | Run code quality checks |
| `task changelog-generate` | Generate changelog from commits |
| `task stats` | Show documentation statistics |
| `task new-page PAGE=path/to/page.md` | Create new page |

### Manual Development

If you prefer not to use Task:

```bash
# Start development server with live reload
mkdocs serve

# Build static site
mkdocs build

# Build with PDF export
ENABLE_PDF_EXPORT=1 mkdocs build
```

### Adding Content

1. Create new Markdown files in the `docs/` directory
2. Add them to the navigation in `mkdocs.yml`
3. Use the development server to preview changes

### Supported Markdown Features

- **Admonitions**: Notes, warnings, tips
- **Code blocks**: Syntax highlighting with line numbers
- **Tables**: Sortable tables with Material theme
- **Mermaid diagrams**: Flowcharts, sequence diagrams, etc.
- **Math expressions**: LaTeX math rendering
- **Tabs and accordions**: Collapsible content sections

## 📦 Dependencies

Key dependencies include:

- `mkdocs` - Static site generator
- `mkdocs-material` - Material theme
- `mkdocs-git-revision-date-localized-plugin` - Git revision tracking
- `mkdocs-git-committers-plugin-2` - Contributor information
- `mkdocs-with-pdf` - PDF export functionality
- `pymdown-extensions` - Additional Markdown extensions

See `requirements.txt` for complete list with versions.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/contributing/guidelines.md) for details.

### Contribution Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Follow conventional commit format
5. Submit a pull request

### Commit Types

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Maintenance tasks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Documentation](https://your-domain.com) - Live documentation site
- [Issues](https://github.com/your-username/template-doc/issues) - Bug reports and feature requests
- [Discussions](https://github.com/your-username/template-doc/discussions) - Community discussions
- [MkDocs](https://www.mkdocs.org/) - Official MkDocs documentation
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Theme documentation

## 🙏 Acknowledgments

- [MkDocs](https://www.mkdocs.org/) - The static site generator
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - The beautiful theme
- [Python-Markdown](https://python-markdown.github.io/) - Markdown processing
- All the plugin authors who make MkDocs extensible

---

**Made with ❤️ using MkDocs and Material for MkDocs**
