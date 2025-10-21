# check_git_security.py
from pathlib import Path

print("=" * 70)
print("GIT SECURITY CHECK - BEFORE INITIALIZING")
print("=" * 70)

# Files that MUST exist
required_files = {
    '.gitignore': 'Git ignore file',
    'README.md': 'Project documentation',
    '.env.example': 'Environment template',
    'requirements.txt': 'Dependencies',
    'manage.py': 'Django management',
}

# Files that should NOT be committed
dangerous_files = {
    '.env': 'Contains real passwords',
    'db.sqlite3': 'Local database',
}

print("\n✅ REQUIRED FILES:")
all_required = True
for file, desc in required_files.items():
    if Path(file).exists():
        print(f"   ✅ {file:<20} - {desc}")
    else:
        print(f"   ❌ {file:<20} - MISSING! {desc}")
        all_required = False

print("\n🔒 SECURITY CHECK (.gitignore protection):")
if Path('.gitignore').exists():
    with open('.gitignore', 'r') as f:
        gitignore_content = f.read()
    
    checks = {
        '.env': '.env' in gitignore_content,
        'venv/': 'venv/' in gitignore_content,
        '__pycache__/': '__pycache__/' in gitignore_content,
        '*.pyc': '*.pyc' in gitignore_content,
    }
    
    all_protected = True
    for item, is_protected in checks.items():
        if is_protected:
            print(f"   ✅ {item:<20} is protected")
        else:
            print(f"   ❌ {item:<20} NOT in .gitignore - DANGER!")
            all_protected = False
else:
    print("   ❌ .gitignore file NOT FOUND!")
    all_protected = False

print("\n⚠️  DANGEROUS FILES CHECK:")
found_dangerous = False
for file, desc in dangerous_files.items():
    if Path(file).exists():
        print(f"   ⚠️  {file:<20} exists - {desc}")
        print(f"      → Will be ignored by .gitignore (GOOD)")
    else:
        print(f"   ✅ {file:<20} not found (or already protected)")

print("\n" + "=" * 70)

if all_required and all_protected:
    print("✅ READY TO INITIALIZE GIT!")
    print("\nYou can safely run:")
    print("  git init")
else:
    print("❌ FIX ISSUES ABOVE BEFORE INITIALIZING GIT!")
    print("\nDo NOT proceed until all checks pass.")

print("=" * 70)