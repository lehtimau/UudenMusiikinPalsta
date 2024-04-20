# Uuden Musiikin Palsta
Kurssin Tietokannat ja Web-ohjelmointi harjoitustyö

Käytän aiheena kurssimateriaalin esimerkkiä 1, jossa luodaan keskustelupalsta, ja aion lisätä siinä ilmoitetut ominaisuudet.

Keskustelualueen ideana on olla paikka jossa uudet muusikot ja yhtyeet voivat mainostaa keikkoja ja albumeitaan ja muut ihmiset voivat kommentoida
niitä. Palstalla on myös mahdollisuus ostaa ja myydä soittimia ja muita musiikin tekemiseen liittyviä tavaroita. Alueita ovat mainostusalue tuleville keikoille 
ja musiikille, arvostelualue keikoille ja musiikille, myyntialue josta mainitsin aikaisemmin sekä alue johon käyttäjät voivat lähettää musiikkiaan ja kysyä neuvoa.

## Päivitys Välipalautus 3:

Sovellukseen voi nyt admin-oikeuksilla lisätä keskustelualeita ja poistaa ketjuja. Normaalikäyttäjä voi hakea viestejä, lisätä ketjuja ja lähettää viestejä. Seuraavaksi muokkaan ulkoasun lopulliseen kuntoon ja helppokäyttöisemmäksi.

## Asennusohjeet:

Sinulla täytyy olla asennettuna Python3 ja PostgreSQL.

1. Kloonaa tämä repositorio tietokoneellesi

2. Käynnistä PSQL tietokanta komennolla `$ start-pg.sh` . Pidä tietokanta käynnissä koko ajan käyttäessäsi sovellusta.

3. Mene UudenMusiikinPalsta-kansioon ja luo .env-tiedosto joka sisältää:

`DATABASE_URL = <TIETOKANNAN_OSOITE>`
`SECRET_KEY = <SALAINEN_AVAIN>`

4. Luo ja käynnistä virtuaaliympäristö kansiossassi näillä komennoilla:
- `$ python3 -m venv venv`
- `$ source venv/bin/activate`
Tämän jälkeen komentorivisi alkuun pitäisi ilmestyä teksti (venv). 

5. Asenna riippuvuudet:
- `(venv) $ pip install -r requirements.txt`

6. Luo tietokanta:
- `psql < schema.sql`

7. Käynnistä sovellus komennolla `flask run`ja siirry osoitteeseen joka lukee komentorivillä.

8. Sovellus sulkeutuu painamalla Ctrl + C, ja virtuaaliympäristö sulkeutuu komennolla `deactivate`. PSQL tietokanta suljetaan painamalla Ctrl + C.

##Käyttäjällä jolla on admin-oikeudet on mahdollista lisätä uusia keskustelualueita. Saat käyttäjällesi nämä oikeudet kun muokkaat tietokannasta kohdan admin arvoksi t. 