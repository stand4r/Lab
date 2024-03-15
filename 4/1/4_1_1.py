class PacketTransmission:
    MIN_PACKET_SIZE = 32  # Минимальный размер пакета в байтах
    MAX_PACKET_SIZE = 32 * 1024  # Максимальный размер пакета в байтах (32 Кбайт)

    def __init__(self, message_size, packet_size):
        self.message_size = self._convert_to_bytes(message_size)
        self.packet_size = self._validate_packet_size(self._convert_to_bytes(packet_size))

    @staticmethod
    def _convert_to_bytes(size):
        units = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}
        try:
            value, unit = size.split()
            value = int(value) * units[unit.upper()]
        except ValueError:
            # Если единица измерения не указана, считаем значение введенным в байтах.
            value = int(size)
        return value

    def _validate_packet_size(self, size):
        if size < self.MIN_PACKET_SIZE or size > self.MAX_PACKET_SIZE:
            raise ValueError("Packet size out of allowed range (32 bytes - 32 KB).")
        return size

    def set_packet_size(self, packet_size):
        self.packet_size = self._validate_packet_size(self._convert_to_bytes(packet_size))

    def change_packet_size(self, change):
        new_size = self.packet_size + self._convert_to_bytes(change)
        self.packet_size = self._validate_packet_size(new_size)

    def calculate_needed_packets(self):
        return -(-self.message_size // self.packet_size)  # Округление вверх


if __name__ == "__main__":
    try:
        transmission = PacketTransmission(message_size="34051", packet_size="2 KB")
        print("Число пакетов для передачи:", transmission.calculate_needed_packets())
        transmission.change_packet_size("1 KB")
        print("После увеличения размера пакета на 1 KB, число пакетов для передачи:", transmission.calculate_needed_packets())

        transmission2 = PacketTransmission(message_size="25 MB", packet_size="1 KB")
        print("\nДля сообщения 25 MB и размера пакета 1 KB, число пакетов:", transmission2.calculate_needed_packets())

    except ValueError as e:
        print(e)