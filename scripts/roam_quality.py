#!/usr/bin/env python3
"""Analyze WiFi roaming quality from controller syslog.
Bad roam = both old and new AP signal weaker than threshold.
Usage: roam_quality.py <log_file> [--threshold -75]
"""
import sys, re
from collections import Counter

def main():
    log_file = sys.argv[1]
    threshold = int(sys.argv[sys.argv.index("--threshold")+1]) if "--threshold" in sys.argv else -75

    roams = []
    for line in open(log_file, encoding="utf-8", errors="replace"):
        if "Client Roamed" not in line:
            continue
        m = re.search(r'Roaming Decision: (-?\d+) dBm to (-?\d+) dBm', line)
        if m:
            roams.append((int(m.group(1)), int(m.group(2))))

    if not roams:
        print("No roam events found"); return

    bad = [(old, new) for old, new in roams if old < threshold and new < threshold]
    print(f"Total roams: {len(roams)}")
    print(f"Bad roams (both < {threshold}dBm): {len(bad)} ({len(bad)/len(roams)*100:.1f}%)")
    print(f"Target: < 2% bad roams")

    if len(bad) / len(roams) > 0.05:
        print("\n🔴 CRITICAL: >5% bad roams — sticky clients confirmed")
        print("   Recommendation: enable min RSSI kick at threshold")
    elif len(bad) / len(roams) > 0.02:
        print("\n⚠️  WARNING: 2-5% bad roams — monitor")
    else:
        print("\n✅ Roaming quality OK")

if __name__ == "__main__":
    main()
