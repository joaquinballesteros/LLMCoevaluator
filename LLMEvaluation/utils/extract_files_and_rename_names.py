import os
import zipfile
import unicodedata
import argparse

def remove_accents(s: str) -> str:
    """
    Remove accents from the input string, returning only ASCII characters.
    """
    nkfd = unicodedata.normalize('NFKD', s)
    return nkfd.encode('ASCII', 'ignore').decode('ASCII')

def extract_and_filter_zip(zip_path: str, dest_root: str, keep_ext: str, delete_names: list):
    """
    Extract the zip file at zip_path into a directory under dest_root named after the
    zip file (without extension and normalized), filtering to only extract files
    with extension keep_ext and excluding files with basenames in delete_names.
    Normalize all filenames by removing accents.
    """
    # Ensure extension starts with a dot
    if keep_ext and not keep_ext.startswith('.'):
        keep_ext = '.' + keep_ext

    base_name = os.path.splitext(os.path.basename(zip_path))[0]
    normalized_base = remove_accents(base_name)
    dest_dir = os.path.join(dest_root, normalized_base)
    os.makedirs(dest_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            # Skip directories for filtering logic but recreate
            path_parts = member.filename.split('/')
            normalized_parts = [remove_accents(part) for part in path_parts if part and part != '.']
            target_path = os.path.join(dest_dir, *normalized_parts)

            # If directory, just recreate
            if member.is_dir():
                os.makedirs(target_path, exist_ok=True)
                continue

            # Filter by basename deletion
            basename = os.path.basename(target_path)
            if basename in delete_names:
                print(f"Deleting by name: {member.filename}")
                continue

            # Filter by extension
            if keep_ext and not basename.lower().endswith(keep_ext.lower()):
                print(f"Skipping (wrong extension): {member.filename}")
                continue

            # Ensure parent directory exists
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            # Extract file
            with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                target.write(source.read())
                print(f"Extracted: {member.filename} -> {target_path}")

    print(f"Processed '{zip_path}' into '{dest_dir}'")

def main():
    parser = argparse.ArgumentParser(
        description="Extract and normalize ZIP files, optionally filtering by extension and file names.")
    parser.add_argument(
        "input_dir",
        help="Directory to search for .zip files")
    parser.add_argument(
        "--output-dir", "-o",
        help="Destination directory for extractions (defaults to input_dir)",
        default=None)
    parser.add_argument(
        "--ext", "-e",
        help="Extension to keep (e.g. .java). If omitted, all extensions are kept.",
        default=None)
    parser.add_argument(
        "--delete-names", "-d",
        nargs='*',
        help="List of file basenames to delete regardless of extension",
        default=[])
    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    output_root = os.path.abspath(args.output_dir) if args.output_dir else input_dir

    for entry in os.listdir(input_dir):
        if entry.lower().endswith('.zip'):
            zip_path = os.path.join(input_dir, entry)
            extract_and_filter_zip(
                zip_path,
                output_root,
                args.ext,
                args.delete_names
            )

if __name__ == "__main__":
    main()

# -e .java will only extract files with the .java extension
# -d Main.java will delete any file named Main.java regardless of its location
# #python extract_files_and_rename_names.py /path/to/folders_with_zips -e .java -d Main.java 
#python extract_files_and_rename_names.py /path/to/folders_with_zips -o /path/to/output_folder -e .java -d Main.java 



