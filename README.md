## Mål

Underlätta möten genom att ta bort den fysika talare listan och där ingen låta medlemar skriva upp sig själva samt se talarlistan.

## Installation

Ladda ner repo genom att tycka upp _code_ och _Download ZIP_, eller genom att

```
git clone https://github.com/Skuggstyret/Digital\_talarlista
```

## Användning

System genom

```
docker-compose -f deployment.yml up
```

Det kräver docker och docker-compose.

Det går att lägga på `-d` flagan för att kör i backgrounden. För att stänga ner så kan man använda

```
docker-compose -f deployment.yml down
```

## Utveckla

Samma som ovan, men för `development.yml`. Detta start backend i development läge vilket ger mer feedback. För att start frontendi development läge, öppna `frontend` och kör.

```
yarn install
```

för att install dependancy samt

```
yarn serve
```

för att start den.

Det kräver att yarn är installerat.

## Förbättring potinial

- Skriva om i bättre språk, _host_ Rust _host_ va.
- Göra web interface mer användarevänligt, samt förmåga att låsa ner men någon typ av lösenord eller använare. <- Extra vilket för kritiska funktion typ dra nästa talare och återställa talarlistan.
- Fixa CI, så att man kan ladda ner image från giten.
