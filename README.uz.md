<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Wi-Fi va tarmoq diagnostikasi vositasi

![Demo](screenshots/demo.svg)
[![CI](https://github.com/uMax-Cyber/NetPulse/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/NetPulse/actions/workflows/ci.yml)

Production muhitidagi Wi-Fi muammolarini tizimli tashxislash metodologiyasi: DHCP pool tugashidan «yopishqoq» (sticky) klientlargacha, kanal tiqilinchidan oʻlik zonalargacha. Topologiya xaritasini chizish, DHCP lease tahlili va roaming sifatini baholash ham shu jumlaga kiradi.

## Tamoyil: umumiydan xususiyga

**Hech qachon ishni wireshark bilan boshlamang.** Tashxislashni quyidagi tartibda olib boring:
1. **Koʻlam** — kim, nima, qayerda, qachon (qaysi SSID, VLAN, qurilmalar)
2. **Passiv koʻrsatkichlar** — RSSI, retry ulushi, kanal yuklamasi, foydalanuvchi qoniqishi
3. **DHCP yoʻli** — pool hajmi va band qilinganlik, lease hodisalari, relay zanjiri
4. **Vaqt boʻyicha tahlil** — muammo doimiy kuzatilsa konfiguratsiya, pik soatlarda boʻlsa yuklama
5. **Capture** — faqat shu nuqtadan keyin, faqat anomaliya roʻy bergan joyda olinadi

## Eng muhim topilma: DHCP pool tugishi (avval shuni tekshiring)

**Belgisi:** yangi qurilmalar «ulanmoqda...» da qotib qoladi, eski qurilmalar esa odatdagidek ishlaydi.
**Tekshirish:** berilgan noyob IP lar soni bilan pool sigʻimini solishtiring.

```bash
# DHCP jurnalidagi noyob IP larni sanash
grep "DHCP Server" /var/log/dhcp.log | \
  grep -oE 'reported_ip="10\.X\.Y\.[0-9]+"' | sort -u | wc -l
# Pool hajmi bilan solishtiring
```

**Nega koʻpincha payqalmaydi:** «sim orqali hammasi yaxshi» degan xulosa DHCP muammosini istisno etmaydi — har bir VLAN ning DHCP pooli alohida.

## Skriptlar

| Skript | Vazifasi |
|--------|----------|
| `scripts/dhcp_pool_check.py` | Berilgan IP lar sonini pool sigʻimi bilan solishtirish |
| `scripts/topology_map.py` | Kontroller API sidan svitch/AP/klient daraxtini chizish |
| `scripts/roam_quality.py` | Roaming hodisalarini tahlil qilish (yomon roaming — ikkala tomon ham −75dBm dan past) |
| `scripts/port_audit.py` | Svitch portlarining toʻliq inventarizatsiyasi (VLAN, PoE, xatolar, flaplar) |

## Hal qilingan real keyslar

### Keys 1: Wi-Fi da «ulanmoqda...»
Sabab: DHCP pool tugagan — 455 manzilli poolga 459 noyob IP berilgan. Poolni ikki baravar kengaytirish bilan hal qilingan.

### Keys 2: 1-qavatdagi qurilma 3-qavatdagi AP ga ulangan
Sabab: min RSSI kick sozlanmagan. Klient beton devorlar ortidagi uzoq AP ga −82dBm signal bilan baribir yopishib turadi — natijada 58 ming qayta uzatish. Min RSSI ni −75/−80dBm qilib belgilash bilan hal qilingan.

### Keys 3: Oʻlik zonalar (IP va link bor, paket yurmaydi)
Sabab: efir toʻlgan — 2.4GHz ning atigi 3 kanalida 627 klient. Katta retry boʻronlari kelib chiqqan (eng ogʻiri: bitta klientda 58 106 retry). Yechim: 5GHz ni yoqish (gateway VM lariga RAM qoʻshilgandan keyin amalga oshirildi).

## Texnologiyalar
- UniFi Controller API (legacy REST)
- Sophos Firewall XML API
- Python (faqat standart kutubxona)
- Markazlashtirilgan log uchun rsyslog

## Litsenziya
MIT

## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
