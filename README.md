# NxMetaRemover

NxMetaRemover is a command-line tool that allows you to remove metadata from JPEG images.

## Requirements

- Python 3.x
- PIL (Pillow)
- piexif

## Installation

### Clone the repository

```
git clone https://github.com/NxShield/NxMetaRemover.git
cd NxMetaRemover
```

### Install Dependencies

```bash
pip3 install -r requirements.txt
# or
pip3 install pillow piexif
```

## Usage

```bash
python3 nx_meta_remover.py <path-to-your-image.jpg>
```

> Replace `<path-to-your-image.jpg>` with the path to the image you want to process.

### Example

```bash
python3 nx_meta_remover.py example.jpg
```

## Output

The tool will save the processed image in the current directory with the original filename. The original metadata will be removed, and a new copyright notice will be added.


## License

This project is licensed under License - see the [LICENSE](./LICENSE) file for details.
