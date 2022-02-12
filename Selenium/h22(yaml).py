import yaml
import json


def order_number():
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt = templates["invoice"]
        print("The number of order: ", txt)


def sending_address():
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt = templates["bill-to"]["address"]
        print("Sending address:", txt)


def parcel_data():
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt_1 = templates["product"][0]
        print("The first parcel:", txt_1)
        txt_2 = templates["product"][1]
        print("The second parcel:", txt_2)


def convert_to_json():
    in_file = "order.yaml"
    out_file = "order.json"

    with open(in_file, "r") as i:
        data = yaml.safe_load(i)
    with open(out_file, "w") as o:
        json.dump(data, o, indent=4)


def create_yaml():
    yaml_str = """\
    TEST:
        test1: 
            name: ghjk
            release date: 2021-12-4
        test2:
            name: fghjkl
            release date: 2022-12-11
        test3:
            name: xcvbnm
            release date: 2022-12-18

    """

    data = yaml.safe_load(yaml_str)
    print(data)


print(order_number())
print()
print(sending_address())
print()
print(parcel_data())
print()
print(convert_to_json())
print()
print(create_yaml())
