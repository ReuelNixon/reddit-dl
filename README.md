# Subreddit Media Downloader

## Description

**reddit-dl** is a command-line tool that allows users to specify a subreddit and download media files from that subreddit. Users can choose the type of media to download (e.g., images, videos) and specify sorting options such as "hot," "top" (with a time filter), or "recent." The tool provides flexibility and convenience for users to fetch media files from their favorite subreddits.

## Features

- Fetch media files (images, videos) from a specified subreddit
- Choose sorting options: "hot," "top" (with time filters: day, week, month, year, all), or "recent"
- Limit the number of media files to download
- Download media files to the user's local machine
- Easy-to-use command-line interface

## Installation

1. Make sure you have Python 3 installed on your system.
2. Install the Subreddit Media Downloader using `pip` by running the following command:
```python
pip install --upgrade reddit-dl
```


## Usage

To use the Subreddit Media Downloader, open a terminal and execute the following command:
```
reddit-dl --subreddit <subreddit_name> --sort <sorting_option> --limit <limit_number>
```


Replace `<subreddit_name>` with the name of the subreddit you want to download media from.
Replace `<sorting_option>` with one of the available sorting options: "hot", "top", or "recent".
Replace `<limit_number>` with the desired limit on the number of media files to download.

The tool will download the media files to your local machine in the current directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

## Contact

For questions or inquiries, feel free to contact the project maintainer:

- Name: Reuel Nixon
- Email: reuelnixon@gmail.com