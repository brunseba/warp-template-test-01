#!/usr/bin/env python3
"""
Automatic Changelog Generator for Template Documentation

This script generates a changelog based on conventional commits.
It analyzes git history and updates the CHANGELOG.md file automatically.
"""

import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import json

# Conventional commit types and their descriptions
COMMIT_TYPES = {
    "feat": {
        "section": "Added",
        "description": "New features",
        "emoji": "✨",
    },
    "fix": {
        "section": "Fixed",
        "description": "Bug fixes",
        "emoji": "🐛",
    },
    "docs": {
        "section": "Documentation",
        "description": "Documentation changes",
        "emoji": "📚",
    },
    "style": {
        "section": "Changed",
        "description": "Code style changes",
        "emoji": "💄",
    },
    "refactor": {
        "section": "Changed",
        "description": "Code refactoring",
        "emoji": "♻️",
    },
    "perf": {
        "section": "Changed",
        "description": "Performance improvements",
        "emoji": "⚡",
    },
    "test": {
        "section": "Changed",
        "description": "Test changes",
        "emoji": "✅",
    },
    "build": {
        "section": "Changed",
        "description": "Build system changes",
        "emoji": "👷",
    },
    "ci": {
        "section": "Changed",
        "description": "CI/CD changes",
        "emoji": "🔧",
    },
    "chore": {
        "section": "Changed",
        "description": "Maintenance tasks",
        "emoji": "🧹",
    },
    "revert": {
        "section": "Changed",
        "description": "Reverted changes",
        "emoji": "⏪",
    },
}

class ConventionalCommit:
    """Represents a conventional commit."""
    
    def __init__(self, commit_hash: str, message: str, date: str, author: str):
        self.hash = commit_hash
        self.raw_message = message
        self.date = date
        self.author = author
        self.parse_message()
    
    def parse_message(self):
        """Parse conventional commit message."""
        # Pattern for conventional commits: type(scope): description
        pattern = r'^(\w+)(?:\(([^)]+)\))?: (.+)$'
        match = re.match(pattern, self.raw_message)
        
        if match:
            self.type = match.group(1)
            self.scope = match.group(2)
            self.description = match.group(3)
            self.is_breaking = '!' in self.type or 'BREAKING CHANGE' in self.raw_message
        else:
            # Fallback for non-conventional commits
            self.type = "chore"
            self.scope = None
            self.description = self.raw_message
            self.is_breaking = False
    
    def get_section(self) -> str:
        """Get the changelog section for this commit."""
        if self.is_breaking:
            return "Breaking Changes"
        return COMMIT_TYPES.get(self.type, COMMIT_TYPES["chore"])["section"]
    
    def get_emoji(self) -> str:
        """Get the emoji for this commit type."""
        return COMMIT_TYPES.get(self.type, COMMIT_TYPES["chore"])["emoji"]
    
    def format_for_changelog(self) -> str:
        """Format commit for changelog entry."""
        scope_text = f"**{self.scope}**: " if self.scope else ""
        breaking_text = "**BREAKING**: " if self.is_breaking else ""
        return f"- {self.get_emoji()} {breaking_text}{scope_text}{self.description} ([{self.hash[:7]}](#{self.hash}))"

class ChangelogGenerator:
    """Generates changelog from git history."""
    
    def __init__(self, repo_path: Path = Path(".")):
        self.repo_path = repo_path
        self.changelog_path = repo_path / "docs" / "changelog.md"
        
    def get_git_commits(self, since_tag: Optional[str] = None) -> List[ConventionalCommit]:
        """Get commits from git history."""
        cmd = ["git", "log", "--pretty=format:%H|%s|%ai|%an"]
        
        if since_tag:
            cmd.append(f"{since_tag}..HEAD")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            commits = []
            
            for line in result.stdout.strip().split('\n'):
                if '|' in line:
                    parts = line.split('|', 3)
                    if len(parts) == 4:
                        commit_hash, message, date, author = parts
                        commits.append(ConventionalCommit(commit_hash, message, date, author))
            
            return commits
        except subprocess.CalledProcessError:
            return []
    
    def get_latest_tag(self) -> Optional[str]:
        """Get the latest git tag."""
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--abbrev=0"],
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return None
    
    def get_version_from_commits(self, commits: List[ConventionalCommit]) -> str:
        """Determine next version based on commit types."""
        if not commits:
            return "0.1.0"
        
        has_breaking = any(commit.is_breaking for commit in commits)
        has_feat = any(commit.type == "feat" for commit in commits)
        
        latest_tag = self.get_latest_tag()
        if latest_tag:
            # Parse semantic version
            version_match = re.match(r'^v?(\d+)\.(\d+)\.(\d+)', latest_tag)
            if version_match:
                major, minor, patch = map(int, version_match.groups())
                
                if has_breaking:
                    major += 1
                    minor = 0
                    patch = 0
                elif has_feat:
                    minor += 1
                    patch = 0
                else:
                    patch += 1
                
                return f"{major}.{minor}.{patch}"
        
        return "0.1.0"
    
    def group_commits_by_section(self, commits: List[ConventionalCommit]) -> Dict[str, List[ConventionalCommit]]:
        """Group commits by changelog section."""
        sections = {}
        
        for commit in commits:
            section = commit.get_section()
            if section not in sections:
                sections[section] = []
            sections[section].append(commit)
        
        return sections
    
    def generate_changelog_entry(self, commits: List[ConventionalCommit], version: str) -> str:
        """Generate a changelog entry for the given commits."""
        if not commits:
            return ""
        
        today = datetime.now().strftime("%Y-%m-%d")
        sections = self.group_commits_by_section(commits)
        
        # Order sections logically
        section_order = [
            "Breaking Changes",
            "Added",
            "Changed", 
            "Fixed",
            "Documentation",
            "Security",
            "Deprecated",
            "Removed"
        ]
        
        entry_lines = [
            f"## [{version}] - {today}",
            ""
        ]
        
        # Add sections in order
        for section_name in section_order:
            if section_name in sections:
                entry_lines.append(f"### {section_name}")
                entry_lines.append("")
                
                for commit in sorted(sections[section_name], key=lambda c: c.date, reverse=True):
                    entry_lines.append(commit.format_for_changelog())
                
                entry_lines.append("")
        
        # Add any remaining sections
        for section_name, section_commits in sections.items():
            if section_name not in section_order:
                entry_lines.append(f"### {section_name}")
                entry_lines.append("")
                
                for commit in sorted(section_commits, key=lambda c: c.date, reverse=True):
                    entry_lines.append(commit.format_for_changelog())
                
                entry_lines.append("")
        
        # Add contributors
        contributors = set(commit.author for commit in commits)
        if contributors:
            entry_lines.append("### Contributors")
            entry_lines.append("")
            for contributor in sorted(contributors):
                entry_lines.append(f"- {contributor}")
            entry_lines.append("")
        
        entry_lines.append("---")
        entry_lines.append("")
        
        return "\n".join(entry_lines)
    
    def read_existing_changelog(self) -> str:
        """Read existing changelog content."""
        if self.changelog_path.exists():
            return self.changelog_path.read_text(encoding="utf-8")
        return ""
    
    def update_changelog(self, new_entry: str):
        """Update the changelog file with new entry."""
        existing_content = self.read_existing_changelog()
        
        # Find the position to insert new entry
        if "## [" in existing_content:
            # Insert before first existing version
            lines = existing_content.split('\n')
            insert_pos = 0
            
            for i, line in enumerate(lines):
                if line.startswith("## [") and "Unreleased" not in line:
                    insert_pos = i
                    break
            
            new_lines = lines[:insert_pos] + new_entry.split('\n') + lines[insert_pos:]
            new_content = '\n'.join(new_lines)
        else:
            # Append to existing content
            header = """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

"""
            new_content = header + new_entry + existing_content
        
        self.changelog_path.write_text(new_content, encoding="utf-8")
    
    def generate_changelog(self, force: bool = False):
        """Generate changelog from recent commits."""
        latest_tag = self.get_latest_tag()
        commits = self.get_git_commits(since_tag=latest_tag)
        
        if not commits and not force:
            print("No new commits found since last tag.")
            return
        
        version = self.get_version_from_commits(commits)
        entry = self.generate_changelog_entry(commits, version)
        
        if entry.strip():
            self.update_changelog(entry)
            print(f"✅ Changelog updated with version {version}")
            print(f"📝 Added {len(commits)} commits to changelog")
        else:
            print("No changelog entry generated (no commits or invalid format)")

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate changelog from conventional commits")
    parser.add_argument("--force", action="store_true", help="Force update even with no new commits")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated without writing")
    
    args = parser.parse_args()
    
    generator = ChangelogGenerator()
    
    if args.dry_run:
        latest_tag = generator.get_latest_tag()
        commits = generator.get_git_commits(since_tag=latest_tag)
        version = generator.get_version_from_commits(commits)
        entry = generator.generate_changelog_entry(commits, version)
        
        print("=== Changelog Entry (Dry Run) ===")
        print(entry)
    else:
        generator.generate_changelog(force=args.force)

if __name__ == "__main__":
    main()
