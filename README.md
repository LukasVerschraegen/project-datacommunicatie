# project-datacommunicatie
Dit is een project waarbij we werken met 2 ttgo esp32 modules die we programmeren met micropython.
De ene module bevat een bmp280, deze module bevat de functionaliteit van een temperatuursensor en een barrometer.
De gegevens van deze module worden doorgestuurt via de ingebouwde lora  module op de chip.
Bij de ontvanger krijgen we de data  te zien op het  builtin lora scherm.

We hebben ook nog een windmeter die aangesloten is, deze werkt momenteel nog niet in micropython.
Om de rs485 signalen van de windmeter om te zetten naar seriële data gebruiken we MAXRS485.
Het uitlezen met arduino ging wel.
