## Mål
Underlätta möten genom att ta bort den fysika talare listan.

Medlamer kan nu skicka sitt kort kommando till server och läggas till på talar listan. Detta bygger helt på tillit, det finns ingen form av säkerhelt. Vem som helst kan skicka kan skicka vad som helst och system kommer ta det som input. Exempelvis genom att använda:
echo "<KORT KOMMANDO>" > /dev/udp/<HOST>/<PORT> på sitt linux based os. Vilket då lägger till personen med <KORT KOMMANDO> på talare listan.

## Förbättring potinial
Skriva om i bättre språk, *host* Rust *host* va. Samt skriva extantion för att låta medlem skriva upp sig själv på talar listan, exempel vis genom en hemsida eller command line tool.
