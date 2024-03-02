# Tor Demonstration in Python

This is a simple demonstration of how to use the Tor network in Python. This demonstration uses the `requests` library to make HTTP requests through the Tor network, and the `stem` library to control the Tor process.

## Installation

### Windows

1. Download and install the Tor Browser Bundle from [https://www.torproject.org/](https://www.torproject.org/).
2. Clone the repository and activate the virtual environment:

```bash
git clone https://github.com/FujiwaraChokik/tor-demo.git
cd tor-demo
python -m venv .venv
.venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Linux

1. Install the Tor package:

```bash
sudo apt install tor
```

2. Clone the repository and activate the virtual environment:

```bash
git clone https://github.com/FujiwaraChokik/tor-demo.git
cd tor-demo
python -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Windows

1. Start the Tor Browser Bundle and click on the `Connect` button.
2. Run the script:

```bash
python src/main.py
```

### Linux

1. Start the Tor service:

```bash
sudo service tor start
```

2. Run the script:

```bash
python src/main.py
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [https://stem.torproject.org/](https://stem.torproject.org/)
- [https://www.torproject.org/](https://www.torproject.org/)
- [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
