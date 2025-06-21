# Contributing Guidelines

Thank you for your interest in contributing to the Template Documentation project! This guide will help you get started with contributing effectively.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/template-doc.git
   cd template-doc
   ```
3. **Set up the development environment** following the [Installation Guide](../getting-started/installation.md)

## Contribution Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
# or
git checkout -b docs/your-docs-change
```

### 2. Make Your Changes

- Follow the existing code style and conventions
- Write clear, concise documentation
- Test your changes locally with `mkdocs serve`

### 3. Commit Your Changes

We use **Conventional Commits** for all commit messages. This helps us:
- Generate changelogs automatically
- Determine semantic version bumps
- Make the commit history more readable

#### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: add PDF export functionality` |
| `fix` | Bug fix | `fix: resolve navigation menu issue` |
| `docs` | Documentation changes | `docs: update installation guide` |
| `style` | Code style changes | `style: format markdown files` |
| `refactor` | Code refactoring | `refactor: reorganize plugin configuration` |
| `test` | Test changes | `test: add unit tests for PDF export` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `ci` | CI/CD changes | `ci: add GitHub Actions workflow` |
| `perf` | Performance improvements | `perf: optimize build process` |

#### Commit Examples

```bash
# Good commit messages
git commit -m "feat: add Mermaid diagram support"
git commit -m "fix: resolve PDF export Chrome path issue"
git commit -m "docs: add troubleshooting section to installation guide"
git commit -m "style: improve code block formatting"
git commit -m "chore: update MkDocs to version 1.5.3"

# Bad commit messages (avoid these)
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "WIP"
```

#### Breaking Changes

For breaking changes, add `!` after the type:

```bash
git commit -m "feat!: change default theme to dark mode"
```

Or include `BREAKING CHANGE:` in the footer:

```bash
git commit -m "feat: update navigation structure

BREAKING CHANGE: The navigation structure has been completely reorganized.
Users will need to update their bookmarks."
```

### 4. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub with:
- A clear title following conventional commit format
- A detailed description of your changes
- References to any related issues

## Types of Contributions

### Documentation Improvements

- Fix typos and grammatical errors
- Improve clarity and readability
- Add missing documentation
- Update outdated information
- Add examples and tutorials

### Feature Additions

- New MkDocs plugins or extensions
- Enhanced PDF export features
- Improved navigation or search
- New theme customizations

### Bug Fixes

- Fix broken links
- Resolve build issues
- Fix plugin compatibility problems
- Correct configuration errors

### Infrastructure

- CI/CD improvements
- Dependency updates
- Build optimizations
- Testing enhancements

## Code Style Guidelines

### Markdown

- Use ATX-style headers (`#` instead of `===`)
- Include blank lines around headers
- Use fenced code blocks with language specification
- Maintain consistent indentation (2 spaces for lists)

### YAML Configuration

- Use 2-space indentation
- Include comments for complex configurations
- Maintain alphabetical order where appropriate
- Quote strings that contain special characters

### File Organization

```
docs/
├── index.md                    # Main homepage
├── getting-started/            # Getting started guides
│   ├── installation.md
│   ├── quick-start.md
│   └── configuration.md
├── user-guide/                 # User documentation
│   └── ...
├── api/                        # API reference
│   └── ...
├── contributing/               # Contribution docs
│   └── ...
└── assets/                     # Images, diagrams, etc.
    └── ...
```

## Testing

Before submitting your changes:

1. **Test locally**:
   ```bash
   mkdocs serve
   ```

2. **Build the site**:
   ```bash
   mkdocs build
   ```

3. **Test PDF export** (if applicable):
   ```bash
   ENABLE_PDF_EXPORT=1 mkdocs build
   ```

4. **Check for broken links**:
   ```bash
   # Install link checker
   pip install mkdocs-linkcheck
   
   # Run link check
   mkdocs build --config-file mkdocs.yml --strict
   ```

## Pull Request Guidelines

### Before Submitting

- [ ] Changes are tested locally
- [ ] Documentation is updated if needed
- [ ] Commit messages follow conventional format
- [ ] No broken links or build errors
- [ ] Changes are focused and atomic

### Pull Request Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Breaking change

## Testing
Describe how you tested your changes

## Checklist
- [ ] Follows conventional commit format
- [ ] Documentation updated
- [ ] No build errors
- [ ] Tested locally
```

## Review Process

1. **Automated Checks**: CI/CD will run automated tests
2. **Code Review**: Maintainers will review your changes
3. **Feedback**: Address any requested changes
4. **Merge**: Once approved, your PR will be merged

## Getting Help

- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Issues**: Report bugs or request features
- 📧 **Email**: Contact maintainers directly if needed

## Recognition

Contributors are recognized in:
- Git commit history
- Automatic contributor lists (via git-committers plugin)
- Release notes and changelogs

Thank you for contributing to making documentation better for everyone! 🎉
