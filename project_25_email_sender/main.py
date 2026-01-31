import smtplib, ssl, certifi
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any
import credentials


def create_image_attachment(path: str) -> MIMEImage:
    # Placeholder
    # raise NotImplementedError("Function not implemented")
    with open(path, "rb") as image:  # read binary
        mime_image = MIMEImage(image.read())
        mime_image.add_header("Content-Disposition", f"attachment; filename={path}")
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = str(credentials.SMTP_ADDRESS)
    port: int = int(credentials.SMTP_PORT)

    # context = ssl.create_default_context(cafile=certifi.where())
    # Python 3.14 running on Windows has an issue with the above command
    context = ssl._create_unverified_context()

    with smtplib.SMTP(host=host, port=port) as server:
        print("Logging in ...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        # Prepare the email
        print("Attempting to send the email...")
        message = MIMEMultipart()
        message["From"] = credentials.EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(
            from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string()
        )

        print("Sent!")


if __name__ == "__main__":
    send_email(
        to_email="arpad.g.bondor@gmail.com",
        subject="Test sending email from Python",
        body="Hello from Python!\nHere's an apple...",
        image="apple.png",
    )
