# Wi-Fi Diagnosis: Step-by-Step Order (READ-ONLY methodology)

## Step 0: DHCP Pool Exhaustion (ALWAYS FIRST)
Before touching any RF tools, check if the pool is full.
- Count unique IPs in DHCP logs vs pool capacity
- "Wired works" ≠ DHCP works (different VLANs, different pools)
- 5 minutes to check, solves 30% of "connecting..." complaints

## Step 1: Scope
- Which SSID/AP/VLAN affected?
- Which device types (phones? printers? specific vendor?)
- Constant or periodic? Peak hours or random?

## Step 2: Passive Metrics (from controller API)
- RSSI distribution of connected clients
- Channel utilization per AP
- Retry rates (tx_retries in client stats)
- Satisfaction scores
- Client count per AP

## Step 3: DHCP Path (from firewall/gateway logs)
- Pool size vs unique IPs issued
- Lease events (Renew/Assign/Expire/NAK/Decline)
- Discover without Offer = server not responding

## Step 4: Time Correlation
- Config problem: constant, all day
- Load problem: peaks during busy hours
- Check: disconnect timestamps vs class schedule / meeting times

## Step 5: Targeted Packet Capture (ONLY NOW)
- Point of capture: gateway vNIC (tap interface on hypervisor)
- Look for: DHCP Discover without Offer, EAPOL failures, retransmissions
- Duration: 60-90 seconds is usually enough

## Step 6: Synthesis
Symptom → log evidence → packet evidence → root cause
All with timestamps and specific device identifiers.
