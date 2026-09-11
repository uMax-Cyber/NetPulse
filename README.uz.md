<div align="center">

**🇬🇧 [English](README.md) · 🇷🇺 [Русский](README.ru.md) · 🇺🇿 [Oʻzbekcha](README.uz.md)**

</div>

# NetPulse — Wi-Fi va Tarmoq Diagnostikasi

Productionda Wi-Fi muammolarini tashxislash metodologiyasi: DHCP pool tugashidan sticky clientlargacha.

## Falsafa: umumiydan xususiyga

**Hech qachon wireshark bilan boshlamang.** Diagnostika zinapoyasi:
1. **Scope** — kim/nima/qayerda/qachon (SSID, VLAN, qurilmalar)
2. **Passiv metrikalar** — RSSI, retry, kanal yuklamasi
3. **DHCP yo'li** — pool hajmi vs utilizatsiya
4. **Vaqt korrelyatsiyasi** — konfig (doimiy) vs yuklama (piklar)
5. **Aniq capture** — endigina, aniq nuqtada

## Asosiy kashfiyot: DHCP pool tugashi (BIRINCHI tekshirish)

**Simptom**: yangi qurilmalar «ulanish...» da qotadi, mavjudlari ishlaydi.
**Tekshirish**: noyob IP soni vs pool hajmi.

```bash
grep "DHCP Server" /var/log/dhcp.log | \
  grep -oE 'reported_ip="10\.X\.Y\.[0-9]+"' | sort -u | wc -l
```

## Real holatlar

| Simptom | Sabab | Yechim |
|---------|-------|--------|
| Yangi qurilmalar «ulanish...» | DHCP pool tugagan (459/455) | Poolni ×2 kengaytirish |
| 1-qavat klienti 3-qavat APda | Min RSSi kick yo'q | -75dBm o'rnatish |
| IP + link bor, paket yurmaydi | 58k retransmission | 5 GHz yoqish |

## 📬 Aloqa

Savollar bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

**🇬🇧 [English](README.md) · 🇷🇺 [Русский](README.ru.md) · 🇺🇿 [Oʻzbekcha](README.uz.md)**

</div>
