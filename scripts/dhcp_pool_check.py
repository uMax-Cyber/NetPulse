#!/usr/bin/env python3
"""Check DHCP pool utilization from syslog.
Usage: dhcp_pool_check.py <log_file> <pool_start> <pool_end>
Example: dhcp_pool_check.py /var/log/dhcp.log 10.0.1.50 10.0.1.250
"""
import sys, re
from collections import Counter

def parse_pool(start, end):
    """Return set of all IPs in pool."""
    import ipaddress
    s = ipaddress.ip_address(start)
    e = ipaddress.ip_address(end)
    return {str(ipaddress.ip_address(i)) for i in range(int(s), int(e)+1)}

def main():
    log_file = sys.argv[1]
    pool_start, pool_end = sys.argv[2], sys.argv[3]

    pool = parse_pool(pool_start, pool_end)
    pool_size = len(pool)

    issued = set()
    events = Counter()
    for line in open(log_file, encoding="utf-8", errors="replace"):
        if "DHCP Server" not in line:
            continue
        m = re.search(r'reported_ip="([0-9.]+)"', line)
        if m and str(m.group(1)) in pool:
            issued.add(m.group(1))
        sm = re.search(r'status="([^"]+)"', line)
        if sm:
            events[sm.group(1)] += 1

    print(f"Pool: {pool_start} - {pool_end} ({pool_size} addresses)")
    print(f"Unique IPs issued: {len(issued)}")
    print(f"Utilization: {len(issued)/pool_size*100:.1f}%")
    print(f"Status distribution: {dict(events)}")

    if len(issued) >= pool_size:
        print("\n🔴 ALERT: POOL EXHAUSTED — new clients cannot get IP!")
    elif len(issued) > pool_size * 0.85:
        print("\n⚠️  WARNING: Pool >85% utilized")
    else:
        print("\n✅ Pool healthy")

if __name__ == "__main__":
    main()
