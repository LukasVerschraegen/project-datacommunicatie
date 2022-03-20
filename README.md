# project-datacommunicatie
Dit is een project waarbij we werken met 2 ttgo esp32 modules die we programmeren met micropython.
De ene module bevat een bmp280, deze module bevat de functionaliteit van een temperatuursensor en een barrometer.
De gegevens van deze module worden doorgestuurt via de ingebouwde lora  module op de chip.
Bij de ontvanger krijgen we de data  te zien op het  builtin lora scherm.

We hebben ook nog een windmeter die aangesloten is, deze werkt momenteel nog niet in micropython.
Om de rs485 signalen van de windmeter om te zetten naar seriële data gebruiken we MAXRS485.
Het uitlezen met arduino ging wel.

Alle programma's zijn terug te vinden in main en libraries.
enkel de windmeter is terug te vinden in windmeter test.

Dit is de module die we gebruiken.
![ttgo module](https://user-images.githubusercontent.com/101976886/159165997-53bbe0ab-8899-488d-afb9-a97aff89f193.jpg)

Om dit project na te maken, zie je exact hoe alles verbonden is.
![schema](https://user-images.githubusercontent.com/101976886/159168420-c9ce6742-8636-4b8e-84d3-77c44e850bb1.png)
