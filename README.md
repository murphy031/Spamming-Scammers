# Automated Form Filling Script using Selenium

This Python script demonstrates automated form filling using Selenium with concurrent threading. It simulates filling out a web form repeatedly with randomized data. Each thread runs independently to submit the form.

## Prerequisites

1. **Python 3.x**: Make sure Python is installed on your system.
2. **Selenium**: Install Selenium package using `pip install selenium`.
3. **ChromeDriver**: Download ChromeDriver and set its path in the script.
4. **Faker**: Install Faker package using `pip install Faker`.

## Setup Instructions

1. **ChromeDriver Setup**:
   - Download ChromeDriver compatible with your Chrome browser version.
   - Set the absolute path of ChromeDriver in the `setup_mobile_driver()` function.

2. **Dependencies**:
   - Install required Python packages: `pip install selenium Faker`.

3. **Names File**:
   - Create a `names.json` file with an array of names.

## Usage

1. **Customization**:
   - Adjust the `setup_mobile_driver()` function for different browser configurations.
   - Modify form field IDs, XPaths, and other selectors to match your target website.
   - Modify the driver.get() with the website you want to spam
   - Modify the chromedriver_path with where your chromedriver.exe exists

2. **Execution**:
   - Run the script using `python your_script_name.py`.
   - Adjust `num_threads` in `__main__` block to control concurrent form submissions.

## Important Notes

- This script is for educational purposes or testing automation flows.
- Ensure compliance with website terms of service and legal regulations.
- Customize error handling and logging based on your use case.

## License

[MIT License](LICENSE)
