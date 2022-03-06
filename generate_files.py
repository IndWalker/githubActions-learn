import argparse
import json
import pickle

from pathlib import Path


DIR = Path(__file__).parent


def save_data(dag_dependencies, client_name):
    with open(f"{DIR}/data/{client_name}.pkl", "wb") as f:
        pickle.dump(dag_dependencies, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--client_name', type=str, help='Client name that the documentation is generated for')

    client = vars(parser.parse_args())['client_name']

    data = {client: "data"}
    save_data(data, client)
