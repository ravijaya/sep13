from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import datetime

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()
builder = x509.CertificateBuilder()

builder = builder.subject_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, 'Simple Test CA'),
]))

builder = builder.issuer_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, 'Simple Test CA'),
]))

one_day = datetime.timedelta(days=1)
today = datetime.datetime.today()
yesterday = today - one_day
next_month = today + (30 * one_day)
builder = builder.not_valid_before(yesterday)
builder = builder.not_valid_after(next_month)
builder = builder.serial_number(x509.random_serial_number())
builder = builder.public_key(public_key)

builder = builder.add_extension(
    x509.BasicConstraints(ca=True, path_length=None),
    critical=True)

certificate = builder.sign(
    private_key=private_key, algorithm=hashes.SHA256(),
    backend=default_backend()
)

private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption())

public_bytes = certificate.public_bytes(
    encoding=serialization.Encoding.PEM)

with open("ca.pem", "wb") as fout:
    fout.write(private_bytes + public_bytes)

with open("ca.crt", "wb") as fout:
    fout.write(public_bytes)

