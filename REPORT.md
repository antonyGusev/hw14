# WiFi Test Report

## Environment Variables

WiFi credentials used by the tests are configured through environment variables:

- `SSID` — WiFi network name.
- `PASSWORD` — WiFi network password.

The framework loads these variables from a `.env` file in the project root using `python-dotenv`.

Create a `.env` file in the project root:

```env
SSID=your_wifi_ssid
PASSWORD=your_wifi_password
```

The resulting project structure should contain:

```text
hw14/
├── .env
├── config.py
├── framework/
├── lib/
├── tests/
└── pyproject.toml
```

The `.env` file is excluded from Git through `.gitignore`, so WiFi credentials are not committed to the repository.

Alternatively, the variables can be set for the current PowerShell session:

```powershell
$env:SSID="your_wifi_ssid"
$env:PASSWORD="your_wifi_password"
```

## Running Tests

Run the complete WiFi regression suite:

```powershell
poe regression
```

The regression task runs the positive tests first and the negative tests second.

Positive tests only:

```powershell
poe positive_tests
```

Negative tests only:

```powershell
poe negative_tests
```

## Test Run Screenshot

![WiFi test run](screenshots/wifi_test_report.png)
