import os
import hashlib
import argparse

# Function to compute hash of a file in chunks to handle large files
def compute_hash(file_path: str, algorithm: str = 'sha256', chunk_size: int = 8192) -> str:
    """
    Compute and return the hexadecimal hash of a file using the specified algorithm.
    """
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Main function to scan directories and detect duplicate files
def find_duplicates(root_dir: str, algorithm: str = 'sha256') -> dict:
    """
    Traverse root_dir, compute hashes for all files, and return a dictionary mapping
    each hash to the list of file paths that share that hash.
    """
    duplicates = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_hash = compute_hash(file_path, algorithm)
            except (PermissionError, FileNotFoundError) as e:
                print(f"Warning: could not read {file_path}: {e}")
                continue
            duplicates.setdefault(file_hash, []).append(file_path)
    return {h: paths for h, paths in duplicates.items() if len(paths) > 1}

# CLI interface
def main():
    parser = argparse.ArgumentParser(
        description="Scan a directory tree and report files with identical contents across subdirectories.")
    parser.add_argument(
        'root_dir',
        help='Path to the directory containing student code folders')
    parser.add_argument(
        '--algo', '-a',
        choices=hashlib.algorithms_available,
        default='sha256',
        help='Hash algorithm to use (default: sha256)')
    args = parser.parse_args()

    duplicates = find_duplicates(args.root_dir, args.algo)
    if not duplicates:
        print("No duplicate files found.")
        return

    print("Duplicate files detected:\n")
    for file_hash, paths in duplicates.items():
        print(f"Hash: {file_hash}")
        for p in paths:
            print(f"  - {p}")
        print()

if __name__ == '__main__':
    main()

#python find_duplicate_files.py /path/students/ --algo sha256
