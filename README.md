# Bakalarska_praca
Riešenie bakalárskej práce - Simulačná platforma na generovanie CTF úloh zameraných na zraniteľnosti webových aplikácií

# Návod na spustenie

## Potrebné nástroje a požiadavky
Nainštalujte si kontajnerizačný nástroj Docker. V prípade nedostatku technických zdrojov
na používanie samotného Docker nástroja je možné využiť pamäťovo šetrnejšiu alternatívu
Rancher.

### Nastavenie nástroja Rancher
V prípade použitia nástroja Rancher je po inštalácií nutné vykonať niekoľko krokov:
1. Otvorte program Rancher až kým sa zobrazí hlavná stránka aplikácie
2. V pravom hornom rohu kliknite na symbol nastavení
3. V sekcii „Container Engine” je potrebné zvoliť možnosť dockerd moby.
4. Po uložení nastavení je Rancher pripravený na riadenie Docker kontajnerov

## Nastavenie environment variables
Environment variables sa z bezpečnostných dôvodov neukladajú v repozitári. 
V projekte je potrebné nastaviť nasledovné premenné:
1. Do priečinka **frontend** je potrebné vložiť _.env_ súbor, v ktorom bude definovaná premenná:

**_VITE_API_HOST=http://localhost:2000/_** kde port je potrebné nastaviť podľa hlavného docker-compose.yaml a teda podľa portu služby **backend-api**

2. Rovnaké _.env_ súbory je potrebné pridať aj do **frontend** priečinkou jednotlivých simulátorov. Avšak sa tam vkladá rovnaká premenná s iným portom a to: 

**_VITE_API_HOST=http://localhost:2001/_**

3. V poslednom kroku je potrebné v hlavnom **backend/api/main.py** súbore prepísať definovanú environment variable **os.environ["USER_PROJECT_PATH"]** a nastaviť jej hodnotu na aktuálnu cestu projektu v spúšťanom počítači.

## Spustenie aplikácie
V hlavnom priečinku aplikácie sa nachádza súbor docker-compose.yaml. Pre spustenie
vykonajte:
1. Hlavný priečinok aplikácie otvorte v konzole/termináli
2. Zadajte príkaz na spustenie docker compose up -d
3. Počkajte kým sa jednotlivé služby vytvoria a naštartujú. 
4. Po naštartovaní si otvorte vo webovom prehliadači lokálnu adresu localhost:3000
5. V prípade, že všetko zbehlo v poriadku, otvorí sa hlavná časť aplikácie kde je treba
zadať používateľské ID. V tomto momente riadi aplikácia ostatné služby automaticky. **!** **Pri prvom skladaní docker images môže dojsť k zlyhaniu budovania (Načítavací loader sa prestane točiť). V tomto prípade je potrebné spustiť program ešte raz a zapnúť simulátor rovnakým spôsobom znova** **!** **Na riešení tohto problému sa aktuálne pracuje**
6. Po spustení služieb sa zobrazí tlačidlo "Continue", pričom kliknutím na tlačidlo sa
otvorí simulátor v novej karte. (Inicializácia trvá pár sekúnd, v prípade že sa stránka
nenačíta hneď, je potrebný refresh stránky)
7. Na ukončenie simulátora slúži tlačidlo "Stop simulátor"na stránke hlavného programu.
(Vypnutie a vymazanie aktívných kontajnerov simulátora môže tiež chvílu trvať)

Pozn.: Pre otestovanie oboch simulátorov, sa dajú použiť nasledujúce príklady identifikátorov:

• **115116** vyberie SQL Simulátor

• **111111** vyberie XSS Simulátor

## Upozornenie
Aplikácia je vo vývojovom štádiu.
Program aj Docker konfigurácia jednotlivých častí je navrhnutá univerzálne a mala by
fungovať rovnako na všetkých bežných operačných systémoch. Testovanie systému a jeho
spustenie sme však vykonávali na operačnom systéme OS X. V prípade spúšťania programu
na operačnom systéme Windows môžu byť vyžadované špecifické nastavenia systému na
spustenie kontajnerov a použitie nástroja Docker, ktoré sme nevedeli predvídať.
