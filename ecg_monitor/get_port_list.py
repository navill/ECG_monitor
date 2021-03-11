from serial.tools import list_ports


def get_comport_list() -> str:
    comport_set = list_ports.comports()
    for comport in comport_set:
        if 'CP210x' in comport.description:
            return str(comport.device)


