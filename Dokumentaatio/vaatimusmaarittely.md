# Vaatimusmäärittely

## Sovelluksen tarkoitus

Harjoitustyön tavoitteena olisi saada aikaseksi sovellus, jonka avulla käyttäjä voi hakea tietoa siitä mitä ohjelmointikieli
vaatimuksia/toiveita ohjelmointiin liittyvissä työpaikkailmoituksissa on listattu Duunitori.fi:n sivuilla. Haun jälkeen ohjelma 
voisi muodostaa esimerkiksi pylväskaavion hakutuloksista.

## Käyttäjät

Sovelluksella on vain yksi käyttäjämuoto ilman minkäänlaisia rajoitteita.


## Toiminnallisuus

-Käyttäjä voi suorittaa haun. (tehty)

-Käyttäjä voi pyytää ohjelmaa esittämään hakutulokset yksinkertaisena kaaviona,
joka näyttää lukumäärän jokaisen kielen esiintymästä ilmotuksissa.
Tuloksessa voisi näkyä myös kuinka monta työpaikkailmoitusta haun aikana käytiin läpi. (tehty)

-Käyttäjä voi nollata hakutiedot. (tehty).



### Kehitysideoita

-Haun suorittaminen kestää tällä hetkellä noin 10 minuuttia, joten olisi vielä hyvä
monisäikeistää haun suoritus. Myös käyttöliittymän käyttö pysähtyy haun ajaksi joten olisi myös hyvä
tehdä siitä oma säikeensä, jolloin käyttöliittymää voisi käyttää haun aikana.

-Hakutulokset voisi tallentaa tietokantaan, jonka avulla myös vanhojen hakujen tuloksia
voisi halutessa katsella.

-Hakutulokset voisi tallentaa tietokantaan siihen tapaan, että
ohjelma tarkistaa että edellisestä tehdystä hausta on vähintään 24 tuntia ja
tallentaa hakutulokset sinne vain sen ehdon täyttyessä.
Tällöin ohjelmaan voisi tehdä toiminnallisuuden, joka esittää yhdistetyn koosteen
kaikista tietokantaan tallennetuista hakutuloksista.


