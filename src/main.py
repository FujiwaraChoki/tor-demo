import time
import requests

from stem import Signal
from stem import CircStatus
from termcolor import colored
from stem.control import Controller
from stem.response.events import CircuitEvent

def print_circuit_info(controller: Controller):
    """
    Print information about the current Tor circuit(s).

    :param controller: The Tor controller
    :type controller: Controller
    """
    circuit_list = controller.get_circuits()

    circuit_id_list = [circuit.id for circuit in circuit_list if circuit.status == CircStatus.BUILT]

    print(f"{colored('Circuit ID', 'green')}\t{colored('Status', 'green')}\t{colored('Path', 'green')}")
    print("-" * 80)
    for circuit_id in circuit_id_list:
        circuit: CircuitEvent = controller.get_circuit(circuit_id)
        if circuit.status != CircStatus.BUILT:
            continue
        # [1] to use nickname instead of fingerprint
        path = ["".join(controller.get_network_status(entry[1]).address) for entry in circuit.path]
        path_str = "".join(str(path))

        print(f"{str(circuit_id)}\t\t{str(circuit.status)}\t{path_str}")

# Signal TOR for a new connection  (NEWNYM)
def renew_connection():
    """
    Signal TOR for a new connection (NEWNYM).

    :return: None
    :rtype: None
    """
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)

        # wait for the new circuit to be created
        while True:
            if controller.is_newnym_available():
                print_circuit_info(controller)
                break
            else:
                time.sleep(1)

def get_tor_session() -> requests.Session:
    """
    Get a new Tor session.

    :return: A new Tor session
    :rtype: requests.Session
    """
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {
        "http":  "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050"
    }
    return session

rounds = 3

for i in range(rounds):
    print(f"Round {i + 1} of {rounds}")
    renew_connection()
    session = get_tor_session()
    print(colored(session.get("http://httpbin.org/ip").json()["origin"], "green"))
    print("-" * 80)
    session.close()
    time.sleep(5)