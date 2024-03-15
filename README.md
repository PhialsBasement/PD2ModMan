# Payday 2 Mod Manager

## The Payday 2 Mod Manager is a Python script that automates the process of downloading and installing mods for the game Payday 2. It utilizes web scraping techniques to fetch mod information from the ModWorkshop website and provides a user-friendly interface for selecting and installing mods.
Features

    Automatically checks if Payday 2 is installed on your system
    Fetches a list of available mods from the ModWorkshop website
    Allows users to select mods from the list or search for specific mods
    Downloads the selected mods and their dependencies
    Extracts the downloaded mods to the appropriate directories (e.g., mods, assets/mod_overrides)
    Handles both ZIP and RAR file formats for mod archives
    Provides clear instructions and error messages for a smooth user experience

## Prerequisites

    Python 3.x
    Payday 2 installed on your system
    Chrome WebDriver (for web scraping)

## Installation

    Clone the repository or download the script files.
    Install the required Python dependencies by running the following command:
```
    pip install -r requirements.txt
```

    Download the appropriate version of the Chrome WebDriver from the official website: ChromeDriver
    Place the downloaded Chrome WebDriver executable in the project directory or add its path to the system's PATH environment variable.
    Download the unrar executable from the RAR Lab website: RAR Add-ons
    Extract the unrar executable and place it in the bin folder within the project directory.

## Usage

    Run the main.py script using Python:
```
    python main.py
```
    The script will check if Payday 2 is installed on your system. If not found, it will display an error message and exit.
    The script will fetch a list of available mods from the ModWorkshop website and display them.
    Enter the index number of the mod you want to install or enter 99 to search for a specific mod.
    If you choose to search for a mod, enter the search query when prompted.
    The script will download the selected mod and its dependencies, extract them to the appropriate directories, and display the installation progress.
    Once the installation is complete, the script will display a success message.

## Troubleshooting

    If the script fails to find the Chrome WebDriver, make sure it is placed in the project directory or its path is added to the system's PATH environment variable.
    If the script encounters issues while extracting RAR files, ensure that the unrar executable is placed in the bin folder within the project directory.
    If you encounter any other errors or issues, please refer to the error messages displayed by the script and troubleshoot accordingly.

## Contributing

Contributions to the Payday 2 Mod Manager are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, please submit an issue or a pull request on the GitHub repository.
## License

This project is licensed under the MIT License.
## Disclaimer

The Payday 2 Mod Manager is an unofficial tool and is not affiliated with or endorsed by Overkill Software or Starbreeze Studios. Use it at your own risk.
