# Internet-Speed-Monitor-Pi

A Python-based project for monitoring internet speed using a Raspberry Pi. The script logs speed test results, including ping, download, and upload speeds, to a Google Sheet for easy tracking and analysis.

## Features

- Runs speed tests at regular intervals.
- Logs ping, download, and upload speeds.
- Stores results in a Google Sheet.
- Uses a virtual environment for dependency management.
- Configured to run as a cron job for continuous monitoring.

## Setup

### Prerequisites

- Raspberry Pi with Python 3 installed
- Google API credentials for accessing Google Sheets
- Internet connection

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR-USERNAME/Internet-Speed-Monitor-Pi.git
    cd Internet-Speed-Monitor-Pi
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the Google API credentials:

    - Place your `credentials.json` file in the project directory.
    - Update the `CREDS_FILE` path in the script to point to your `credentials.json` file.

### Usage

1. Run the script manually:

    ```bash
    ./run_speedtest.sh
    ```

2. Schedule the script to run every 5 minutes using cron:

    ```bash
    crontab -e
    ```

    Add the following line:

    ```bash
    */5 * * * * /path/to/your/project/run_speedtest.sh
    ```

### License

This project is licensed under the MIT License.
