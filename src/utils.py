"""Shared utility functions for skeleton page generation."""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def create_directory(path: str) -> None:
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def write_file(path: str, content: str) -> None:
    """Write content to file, creating parent directories if needed."""
    create_directory(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def read_file(path: str) -> str:
    """Read file content."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def file_exists(path: str) -> bool:
    """Check if file exists."""
    return os.path.isfile(path)


def get_file_size(path: str) -> int:
    """Get file size in bytes."""
    return os.path.getsize(path) if file_exists(path) else 0


def sanitize_filename(text: str) -> str:
    """Convert text to valid filename slug."""
    # Convert to lowercase, replace spaces with underscores, remove special chars
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '_', slug)
    return slug.strip('_')


def validate_markdown_syntax(content: str) -> bool:
    """Basic markdown syntax validation."""
    # Check for unclosed code blocks
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        return False
    
    # Check for unclosed emphasis markers
    em_count = content.count('**')
    if em_count % 2 != 0:
        return False
    
    return True


def get_timestamp() -> str:
    """Get current ISO 8601 timestamp."""
    return datetime.now().isoformat()


def get_date_string() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def extract_frontmatter(content: str) -> Dict[str, str]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}
    
    try:
        parts = content.split('---', 2)
        if len(parts) >= 2:
            import yaml
            return yaml.safe_load(parts[1]) or {}
    except Exception:
        pass
    
    return {}


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def extract_headings(content: str) -> List[Dict[str, str]]:
    """Extract all headings from markdown content."""
    headings = []
    lines = content.split('\n')
    
    for line in lines:
        match = re.match(r'^(#+)\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            headings.append({'level': level, 'text': text})
    
    return headings


def validate_heading_hierarchy(headings: List[Dict[str, str]]) -> bool:
    """Validate heading hierarchy (should go 1 -> 2, not skip levels)."""
    if not headings:
        return True
    
    if headings[0]['level'] != 1:
        return False
    
    for i in range(1, len(headings)):
        prev_level = headings[i-1]['level']
        curr_level = headings[i]['level']
        
        # Can stay same, go deeper (+1), or go up any amount
        if curr_level > prev_level + 1:
            return False
    
    return True


def extract_code_blocks(content: str) -> List[Dict[str, str]]:
    """Extract code blocks from markdown."""
    blocks = []
    pattern = r'```(\w*)\n(.*?)\n```'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        language = match.group(1) or 'text'
        code = match.group(2)
        blocks.append({'language': language, 'code': code})
    
    return blocks


def extract_tables(content: str) -> List[List[str]]:
    """Extract markdown tables from content."""
    tables = []
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        if '|' in line:
            table_lines = [line]
            i += 1
            
            # Check for separator row
            if i < len(lines) and '|' in lines[i] and '-' in lines[i]:
                table_lines.append(lines[i])
                i += 1
                
                # Collect table rows
                while i < len(lines) and '|' in lines[i]:
                    table_lines.append(lines[i])
                    i += 1
                
                tables.append(table_lines)
            else:
                i += 1
        else:
            i += 1
    
    return tables


def validate_urls(urls: List[str]) -> Dict[str, bool]:
    """Check if URLs are accessible (returns dict of url -> is_accessible)."""
    try:
        import requests
    except ImportError:
        # requests not available, return all as unknown
        return {url: None for url in urls}
    
    results = {}
    for url in urls:
        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            results[url] = 200 <= response.status_code < 400
        except Exception:
            results[url] = False
    
    return results


def progress_bar(current: int, total: int, label: str = "") -> str:
    """Generate progress bar string."""
    percent = current / total if total > 0 else 0
    filled = int(30 * percent)
    bar = '█' * filled + '░' * (30 - filled)
    return f"{label} [{bar}] {current}/{total} ({percent:.0%})"
