# Testausdokumentti

[Testikattavuusraportti](coverage_report.txt)


- Voit ajaa testit virtuaaliympäristössä projektin juurikansiossa komennolla pytest


## Testatut Komponentit

### Heuristiset Funktiot

- **Mitä testattiin**: Heuristiset funktiot pelilaudan tilan arviointiin.
- **Testausmenetelmä**: Yksikkötestit jokaiselle heuristiselle funktiolle, jotka tarkistaa, että funktiot antavat oikeat pisteet eri kuvioille.
- **Syötteet**:
  - Erilaiset pelilaudan tilat, jotka edustavat erilaisia pelitilanteita.
  - Siirrot, jotka luovat mahdollisia voittoja tai blokkaavia tilanteita
  - Siirrot, joiden ei kuulu antaa pisteitä
- **Testitulokset**:
- Kaikki heuristiset funktiot läpäisivät omat testinsä.
- Oikeat pisteet mahdollisille voitoille ja puolustaville asemille.


### Minimax-algoritmi
- **Mitä Testattiin**: Minimax-algoritmi Alpha-Beta-karsinnalla.
- **Testausmenetelmä**: Yksikkötestit, jotka tarkistaa algoritmin siirtojen valinnan oikeellisuuden.
- **Syötteet**:
  - Erilaiset pelilaudan tilat, joissa tiedetään optimaaliset siirrot.
  - Ääritapaukset, kuten täydet laudat ja lähellä-voittoa tilanteet.
- **Testitulokset**:
- Minimax-algoritmi tuotti oikeat siirrot tiedossa oleville pelilaudan tiloille.


### Siirtojen Laillisuuden Tarkistus
- **Mitä Testattiin**: Funktiot, jotka määrittävät siirtojen laillisuuden.
- **Testausmenetelmä**: Yksikkötestit, jotka tarkistaa, tunnistetaanko siirrot oikein laillisiksi tai laittomiksi.
- **Syötteet**:
  - Lailliset siirrot eri pelaajasymboleille (esim. "x", "o").
  - Siirrot jo varatuille ruuduille.
- **Testitulokset**:
- Lailliset siirrot tehtiin oikein
- Funktio käsitteli laittomat siirrot oikein.


### Voiton Ehtojen Tarkistus
- **Mitä Testattiin**: Funktiot voittavan pelitilan tarkistamiseksi.
- **Testausmenetelmä**: Yksikkötestit, jotka tarkistaa että oikea pelaaja tunnistetaan voittajaksi tai peli päättyy tasapeliin.
- **Syötteet**:
  - Pelilaudan tilat, joissa on voittavia kuvioita sekä "x" että "o" pelaajille.
  - Pelilaudan tila ilman voittokuvioita, mutta täysi lauta tasapelitilannetta varten.
  - Ääritapaus lähellä voittotilanteita.
- **Testitulokset**:
- Kaikki testit voittavan tilan havaitsemiseksi suoritettiin onnistuneesti.
- Voittavat tilanteet tunnistettiin oikein sekä pelaajille "x" että "o".
- Tasapeli tunnistettiin oikein täydessä pelilaudassa ilman voittajaa.


### Pelisilmukan Testaus
- **Mitä Testattiin**: Pelisilmukan toiminta ja yleinen pelin toiminnallisuus.
- **Testausmenetelmä**: Testitapaukset suunniteltiin simuloimaan erilaisia pelitilanteita oikean pelikulun ja etenemisen varmistamiseksi.
- **Syötteet**:
  - Syötteet virheenkäsittelyn tarkistamiseksi, ja että pelilaudan tila päivittyy oikein siirtojen jälkeen.
- **Testitulokset**:
- Virheenkäsittely toimii oikein
- Pelilaudan tila päivittyy oikein

