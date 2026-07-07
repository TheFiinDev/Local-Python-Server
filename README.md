# Local Python HTTP Server

A minimal, zero-dependency multi-threaded HTTP server for local web development.

## Features

- 🌐 **Network Accessible**: Bound to `0.0.0.0` so you can test your website on mobile devices or other computers in the same Wi-Fi network.
- 🚀 **Multi-Threaded**: Uses `ThreadingTCPServer` to handle multiple requests and assets concurrently.
- 🔓 **CORS Enabled**: Sends `Access-Control-Allow-Origin: *` headers for easier API, font, and asset testing.
- 🛠️ **Automatic Port Reuse**: Reduces "Address already in use" errors during quick restarts.
- 📂 **Static File Serving**: Automatically serves HTML, CSS, JavaScript, images, and other static files.

## Usage

1. Clone or download this repository.
2. Open a terminal in the directory containing your website files.
3. Run the server:

   ```bash
   python server.py
   ```
4. Open your browser:
   [http://localhost:8000](http://localhost:8000)

## Access From Other Devices

To access the server from a smartphone, tablet, or another computer:

1. Make sure the device is connected to the same Wi-Fi network.
2. Start the server.
3. Use your computer's local IP address shown in the terminal:
   `http://YOUR_LOCAL_IP:8000`


## Requirements

- Python 3.x
- No external dependencies required

## License

This project is licensed under the MIT License.
