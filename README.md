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

## Spustenie aplikácie
V hlavnom priečinku aplikácie sa nachádza súbor docker-compose.yaml. Pre spustenie
vykonajte:
1. Hlavný priečinok aplikácie otvorte v konzole/termináli
2. Zadajte príkaz na spustenie docker compose up -d
3. Počkajte kým sa jednotlivé služby vytvoria a naštartujú
4. Po naštartovaní si otvorte vo webovom prehliadači lokálnu adresu localhost:3000
5. V prípade, že všetko zbehlo v poriadku, otvorí sa hlavná časť aplikácie kde je treba
zadať používateľské ID. V tomto momente riadi aplikácia ostatné služby automaticky.
6. Po spustení služieb sa zobrazí tlačidlo "Continue", pričom kliknutím na tlačidlo sa
otvorí simulátor v novej karte. (Inicializácia trvá pár sekúnd, v prípade že sa stránka
nenačíta hneď, je potrebný refresh stránky)
7. Na ukončenie simulátora slúži tlačidlo "Stop simulátor"na stránke hlavného programu.
(Vypnutie a vymazanie aktívných kontajnerov simulátora môže tiež chvílu trvať)

Pozn.: Pre otestovanie oboch simulátorov, sa dajú použiť nasledujúce príklady identifikátorov:

• **115116** vyberie SQL Simulátor

• **111111** vyberie XSS Simulátor

## Upozornenie
Program aj Docker konfigurácia jednotlivých častí je navrhnutá univerzálne a mala by
fungovať rovnako na všetkých bežných operačných systémoch. Testovanie systému a jeho
spustenie sme však vykonávali na operačnom systéme OS X. V prípade spúšťania programu
na operačnom systéme Windows môžu byť vyžadované špecifické nastavenia systému na
spustenie kontajnerov a použitie nástroja Docker, ktoré sme nevedeli predvídať.
