# Instance Search

- Sovelluksella käyttäjä voi suorittaa haun, joka hakee tietoa siitä mitä ohjelmointikieli-vaatimuksia/toiveita ohjelmointiin liittyvissä työpaikkailmoituksissa on listattu Duunitori.fi:n sivuilla.
- Sovellus suorittaa haun laskemalla löydetyiltä sivuilta eri ohjelmointikielien esiintymiä.
- Haun jälkeen ohjelma voi käyttäjän pyynnöstä esittää pylväskaavion hakutuloksista sekä
tallentaa hakutulokset csv tiedostoon myöhemmin luettavaksi.


### Dokumentaatio
- [Testausdokumentti](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/testaus.md)

- [Arkkitehtuuri](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)

- [vaatimusmäärittely](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimusmaarittely.md)

- [Käyttö ja asennusohje](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/kaytt%C3%B6ohje.md)

### Ohjelman asennus ja testaaminen
Riippuvuudet voi asentaa komennolla:
```bash
poetry install
```

Käynnistys onnistuu komennolla:
```bash
poetry run invoke start
```

### Komentorivin toiminnot

Koodin laadun voi tarkistaa komennolla:
```bash
poetry run invoke lint
```

koodin testauksen voi suorittaa komennolla:
```bash
poetry run invoke test
```

Testikattavauus raportin voi luoda komennolla:
```bash
poetry run invoke coverage-report
```

  
