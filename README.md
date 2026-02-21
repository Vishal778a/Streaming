# YouTube Thumbnail Generator

Python utilities to download YouTube video thumbnails.

## Scripts

- **thumbnail_generator.py**  
  Download a single YouTube video's thumbnail.

- **multi_thumbnail_generator.py**  
  Batch-download thumbnails from a text file (one URL per line). Saves each batch into a timestamped or custom subfolder under `thumbnails/`.

## Requirements

- Python 3.7+
- `requests` library

### Install

````````
pip install -r requirements.txt
````````

## Usage

### Single Video

Run `thumbnail_generator.py` with the YouTube video URL:

```bash
python thumbnail_generator.py "https://www.youtube.com/watch?v=VIDEOID"
```

- Output: `thumbnails/<VIDEO_ID>.jpg`
- Note: Only URLs with the `v=` query parameter are supported by default.

### Batch (from a text file)

1. Create `urls.txt` with one YouTube URL per line:
    ```
    https://www.youtube.com/watch?v=VIDEOID1
    https://www.youtube.com/watch?v=VIDEOID2
    ```
2. Run:
    ```bash
    # Default: creates a timestamped batch folder
    python multi_thumbnail_generator.py urls.txt

    # Or provide a custom folder name under thumbnails/
    python multi_thumbnail_generator.py urls.txt MyCustomBatchName
    ```
- Output: `thumbnails/<timestamp_or_custom_name>/<VIDEO_ID>.jpg`

## Behavior & Troubleshooting

- The scripts download the `maxresdefault.jpg` thumbnail. If unavailable, a warning is shown; you may try `hqdefault.jpg` manually.
- If you see "❌ Could not extract video ID", ensure the URL contains `v=<11-char id>`. For `youtu.be` or other formats, convert to the long-form URL or update the regex.
- Network issues or rate limits may affect batch downloads.

## Suggested Improvements

- Support for alternate URL formats (e.g., `youtu.be/ID`).
- Automatic fallback to `hqdefault.jpg`.
- Parallel downloads for large batches.

## License

MIT — free to adapt and reuse.

## Repository

- Thumbnails are saved in the `thumbnails/` folder in your project root.
