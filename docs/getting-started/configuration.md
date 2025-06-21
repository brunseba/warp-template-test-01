# Configuration

This guide covers advanced configuration options for customizing your MkDocs documentation site.

## MkDocs Configuration File

The main configuration is in `mkdocs.yml`. This file controls all aspects of your documentation site.

### Site Information

```yaml
site_name: Your Documentation Name
site_description: A brief description of your project
site_author: Your Name
site_url: https://your-domain.com
```

### Repository Settings

```yaml
repo_name: your-username/your-repo
repo_url: https://github.com/your-username/your-repo
edit_uri: edit/main/docs/
```

## Theme Customization

### Color Scheme

The Material theme supports both light and dark modes:

```yaml
theme:
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

Available colors: `red`, `pink`, `purple`, `deep purple`, `indigo`, `blue`, `light blue`, `cyan`, `teal`, `green`, `light green`, `lime`, `yellow`, `amber`, `orange`, `deep orange`, `brown`, `grey`, `blue grey`, `black`, `white`

### Navigation Features

```yaml
theme:
  features:
    - navigation.tabs        # Top-level tabs
    - navigation.sections    # Section grouping
    - navigation.expand      # Expand all sections
    - navigation.path        # Show breadcrumbs
    - navigation.top         # Back to top button
    - search.highlight       # Highlight search terms
    - search.share          # Share search results
    - toc.follow            # Follow TOC while scrolling
    - toc.integrate         # Integrate TOC with navigation
```

## Plugin Configuration

### Git Integration Plugins

#### Git Revision Date

```yaml
plugins:
  - git-revision-date-localized:
      enable_creation_date: true
      type: timeago          # Options: date, datetime, iso_date, iso_datetime, timeago
      timezone: UTC
      locale: en
      fallback_to_build_date: false
      exclude:
        - index.md
```

#### Git Committers

```yaml
plugins:
  - git-committers:
      repository: .
      branch: main
      docs_path: docs/
      exclude:
        - index.md
```

### PDF Export Configuration

```yaml
plugins:
  - with-pdf:
      author: Your Name
      copyright: Copyright © 2024 Your Organization
      cover: true
      back_cover: true
      cover_title: Your Documentation Title
      cover_subtitle: Comprehensive Documentation
      headless_chrome_path: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
      output_path: pdf/documentation.pdf
      enabled_if_env: ENABLE_PDF_EXPORT
```

#### PDF Export Options

- `cover`: Include a cover page
- `back_cover`: Include a back cover
- `headless_chrome_path`: Path to Chrome executable
- `output_path`: Where to save the PDF
- `enabled_if_env`: Environment variable to enable PDF export
- `exclude_pages`: Pages to exclude from PDF
- `two_columns_level`: Heading level for two-column layout
- `ordered_chapter_level`: Heading level for ordered chapters

### Search Configuration

```yaml
plugins:
  - search:
      separator: '[\s\u200b\-_,:!=\[\]()"`/]+|\.(?!\d)|&[lg]t;|(?!\b)(?=[A-Z][a-z])'
      min_search_length: 2
      lang: 
        - en
        - fr  # Add multiple languages
```

## Markdown Extensions

### Core Extensions

```yaml
markdown_extensions:
  - abbr              # Abbreviations
  - admonition        # Note/warning boxes
  - attr_list         # HTML attributes on elements
  - def_list          # Definition lists
  - footnotes         # Footnotes
  - md_in_html        # Markdown inside HTML
  - toc:              # Table of contents
      permalink: true
      title: On this page
```

### PyMdown Extensions

```yaml
markdown_extensions:
  - pymdownx.arithmatex:    # Math expressions
      generic: true
  - pymdownx.betterem:      # Better emphasis
      smart_enable: all
  - pymdownx.caret          # Superscript
  - pymdownx.details        # Collapsible details
  - pymdownx.emoji:         # Emoji support
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
      emoji_index: !!python/name:material.extensions.emoji.twemoji
  - pymdownx.highlight:     # Code highlighting
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite   # Inline code highlighting
  - pymdownx.keys           # Keyboard keys
  - pymdownx.mark           # Text highlighting
  - pymdownx.smartsymbols   # Smart symbols
  - pymdownx.superfences:   # Advanced code blocks
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:        # Tabbed content
      alternate_style: true
  - pymdownx.tasklist:      # Task lists
      custom_checkbox: true
  - pymdownx.tilde          # Strikethrough
```

## Navigation Structure

### Basic Navigation

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quick-start.md
  - User Guide: user-guide/overview.md
```

### Advanced Navigation

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - getting-started/installation.md
    - getting-started/quick-start.md
    - getting-started/configuration.md
  - User Guide:
    - Overview: user-guide/overview.md
    - Features: user-guide/features.md
    - Advanced Usage: user-guide/advanced.md
  - API Reference:
    - Introduction: api/introduction.md
    - Endpoints: api/endpoints.md
    - Examples: api/examples.md
  - Contributing:
    - Guidelines: contributing/guidelines.md
    - Development: contributing/development.md
  - Changelog: changelog.md
```

## Custom CSS and JavaScript

### Adding Custom Styles

1. Create `docs/stylesheets/extra.css`:

```css
/* Custom styles */
.custom-class {
    color: #ff6b6b;
    font-weight: bold;
}

/* Override theme colors */
:root {
    --md-primary-fg-color: #2196f3;
    --md-accent-fg-color: #ff9800;
}
```

2. Reference in `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```

### Adding Custom JavaScript

1. Create `docs/javascripts/custom.js`:

```javascript
// Custom JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Documentation loaded');
    
    // Add custom functionality
    const buttons = document.querySelectorAll('.custom-button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    });
});
```

2. Reference in `mkdocs.yml`:

```yaml
extra_javascript:
  - javascripts/custom.js
```

## Environment Variables

### PDF Export

```bash
# Enable PDF export
export ENABLE_PDF_EXPORT=1
mkdocs build

# Or inline
ENABLE_PDF_EXPORT=1 mkdocs build
```

### Analytics

```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

### Social Links

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/your-username
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/your-handle
    - icon: fontawesome/brands/linkedin
      link: https://linkedin.com/in/your-profile
```

## Advanced Features

### Version Management

Use `mike` for version management:

```yaml
extra:
  version:
    provider: mike
```

Commands:
```bash
# Deploy a version
mike deploy --push --update-aliases 1.0 latest

# Set default version
mike set-default --push latest

# List versions
mike list
```

### Internationalization

For multi-language sites:

```yaml
plugins:
  - i18n:
      languages:
        - locale: en
          name: English
          build: true
        - locale: fr
          name: Français
          build: true
```

### Custom Templates

Create custom templates in `templates/` directory:

```html
<!-- templates/custom.html -->
{% extends "base.html" %}

{% block content %}
<div class="custom-content">
    {{ super() }}
</div>
{% endblock %}
```

## Troubleshooting

### Common Configuration Issues

1. **Plugin not found**: Ensure all plugins are installed via `pip install -r requirements.txt`
2. **PDF export fails**: Check Chrome path and ensure `ENABLE_PDF_EXPORT` is set
3. **Git plugins error**: Ensure you're in a git repository with commits
4. **Build fails**: Check YAML syntax in `mkdocs.yml`

### Validation

Validate your configuration:

```bash
# Check configuration
mkdocs config

# Strict mode (fail on warnings)
mkdocs build --strict

# Clean build
mkdocs build --clean
```

## Performance Optimization

### Build Optimization

```yaml
plugins:
  - minify:
      minify_html: true
      minify_js: true
      minify_css: true
      htmlmin_opts:
        remove_comments: true
        remove_empty_space: true
```

### Search Optimization

```yaml
plugins:
  - search:
      indexing: 'full'  # Options: full, sections, titles
      lang: en
      separator: '[\s\-\.]+'
```

This completes the configuration guide. For more advanced options, refer to the official documentation of each plugin and the MkDocs documentation.
