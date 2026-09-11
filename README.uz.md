<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# NetPulse — Wi-Fi va Tarmoq Diagnostikasi

# NetPulse — Wi-Fi va tarmoq diagnostikasi

Wi-Fi muammolarini bosqichma-bosqich aniqlash metodologiyasi: DHCP pool tugashidan boshlab, qoplama muammolarigacha.

## Tamoyil: umumiydan xususiyga

**Wireshark bilan boshlamang.** Avval quyidagi tartibda tekshiring:
1. **Doira** — qaysi SSID, VLAN, qurilmalar taʼsirlangan
2. **Passiv koʻrsatkichlar** — RSSI, retry, kanal yuklamasi
3. **DHCP yoʻli** — pool hajmi va band qilingan IP soni
4. **Vaqt bogʻliqligi** — konfiguratsiya (doimiy) yoki yuklama (pik soatlar)
5. **Aniq nuqtada capture** — faqat shu bosqichdan keyin

## Eng muhim tekshiruv: DHCP pool (birinchi navbatda!)

**Belgi**: yangi qurilmalar «ulanmoqda...» da qolib ketadi, lekin mavjud qurilmalar ishlaydi.

```bash
grep "DHCP Server" /var/log/dhcp.log | \\
  grep -oE "reported_ip=\\"10\\\\.X\\\\.Y\\\\.[0-9]+\\"" | sort -u | wc -l
```

## Real hayotdan misollar

| Belgi | Sabab | Yechim |
|-------|-------|--------|
| Yangi qurilmalar ulanmaydi | DHCP pool toʻlgan (459/455) | Poolni ikki barobar kengaytirish |
| 1-qavat qurilmasi 3-qavat APga ulangan | Min RSSI belgilanmagan | -75dBm chegara qoʻyish |
| IP bor, lekin trafik yurmaydi | 58 ming qayta uzatish | 5 GHz yoqish |


## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

