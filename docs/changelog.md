# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup with comprehensive MkDocs template
- Material for MkDocs theme integration
- Git revision tracking capabilities
- PDF export functionality
- Automatic table of contents generation
- Conventional commit workflow
- Advanced search features
- Mermaid diagram support
- Code syntax highlighting
- Contributing guidelines
- Installation and quick start documentation

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

---

## [1.0.0] - 2024-06-21

### Added
- **MkDocs Configuration**: Complete setup with Material theme
- **Git Integration**: 
  - `git-revision-date-localized-plugin` for automatic page timestamps
  - `git-committers-plugin-2` for contributor tracking
- **PDF Export**: Full PDF generation with `mkdocs-with-pdf`
- **Documentation Structure**:
  - Getting started guides (installation, quick start, configuration)
  - User guide templates
  - API reference templates
  - Contributing guidelines
- **Markdown Extensions**:
  - Admonitions for notes and warnings
  - Code highlighting with line numbers
  - Mermaid diagrams support
  - Math expressions with MathJax
  - Tabbed content and task lists
- **Theme Features**:
  - Dark/light mode toggle
  - Navigation tabs and sections
  - Integrated table of contents
  - Search highlighting
  - Social links integration
- **Development Tools**:
  - Comprehensive `.gitignore`
  - Requirements file with all dependencies
  - Conventional commit guidelines
- **Documentation Content**:
  - Installation instructions
  - Quick start guide
  - Configuration documentation
  - Contributing guidelines with conventional commits

### Technical Details
- **Dependencies**: 13 Python packages including MkDocs 1.5.3+
- **Plugins**: 6 MkDocs plugins for enhanced functionality
- **Extensions**: 15+ Markdown extensions for rich content
- **Theme**: Material for MkDocs with custom configuration
- **PDF Support**: Chrome-based PDF generation
- **Version Control**: Git integration with automatic tracking

### Breaking Changes
- N/A (Initial release)

---

## How to Use This Changelog

This changelog follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format:

### Categories
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** in case of vulnerabilities

### Semantic Versioning
We use [Semantic Versioning](https://semver.org/):
- **MAJOR** version when you make incompatible API changes
- **MINOR** version when you add functionality in a backwards compatible manner
- **PATCH** version when you make backwards compatible bug fixes

### Conventional Commits
Changes are driven by [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` → **Added** section
- `fix:` → **Fixed** section
- `docs:` → **Changed** section (for documentation)
- `style:` → **Changed** section (for formatting)
- `refactor:` → **Changed** section
- `perf:` → **Changed** section
- `test:` → **Changed** section
- `chore:` → **Changed** section
- `BREAKING CHANGE:` → **Changed** section with note

### Links
- [Unreleased]: Compare with latest release
- [1.0.0]: First release tag

---

*This changelog is automatically updated based on conventional commit messages.*
