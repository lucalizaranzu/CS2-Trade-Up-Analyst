import json
import os
from steamguard import SteamMobile

# Sample dictionary containing usernames and passwords
credentials = {
    "Scrungly2": "jfc93a's81`~fd-7dk3",
    "Scrungly3": "cdk54\"F95'cvS\'f04dD",
    "Scrungly4": "*hD6DJM1~D9v.z3,j",
}

# Function to generate the JavaScript configuration file
def generate_js_file(credentials):
    logins = []

    for username, password in credentials.items():
        # Initialize SteamMobile for each user
        mobile = SteamMobile(username, password)

        # Load the mobile data (ensure you have the appropriate exported data file)
        try:
            mobile_data = mobile.load_exported_data(f'{mobile.account_name}_mobile.json')
            mobile.load_mobile(mobile_data)

            # Generate the Steam Guard code
            guard_code = mobile.generate_steam_guard_code()
        except Exception as e:
            print(f"Error processing user {username}: {e}")
            guard_code = ''  # If there's an error, set the auth to empty

        logins.append({
            'user': username,
            'pass': password,
            'auth': guard_code,  # Include the generated auth code
        })

    js_content = f"""module.exports = {{
    // Configuration for the HTTP API server
    'http': {{
        'port': 80
    }},
    // Whether to trust a forwarding proxy's IP (trust X-Forwarded-For)
    'trust_proxy': false,
    // List of usernames and passwords for the Steam accounts
    'logins': {json.dumps(logins, indent=4)},
    // Optional HTTP/SOCKS5 proxies to auto-rotate for each bot in a round-robin
    'proxies': [],
    // Bot settings
    'bot_settings': {{
        // Amount of attempts for each request to Valve
        'max_attempts': 1,
        // Amount of milliseconds to wait between subsequent requests to Valve (per bot)
        'request_delay': 1100,
        // Amount of milliseconds to wait until a request to Valve is timed out
        'request_ttl': 2000,
        // OPTIONAL: Settings for Steam User (https://github.com/DoctorMcKay/node-steam-user#options-)
        'steam_user': {{}}
    }},
    // Origins allowed to connect to the HTTP/HTTPS API
    'allowed_origins': [
        'http://localhost:3000'
    ],
    // Origins allowed to connect to the HTTP/HTTPS API with Regex
    'allowed_regex_origins': [
        '^http://localhost(:[0-9]+)?$'
    ],
    // Optionally configure a global rate limit across all endpoints
    'rate_limit': {{
        'enable': false,
        'window_ms': 60 * 60 * 1000, // 60 min
        'max': 10000
    }},
    // Logging Level (error, warn, info, verbose, debug, silly)
    'logLevel': 'debug',
    // Max amount of simultaneous requests from the same IP  (incl. WS and HTTP/HTTPS), -1 for unlimited
    'max_simultaneous_requests': 1,
    // Bool to enable game file updates from the SteamDB Github tracker (updated item definitions, images, names)
    'enable_game_file_updates': true,
    // Amount of seconds to wait between updating game files (0 = No Interval Updates)
    'game_files_update_interval': 3600,
    // Postgres connection string to store results in (ex. postgres://user:pass@127.0.0.1:5432/postgres?sslmode=disable)
    'database_url': 'postgres://postgres:Nineone35@localhost:5432/csfloat_data',
    // OPTIONAL: Enable bulk inserts, may improve performance with many requests
    'enable_bulk_inserts': false,
    // OPTIONAL: Key by the caller to allow inserting price information, required to use the feature
    'price_key': '',
    // OPTIONAL: Key by the caller to allow placing bulk searches
    'bulk_key': '',
    // OPTIONAL: Maximum queue size allowed before dropping requests
    'max_queue_size': -1,
}};
"""

    # Save to a .js file in the csfloatinspect/config directory
    js_file_path = os.path.join('csfloatinspect', 'config', 'config.js')

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(js_file_path), exist_ok=True)

    with open(js_file_path, 'w') as js_file:
        js_file.write(js_content)

    print(f"Configuration file saved to {js_file_path}")

    print(js_content)

# Call the function to generate the JS file
generate_js_file(credentials)
