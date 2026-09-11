<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Wi-Fi va tarmoq diagnostikasi vositasi

![Demo](screenshots/demo.svg)
[![CI](https://github.com/uMax-Cyber/NetPulse/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/NetPulse/actions/workflows/ci.yml)

Production muhitida Wi-Fi muammolarini tashxislashning tizimli metodologiyasi: DHCP pool tugashidan «yopishqoq» (sticky) klientlargacha, RF tiqilinchidan oʻlik zonalargacha. Topologiya xaritasini chizish, DHCP ijaralarini (lease) tahlil qilish va roaming sifatini baholashni oʻz ichiga oladi.

## Tamoyil: umumiydan xususiyga

**Hech qachon wireshark bilan boshlamang.** Diagnostika zinapoyasiga amal qiling:
1. **Koʻlam** — kim/nima/qayerda/qachon (qaysi SSID, VLAN, qurilmalar)
2. **Passiv koʻrsatkichlar** — RSSI, qayta uzatish ulushi, kanal yuklamasi, qoniqish darajasi
3. **DHCP yoʻli** — pool hajmi va band qilinganlik, lease hodisalari, relay yoʻli
4. **Vaqt boʻyicha bogʻliqlik** — doimiy (konfiguratsiya) yoki pik soatlarda (yuklama)
5. **Nishonga yoʻnaltirilgan capture** — faqat shu bosqichda, faqat anomaliyaning aniq nuqtasida

## Asosiy kashfiyot: DHCP pool tugashi (birinchi navbatda tekshiring)

**Belgi**: yangi qurilmalar «ulanmoqda...» da qolib ketadi, mavjud qurilmalar esa odatdagidek ishlaydi.
**Tekshirish**: berilgan noyob IP lar soni va pool sigʻimini solishtirish.

```bash
# DHCP jurnalidagi noyob IP larni sanash
grep "DHCP Server" /var/log/dhcp.log | \
  grep -oE 'reported_ip="10\.X\.Y\.[0-9]+"' | sort -u | wc -l
# Pool hajmi bilan solishtiring
```

**Nega e'tibordan chetda qoladi**: «sim orqali hammasi ishlaydi» DHCP muammosini istisno etmaydi — har xil VLAN da alohida poolar bor.

## Skriptlar

| Skript | Vazifasi |
|--------|----------|
| `scripts/dhcp_pool_check.py` | Berilgan IP lar va pool sigʻimini solishtirish |
| `scripts/topology_map.py` | Kontroller API sidan svitch/AP/klient daraxtini qurish |
| `scripts/roam_quality.py` | Roaming hodisalarini tahlil qilish (yomon roaming = ikkala tomon < -75dBm) |
| `scripts/port_audit.py` | Svitch portlarining toʻliq inventarizatsiyasi (VLAN, PoE, xatolar, flaplar) |

## Hal qilingan real keyslar

### Keys 1: Wi-Fi da «ulanmoqda...»
Asosiy sabab: DHCP pool tugagan (455 manzilli poolga 459 noyob IP). Pool ×2 kengaytirib hal qilingan.

### Keys 2: 1-qavatdagi klient 3-qavatdagi AP ga ulangan
Asosiy sabab: min RSSI kick sozlanmagan. Klient beton devorlar orqali uzoqdagi AP ga -82dBm signal bilan yopishib olgan. 58 ming qayta uzatish. Min RSSI ni -75/-80dBm ga belgilab hal qilingan.

### Keys 3: Oʻlik zonalar (IP + link yaxshi, paketlar yurmaydi)
Asosiy sabab: efirning tiqilishi — 2.4GHz ning 3 kanalida 627 klient. Katta qayta uzatish boʻronlari (eng yomoni: bitta klientda 58 106 qayta uzatish). 5GHz ni yoqib hal qilingan (gateway VM larida RAM yangilagandan keyin).

## Texnologiyalar
- UniFi Controller API (legacy REST)
- Sophos Firewall XML API
- Python (faqat standart kutubxona)
- Markazlashtirilgan jurnal uchun rsyslog

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
