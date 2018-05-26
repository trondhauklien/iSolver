# iSolver
Denne koden vil sammen med robotsett fra Fischertechnik legge grunnlaget for å kunne skanne sudokuer, komme med en gyldig løsning, for så å printe løsningen den kommer fram til. Den bruker Fischertechnik sin TXT-kontroller som hovedprosesseringsenhet, med FTCommunity firmware. "Operativsystemet" er basert på en forenklet linux-versjon, og kan styre blant annet motorer, samtidig som den kan ta input fra sensorer, trykknapper og et kamera. Fordelen med å bruke FTCommunity firmware i dette prosjektet er at man får muligheten til å programmere roboten i Python.

# Innhold
I denne mappen finner du bestanddelene i applikasjonen som kan lastes opp til TXT-kontrolleren, ved hjelp av brukergrensesnittet som er tilgjengelig ved å skrive ip-adressen til TXT-kontrolleren inn i en nettleser.
De øverste mappeelementene er forklart under.

## app
Programkode til iSolver-programmet som kjøres på TXT-kontrolleren.

## utilities
Verktøy som er nyttige ved bruk av iSolver.

# Kilder og referanser
Prosjektet hadde ikke vært mulig uten god hjelp fra GitHub-arkivet til FTCommunity firmware. Programvaren er forklart i en rekke dokumenter, med forskjellige utvidelser og hjelpsomme kodebiter.

[Samleside FTCommunity](https://github.com/ftCommunity)

[Arkiv FTCommunity ROBOTICS TXT firmware](https://github.com/ftCommunity/ftcommunity-TXT)

I tillegg har det tyske forumet av og for FT-samfunnet vært til hjelp.

[FTC Forum](https://forum.ftcommunity.de)

I tillegg må Adrian Rosebrock takkes for mye verdifull kunnskap om datamaskinsyn (Computervision/CV2). I tillegg har han utviklet en Python-pakke med en rekke funksjoner som gjør koding med CV2 litt lettere.

[Nettsiden til Rosebrock](https://www.pyimagesearch.com/)

[Imutils GitHub](https://github.com/jrosebr1/imutils)

Til slutt må også “hari”, en bruker på Stackoverflow, takkes for algoritmen som brukes i iSolver-programmet.

[Algroritmen på Stackoverflow](https://stackoverflow.com/a/20279566)
