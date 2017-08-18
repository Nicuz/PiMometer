# Room Thermometer
Script per la creazione di un piccolo termometro che mostra ora, data, temperatura e umidità con l'utilizzo di un sensore DHT11/DHT22 e un display LCD 16x2 HD44780.

<p align="center">
  <img src="https://github.com/Nicuz/Room_Thermometer/blob/master/images/display_data.jpg"
</p>

**Cablaggio:**

<p align="center">
  <img src="https://github.com/Nicuz/Room_Thermometer/blob/master/images/Raspberry%20Pi%2016x2%20LCD%20HD44780.png"
</p>

**Requisiti:**
* Adafruit_DHT
* Adafruit_CharLCD

**Come avviarlo in background con systemd**

Creare il file di configurazione lanciando:
`sudo nano /lib/systemd/system/NOME.service`

Inserire all'interno del file:
```
[Unit]
Description=DESCRIZIONE DEL SERVIZIO
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/UTENTE/NOME_FILE.py

[Install]
WantedBy=multi-user.target
```
Dare i permessi al file:
`sudo chmod 644 /lib/systemd/system/NOME.service`

Ricarichiamo i demoni e abilitiamo quello appena creato:
```
sudo systemctl daemon-reload
sudo systemctl enable NOME.service
```
Avviamo il nostro demone:
`sudo systemctl start NOME.service`

Controlliamo lo stato:
`sudo systemctl status NOME.service`
