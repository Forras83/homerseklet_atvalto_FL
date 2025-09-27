# Grafikus Hőmérséklet Átváltó – FL

**Hallgató monogram:** FL

## Program leírása
Az alkalmazás egy **grafikus hőmérséklet átváltó** program, amelyet Python nyelven,  
a beépített **Tkinter** könyvtár segítségével készítettem.

A felhasználó megadhat egy hőmérsékleti értéket, majd kiválaszthatja,  
hogy melyik egységből (Celsius, Fahrenheit, Kelvin) melyikbe szeretné átváltani.  
Az átváltás elindítható az **„Átváltás” gomb** megnyomásával, az **Enter** billentyűvel,  
vagy automatikusan akkor is, ha a felhasználó megváltoztatja a forrás vagy cél egységet a legördülő listában.

A program a beírt értéket ellenőrzi:
- ha a megadott érték nem érvényes szám (pl. betűk vagy hibás formátum), hibaüzenetet jelenít meg,
- ha a forrás- és a célegység azonos, szintén hibát jelez.

A számítás eredményét a cél egység **teljes nevével** együtt jeleníti meg  
(pl. `100 Celsius` → `212 Fahrenheit`).

Az alkalmazás ablakos felületet biztosít, kényelmesen használható,  
és támogatja a **tizedesvesszőt** is (pl. `23,5` helyett nem kötelező a pont).

## Modulok és felépítés
- **fl_mod**  
  - `FLConverter` osztály – a konverzió logikája  
  - `fl_parse_input` – felhasználói bemenet feldolgozása  
  - `fl_format_output` – eredmény formázása  
  - `fl_convert` – hőmérséklet átváltás számítása
- **fl_gui**  
  - `FLApp` osztály – grafikus felület és eseménykezelés  
  - fő eseménykezelő metódusok: `on_convert_click`, `on_convert_enter`, `on_combo`, `exec_convert`
- **main.py**  
  - a program belépési pontja, létrehozza az ablakot és elindítja az alkalmazást

## Használat
1. Írj be egy számot a **„Érték”** mezőbe (pl. `23,5` vagy `100`).
2. Válaszd ki a **forrás** egységet (pl. *C - Celsius*).
3. Válaszd ki a **cél** egységet (pl. *F - Fahrenheit*).
4. Kattints az **Átváltás** gombra vagy nyomd meg az **Enter** billentyűt.
5. Az eredmény megjelenik az alsó mezőben a cél egység teljes nevével.

## Futtatás
```bash
python3 main.py


