import qrcode
from pathlib import Path


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter text: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Successfully created! ({file_name})")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def next_filename(prefix="p07_qr", width=4, ext="png"):
        existing = Path(".").glob(f"{prefix}_*.{ext}")

        max_num = -1
        for path in existing:
            try:
                num = int(path.stem.split("_")[-1])
                max_num = max(max_num, num)
            except ValueError:
                continue

        return f"{prefix}_{max_num + 1:0{width}d}.{ext}"


def main():
    myqr = MyQR(size=30, padding=2)
    filename = MyQR.next_filename()
    myqr.create_qr(filename, fg="red", bg="white")


if __name__ == "__main__":
    main()
