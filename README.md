# Metadata Deletion Script

This Python script allows you to delete metadata from a file using the `pyexiv2` library. Metadata in files can contain information such as author, camera details, and other attributes. Running this script will clear all metadata from the specified file.

## Prerequisites

Before using the script, make sure to install the `pyexiv2` library by running the following command:

```bash
pip install pyexiv2
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/agx-r/metadata-deletion-script.git
   ```

2. Navigate to the script directory:

   ```bash
   cd metadata-deletion-script
   ```

3. Run the script with the following command, providing the path to the file as an argument:

   ```bash
   python delete_metadata.py path/to/your/file.jpg
   ```

   Replace `path/to/your/file.jpg` with the actual path to the file from which you want to delete metadata.

## Note

- Ensure you have proper permissions to modify the specified file.
- Deleting metadata might affect certain aspects of the file, so use this script cautiously.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
