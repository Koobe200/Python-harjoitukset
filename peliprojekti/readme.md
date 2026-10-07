# U-juna

Tekstiseikkailupeli, jossa yrität päästä U-junalla Kirkkonummelta Helsinkiin.

## Idea ja tavoite

Pelaaja aloittaa Kirkkonummelta ja pitää päästä opiskelijatapahtuma Helsinkiin.
Tavoite on pysyä junassa koko matka ja ehtiä perille ennen kuin 120 minuuttia loppuu. 
Junan mennessä eteenpäin, pelaaja kohtaa eri haasteita,jotka vievät aikaa tai muuttavat pelaajan ystävällisyyttä. 
Pelaajan valinnat johtavat tulokseen, mitä seuraavilla asemilla tapahtuu.

## Käynnistys

--------------
python main.py

Peli kysyy ensin nimen ja iän. Pelaajan pitää olla vähintään 12-vuotias.

## Pelin kulku

Päävalikko:

1. Uusi peli
2. Jatka tallennuksesta
3. Ohjeet
4. Lopeta

Pelaaja pelaa seuraavat asemat läpi:Kirkkonummi, espoo, leppävaara, helsinki

pelaajalla on kaksi arvoa:

**Aika**: alussa 120 minuuttia. Jos aika loppuu, peli päättyy häviöön.
**Ystävällisyys**: nousee kun pelaaja auttaa muita ja laskee kun hän on ilkeä. 

Pisteet lasketaan lopussa: jäljellä oleva aika + ystävällisyys x 10. Tulokset
kirjoitetaan tiedostoon tulokset.txt.

## Reitit

**Kirkkonummella** arvotaan, milloin juna lähtee. Siitä lähtee eri reittejä, reitit muokkaantuu sen mukaan mitä eri päätöksiä eri asemilla tekee:
Kävely: juna lähtee yli 23 minuutin päästä, 
Kyydin pummiminen: pelaajalla on kiire ja yrittää saada kyydin. Kolme yritystä, joista
jokainen vie 10 minuuttia. Jos kyytiä ei tule, peli päättyy.
Pyörävarkaus: nopein tapa, mutta HSL-lippu tippuu ja ystävällisyys laskee.

**Espoo**: ilman pyörää pelaaja päättää, antaako paikkansa mummolle (palkkiona
  pulla). Pyörän kanssa pitää löytää pyöräpaikka joko kysymällä kohteliaasti tai
  tunkemalla, jolloin pelaaja joutuu pakoon ja arvaamaan oven oikean napin.
**Leppävaara**: lipuntarkastaja. Ilman lippua voi ostaa mobiililipun (-30 min)
  tai kertoa totuuden, jolloin arvottu arvo + ystävällisyys ratkaisevat. Sen jälkeen
  juna pysähtyy Keran asemalla opastinvian takia: odota, auta kuljettajaa arvaamaan
  koodi tai hae varastettu pyörä.
**Helsinki**: jos pelaajalla on pulla, hän voi antaa sen nälkäiselle lapselle.
  Viimeinen matka tapahtumaan tehdään ratikalla, kaupunkipyörällä tai taksilla.
  taksista häviää pelin.

## Kestävä kehitys

Peli liittyy kestävän kehityksen tavoitteeseen kestävät kaupungit ja
yhteisöt, joka sisältää kestävän joukkoliikenteen. Ilmastoteot sopivat myös tähän

- Koko peli kertoo julkisella liikenteellä matkustamisesta auton sijaan.
- Helsingissä ratikka ja kaupunkipyörä vievät perille, mutta taksin valitseminen
  hävittää pelin, koska auto saastuttaa.
- Pyörän varastaminen kostautuu myöhemmin, ja muiden auttaminen palkitaan
  ystävällisyyspisteillä.

## Tallennus ja tiedostot

- intro.txt ja ohjeet.txt luetaan tiedostoista pelin aikana.
- Kirjoittamalla "valikko" minkä tahansa kysymyksen kohdalla aukeaa
  pikkuvalikko: jatka, tallenna tai palaa päävalikkoon.
- Tallennuspaikkoja on neljä. Ne tallentuvat JSON-muodossa kansioon
  talennukset/ (save1.json jne.). Jos paikka on jo käytössä, peli
  kysyy ennen ylikirjoittamista.
- Tulokset tallentuvat tiedostoon tulokset.txt.

## Rakenne

| Tiedosto | Tehtävä |
|---|---|
| main.py | Käynnistää pelin: nimen ja iän tarkistus, pelaaja-olio, päävalikko |
| paavalikko.py | Päävalikko |
| peli.py | Käy asemat läpi listasta for-silmukalla ja näyttää lopputulokset |
| pelaaja.py | Pelaaja-luokka: nimi, sijainti, esineet, aika, ystävällisyys |
| yleisfunktiot.py | Yhteiset funktiot: syötteen tarkistus, häviö, tallennus, pikkuvalikko, clear funktio |
| Asemat | Paketti, jossa jokainen asema on oma luokkansa |
| Asemat/asema.py | Asema-yläluokka, jonka kaikki asemat perivät |

Jokaisella asemalla on oma pelaa()-metodi. 

## Omat lisäominaisuudet

- Pikkuvalikko, jonka saa auki missä tahansa kohtaa peliä.
- Neljä tallennuspaikkaa ja varoitus ennen ylikirjoittamista.
- Pisteiden lasku ja tulostiedosto.
