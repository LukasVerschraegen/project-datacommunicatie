# project-datacommunicatie
Alle info over dit project vindt u terug in de file weerstation.docx
Dit is een project waarbij we werken met 2 ttgo esp32 modules die we programmeren met micropython in de software Thonny ide versie 3.3.13.
De ene module bevat een bmp280, deze module bevat de functionaliteit van een temperatuursensor en een barrometer.
De gegevens van deze module worden doorgestuurd via de ingebouwde LoRa module op de chip.
Bij de ontvanger krijgen we de data te zien op het builtin OLED scherm.

We hebben ook een windmeter die aangesloten is, deze werkt momenteel niet in micropython.
Om de RS485 signalen van de windmeter om te zetten naar seriële data gebruiken we MAXRS485.
Het uitlezen met arduino is wel gelukt.

Alle programma's zijn terug te vinden in de map main en libraries.
Enkel de windmeter is terug te vinden in de map windmeter test.

Dit is de module die we gebruiken.
![ttgo module](https://user-images.githubusercontent.com/101976886/159165997-53bbe0ab-8899-488d-afb9-a97aff89f193.jpg)

Om dit project te maken, zie je exact hoe alles aangesloten is.
![schema](https://user-images.githubusercontent.com/101976886/159168420-c9ce6742-8636-4b8e-84d3-77c44e850bb1.png)
