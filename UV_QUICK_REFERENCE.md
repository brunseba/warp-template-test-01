# 🚀 uv Quick Reference Card

## Essential Commands

### Project Setup
```bash
# Clone and setup (new contributors)
git clone <repo-url>
cd template-doc
task setup                    # Full environment setup

# Manual setup
uv sync                       # Install all dependencies
uv sync --extra dev          # Install with dev dependencies
```

### Development Workflow
```bash
task serve                    # Start development server
task build                    # Build documentation
task build-pdf               # Build with PDF export
task clean                    # Clean build artifacts
```

### Dependency Management
```bash
# Add dependencies
task uv-add DEP=requests      # Add production dependency
task uv-add-dev DEP=pytest   # Add development dependency

# Remove dependencies  
task uv-remove DEP=requests   # Remove dependency

# Update dependencies
task update                   # Update all to latest versions
task uv-lock                  # Regenerate lock file
```

### Inspection & Validation
```bash
task uv-tree                  # Show dependency tree
task uv-check                 # Validate dependencies
task stats                    # Show project statistics
task version                  # Show version information
```

### Code Quality
```bash
task pre-commit-install       # Install git hooks
task pre-commit-run          # Run all quality checks
task check                    # Run validation suite
```

### Version Management
```bash
task commit                   # Interactive conventional commit
task changelog               # Generate changelog
task bump                     # Bump version
task bump-dry                # Preview version bump
```

## File Structure

```
template-doc/
├── pyproject.toml           # Modern Python project config
├── uv.lock                  # Dependency lock file
├── .uvignore               # Build exclusions
├── Taskfile.yml            # Task automation
├── .venv/                  # Virtual environment (auto-created)
├── docs/                   # Documentation source
├── site/                   # Built documentation
└── SESSION_SUMMARY.md      # This session's work
```

## Key Benefits

| Feature | Before (pip/venv) | After (uv) |
|---------|------------------|------------|
| **Speed** | ~30s setup | ~5s setup |
| **Resolution** | Single-threaded | Parallel |
| **Lock Files** | Manual pip-tools | Automatic |
| **Virtual Envs** | Manual creation | Auto-managed |
| **Tool Count** | 3+ tools | Single tool |
| **Configuration** | Multiple files | pyproject.toml |

## Dependency Groups

- **Core**: Documentation generation (mkdocs, material theme)
- **Dev**: Development tools (pytest, black, flake8, pre-commit)
- **PDF**: PDF export capabilities (weasyprint)
- **Performance**: Optimization plugins (minify)

## Quick Troubleshooting

```bash
# Environment issues
rm -rf .venv && uv sync      # Recreate environment

# Dependency conflicts
uv lock --upgrade            # Resolve with latest versions

# YAML errors
yamllint Taskfile.yml       # Validate task file

# Build issues
task clean && task build     # Clean rebuild
```

## Migration Notes

### What Changed
- ✅ `requirements.txt` → `pyproject.toml`
- ✅ `pip install` → `uv sync`
- ✅ `python -m venv` → automatic `.venv`
- ✅ `source venv/bin/activate` → `uv run`
- ✅ Python 3.8+ → Python 3.9+

### What Stayed the Same
- ✅ All `task` commands work identically
- ✅ MkDocs configuration unchanged
- ✅ Documentation structure preserved
- ✅ Git workflow maintained
- ✅ Pre-commit hooks functional

---

**💡 Tip**: Use `task help` to see all available commands!
