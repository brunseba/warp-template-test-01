# Template Documentation

Welcome to the **Template Documentation** project! This is a comprehensive MkDocs template designed to help you create professional documentation with advanced features.

## Features

This documentation template includes:

- **📝 Modern Design**: Built with Material for MkDocs theme
- **🔄 Git Integration**: Automatic revision tracking and contributor information
- **📄 PDF Export**: Generate PDF versions of your documentation
- **📋 Table of Contents**: Automatic TOC generation and navigation
- **🔍 Advanced Search**: Full-text search capabilities
- **📊 Mermaid Diagrams**: Support for flowcharts and diagrams
- **⚡ Fast Building**: Optimized for quick builds and deployments

## Quick Start

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the development server:
   ```bash
   mkdocs serve
   ```

3. Open your browser to `http://localhost:8000`

## Building Documentation

### Development
```bash
mkdocs serve
```

### Production Build
```bash
mkdocs build
```

### PDF Export
```bash
ENABLE_PDF_EXPORT=1 mkdocs build
```

## Project Structure

```
template-doc/
├── docs/                   # Documentation source files
│   ├── getting-started/    # Getting started guides
│   ├── user-guide/         # User documentation
│   ├── api/               # API reference
│   └── contributing/      # Contribution guidelines
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies
└── README.md             # Project README
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](contributing/guidelines.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*This documentation was built with ❤️ using [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).*
