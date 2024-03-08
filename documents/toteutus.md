# Toteutusdokumentti


## 1. Ohjelman Yleisrakenne


### Luokat
- `TicTacToeGame`: Pelisilmukan toiminnasta huolehtiva luokka.
- `Board`: Luokka, joka edustaa pelilautaa ja sisältää metodit pelilaudan tilan hallintaan.
- `Minimax`: Luokka, joka toteuttaa Minimax-algoritmin ja alpha-beta -karsinnan.
- `Heuristic`: Luokka minimaxin siirtojen arviointiin.


## 2. Saavutetut Aika- ja Tilavaativuudet

### Minimax-algoritmi
- Aikavaativuus: 
  - worst-case: O(b^d), missä b on haarojen määrä ja d on haun syvyys.
  - teoreettinen best-case: O(b^d/2)
- Tilavaativuus: O(d), missä d on haun syvyys.


## 4. Työn Mahdolliset Puutteet ja Parannusehdotukset

### Puutteet
- Käyttöliittymä hyvin yksinkertainen.
- Yksikkötestaus voisi olla vielä laajempaa.
- Pelilogiikan optimointi suurempia pelilautoja ja syvyysarvoja varten. Tällä hetkellä osassa syötteitä algoritmin päätöksenteossa saattaa kestää kauan, kun hakusyvyys on 5. Hakusyvyydellä 4 algoritmi ei välttämättä löydä optimaalista siirtoa, eikä tälle ole olemassa virheenkäsittelyä, koska sen toteutus ja testaaminen olisi vaatinut liian paljon aikaa. 

### Parannusehdotukset
- Monipuolisempi arviointi eri siirroille.
- Tehokkaampi siirtojen järjestäminen alpha beta karsintaa varten.
- Mahdollisuus valita pelimerkki ja aloittava pelaaja.
- Mahdollisuus valita pelilaudan koko ja voittorivin pituus käyttäjän toimesta.
- Hienompi käyttöliittymä


## 5. Laajojen kielimallien (ChatGPT yms.) käyttö. 

- Olen käyttänyt ChatGPT:tä:
  - alussa ideointiin
  -  debuggaukseen
  -  kirjoittamaan syötteitä, joilla testata toiminnallisuuksia.
  -  dokumentaation muotoiluun

## 6. Lähteet
1. Alpha–beta pruning - Wikipedia. [Linkki](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
2. Alpha-Beta Pruning - GeeksforGeeks. [Linkki](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)