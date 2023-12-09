import sys
import pyexiv2

def delete_metadata(file_path):
    try:
        metadata = pyexiv2.ImageMetadata(file_path)
        metadata.read()
        metadata.clear()
        metadata.write()
        print(f"Metadata successfully deleted from {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        delete_metadata(file_path)
