from eth_abi_parser import HumanReadableParser


def main():
    parser = HumanReadableParser(
        'event TestEvent(uint indexed id, (string, uint16, (uint8, uint8)) value)')
    print(parser.take_event())

    parser = HumanReadableParser(
        'function doTransferOut(address to, uint amount) external returns (bool success)')
    print(parser.take_function())


if __name__ == '__main__':
    main()
