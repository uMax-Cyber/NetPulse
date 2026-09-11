<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# NetPulse — Диагностика Wi-Fi и сети

Структурированная методология диагностики Wi-Fi в продакшене: от исчерпания DHCP-пула до sticky clients, RF-заторов до мёртвых зон.

## Философия: от общего к частному

**Никогда не начинай с wireshark.** Следуй лестнице диагностики:
1. **Scope** — кто/что/где/когда (SSID, VLAN, устройства)
2. **Пассивные метрики** — RSSI, retry, загрузка каналов, satisfaction
3. **DHCP-путь** — размер пула vs утилизация, события lease
4. **Корреляция по времени** — конфиг (постоянно) vs нагрузка (пики)
5. **Точечный capture** — только теперь, в конкретной точке

## Ключевое открытие: исчерпание DHCP-пула (проверять ПЕРВЫМ)

**Симптом**: новые устройства зависают на «подключение...», существующие работают.
**Проверка**: уникальные IP vs ёмкость пула.

```bash
grep "DHCP Server" /var/log/dhcp.log | \
  grep -oE 'reported_ip="10\.X\.Y\.[0-9]+"' | sort -u | wc -l
```

## Реальные случаи

| Симптом | Причина | Решение |
|---------|--------|---------|
| Новые устройства «connecting...» | DHCP-пул исчерпан (459/455) | Расширить пул ×2 |
| Клиент с 1-го этажа на AP 3-го | Нет min RSSI kick | Установить -75dBm |
| IP + link есть, пакеты не идут | 58k retransmissions (затор) | Включить 5 ГГц |

## 📬 Контакты

Вопросы? Пишите: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
