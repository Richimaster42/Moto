import qrcode

# Información de los mototaxis
mototaxis = [
    {"grupo": "Grupo A", "numero": "001", "url": "https://richimaster42.github.io/Moto/?id=001"},
    {"grupo": "Grupo B", "numero": "002", "url": "https://richimaster42.github.io/Moto/?id=002"},
]

# Generar códigos QR
for mototaxi in mototaxis:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(mototaxi["url"])
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(f"mototaxi_{mototaxi['numero']}.png")

print("Códigos QR generados correctamente.")

