#!/usr/bin/env python3
"""Restore and verify index.html from backup file"""

import shutil
import os

def main():
    source = r'C:\Users\32433\Desktop\Ordines Coronationis For Speculum\index.html.bak-precleanup-20260514'
    destination = r'C:\Users\32433\Desktop\Ordines Coronationis For Speculum\index.html'
    
    # Copy the file
    try:
        shutil.copy2(source, destination)
        print('✓ File copied successfully\n')
    except Exception as e:
        print(f'ERROR copying file: {e}')
        return 1
    
    # Verification
    print('=== VERIFICATION ===\n')
    
    # 1. Check file exists and size
    if not os.path.exists(destination):
        print('ERROR: File not found after copy!')
        return 1
    
    size_bytes = os.path.getsize(destination)
    print('1. File Status:')
    print(f'   - Exists: YES')
    print(f'   - Size: {size_bytes:,} bytes')
    
    # 2. Check closing tags
    print('\n2. Closing Tags:')
    try:
        with open(destination, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        has_close_script = '</script>' in content
        has_close_body = '</body>' in content
        has_close_html = '</html>' in content
        
        print(f'   - Contains </script>: {has_close_script}')
        print(f'   - Contains </body>: {has_close_body}')
        print(f'   - Contains </html>: {has_close_html}')
        
        if not (has_close_script and has_close_body and has_close_html):
            print('   ERROR: Missing one or more closing tags!')
            return 1
    except Exception as e:
        print(f'ERROR reading file: {e}')
        return 1
    
    # 3. Show last 300 characters
    print('\n3. Last 300 Characters:')
    print('   ' + '-' * 76)
    last_300 = content[-300:]
    for line in last_300.split('\n'):
        if line:
            print('   ' + line)
    print('   ' + '-' * 76)
    
    print('\n✓ Restoration and verification complete!')
    return 0

if __name__ == '__main__':
    exit(main())
