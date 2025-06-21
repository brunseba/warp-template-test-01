#!/usr/bin/env python3
"""
Documentation Structure Checker for Template Documentation

This script validates the documentation structure and ensures consistency
between navigation configuration and actual files.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple
import yaml


class DocumentationChecker:
    """Checks documentation structure and consistency."""
    
    def __init__(self, repo_path: Path = Path(".")):
        self.repo_path = repo_path
        self.mkdocs_config_path = repo_path / "mkdocs.yml"
        self.docs_dir = repo_path / "docs"
        self.errors = []
        self.warnings = []
    
    def load_mkdocs_config(self) -> Dict:
        """Load MkDocs configuration."""
        try:
            with open(self.mkdocs_config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"Failed to load mkdocs.yml: {e}")
            return {}
    
    def get_nav_files(self, nav: List) -> Set[str]:
        """Extract file paths from navigation configuration."""
        files = set()
        
        def extract_files(nav_item):
            if isinstance(nav_item, dict):
                for key, value in nav_item.items():
                    if isinstance(value, str) and value.endswith('.md'):
                        files.add(value)
                    elif isinstance(value, list):
                        for item in value:
                            extract_files(item)
            elif isinstance(nav_item, str) and nav_item.endswith('.md'):
                files.add(nav_item)
            elif isinstance(nav_item, list):
                for item in nav_item:
                    extract_files(item)
        
        for item in nav:
            extract_files(item)
        
        return files
    
    def get_actual_docs_files(self) -> Set[str]:
        """Get actual markdown files in docs directory."""
        files = set()
        
        if self.docs_dir.exists():
            for md_file in self.docs_dir.rglob("*.md"):
                relative_path = md_file.relative_to(self.docs_dir)
                files.add(str(relative_path).replace('\\', '/'))
        
        return files
    
    def check_navigation_consistency(self):
        """Check navigation configuration consistency."""
        config = self.load_mkdocs_config()
        
        if 'nav' not in config:
            self.warnings.append("No navigation configuration found in mkdocs.yml")
            return
        
        nav_files = self.get_nav_files(config['nav'])
        actual_files = self.get_actual_docs_files()
        
        # Check for missing files (in nav but not on disk)
        missing_files = nav_files - actual_files
        for missing_file in missing_files:
            self.errors.append(f"Navigation references missing file: {missing_file}")
        
        # Check for orphaned files (on disk but not in nav)
        orphaned_files = actual_files - nav_files
        for orphaned_file in orphaned_files:
            self.warnings.append(f"File exists but not in navigation: {orphaned_file}")
    
    def check_internal_links(self):
        """Check internal markdown links."""
        actual_files = self.get_actual_docs_files()
        
        for md_file in self.docs_dir.rglob("*.md"):
            relative_path = md_file.relative_to(self.docs_dir)
            relative_path_str = str(relative_path).replace('\\', '/')
            
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Find markdown links [text](link)
                link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
                matches = re.findall(link_pattern, content)
                
                for text, link in matches:
                    # Skip external links
                    if link.startswith(('http://', 'https://', 'mailto:', '#')):
                        continue
                    
                    # Handle relative links
                    if link.endswith('.md'):
                        # Calculate target file path
                        current_dir = relative_path.parent
                        target_path = (current_dir / link).resolve()
                        
                        # Make path relative to docs directory
                        try:
                            target_relative = target_path.relative_to(self.docs_dir.resolve())
                            target_str = str(target_relative).replace('\\', '/')
                            
                            if target_str not in actual_files:
                                self.errors.append(
                                    f"Broken link in {relative_path_str}: '{link}' -> {target_str}"
                                )
                        except ValueError:
                            # Path is outside docs directory
                            self.errors.append(
                                f"Link outside docs directory in {relative_path_str}: '{link}'"
                            )
                            
            except Exception as e:
                self.warnings.append(f"Could not check links in {relative_path_str}: {e}")
    
    def check_frontmatter(self):
        """Check YAML frontmatter in markdown files."""
        for md_file in self.docs_dir.rglob("*.md"):
            relative_path = md_file.relative_to(self.docs_dir)
            relative_path_str = str(relative_path).replace('\\', '/')
            
            try:
                content = md_file.read_text(encoding='utf-8')
                
                # Check for frontmatter
                if content.startswith('---\n'):
                    end_pos = content.find('\n---\n', 4)
                    if end_pos != -1:
                        frontmatter = content[4:end_pos]
                        try:
                            yaml.safe_load(frontmatter)
                        except yaml.YAMLError as e:
                            self.errors.append(
                                f"Invalid YAML frontmatter in {relative_path_str}: {e}"
                            )
                    else:
                        self.warnings.append(
                            f"Unclosed frontmatter in {relative_path_str}"
                        )
                        
            except Exception as e:
                self.warnings.append(f"Could not check frontmatter in {relative_path_str}: {e}")
    
    def check_heading_structure(self):
        """Check heading structure and hierarchy."""
        for md_file in self.docs_dir.rglob("*.md"):
            relative_path = md_file.relative_to(self.docs_dir)
            relative_path_str = str(relative_path).replace('\\', '/')
            
            try:
                content = md_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                # Extract headings
                headings = []
                for line_num, line in enumerate(lines, 1):
                    if line.strip().startswith('#'):
                        level = len(line) - len(line.lstrip('#'))
                        if level <= 6:  # Valid heading levels
                            headings.append((line_num, level, line.strip()))
                
                # Check heading hierarchy
                for i, (line_num, level, text) in enumerate(headings):
                    if i == 0 and level != 1:
                        self.warnings.append(
                            f"First heading in {relative_path_str}:{line_num} should be H1, got H{level}"
                        )
                    
                    if i > 0:
                        prev_level = headings[i-1][1]
                        if level > prev_level + 1:
                            self.warnings.append(
                                f"Heading hierarchy skip in {relative_path_str}:{line_num}: "
                                f"H{prev_level} to H{level}"
                            )
                            
            except Exception as e:
                self.warnings.append(f"Could not check headings in {relative_path_str}: {e}")
    
    def check_required_files(self):
        """Check for required documentation files."""
        required_files = [
            'index.md',
            'changelog.md'
        ]
        
        actual_files = self.get_actual_docs_files()
        
        for required_file in required_files:
            if required_file not in actual_files:
                self.errors.append(f"Required file missing: {required_file}")
    
    def check_file_naming(self):
        """Check file naming conventions."""
        for md_file in self.docs_dir.rglob("*.md"):
            filename = md_file.name
            
            # Check for lowercase with hyphens
            if not re.match(r'^[a-z0-9-]+\.md$', filename):
                self.warnings.append(
                    f"File name should use lowercase and hyphens: {md_file.relative_to(self.docs_dir)}"
                )
            
            # Check for spaces in filename
            if ' ' in filename:
                self.errors.append(
                    f"File name contains spaces: {md_file.relative_to(self.docs_dir)}"
                )
    
    def run_all_checks(self) -> bool:
        """Run all documentation checks."""
        print("🔍 Running documentation structure checks...")
        
        self.check_required_files()
        self.check_navigation_consistency()
        self.check_internal_links()
        self.check_frontmatter()
        self.check_heading_structure()
        self.check_file_naming()
        
        # Report results
        if self.errors:
            print("\n❌ Errors found:")
            for error in self.errors:
                print(f"  • {error}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        if not self.errors and not self.warnings:
            print("✅ All documentation structure checks passed!")
        elif not self.errors:
            print(f"✅ No errors found, {len(self.warnings)} warnings")
        else:
            print(f"❌ Found {len(self.errors)} errors and {len(self.warnings)} warnings")
        
        return len(self.errors) == 0


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Check documentation structure")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    
    args = parser.parse_args()
    
    checker = DocumentationChecker()
    success = checker.run_all_checks()
    
    if args.strict and checker.warnings:
        print("\n❌ Strict mode: treating warnings as errors")
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
