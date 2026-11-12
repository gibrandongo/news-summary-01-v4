"""Write one English summary of the world news of 11 November 2026.

The summary is embedded below and written verbatim to entry.txt in the
output directory. The program is offline, deterministic and stdlib-only.
"""

import os

SUMMARY = """World news, Wednesday, 11 November 2026

1. Russia and Ukraine ended two days of US-mediated talks in Abu Dhabi agreeing the largest prisoner-of-war exchange of the war, but no ceasefire, and US envoys go to Moscow on Thursday. (Reuters)
2. Secretary of State Marco Rubio said pressure on Iran was working so well there was "no need for major combat operations any longer". The Justice Department charged three Iran-backed operatives over nearly 20 plots in the US and Europe. (New York Times; Justice Department)
3. Iran designated Argentina's navy and air force as terrorist organizations, and security chief Mohsen Rezaei said no enriched nuclear material would leave Iran. (Just Security)
4. Congo's Bundibugyo Ebola outbreak passed 11,000 infections: 11,042 cases and 5,387 deaths, the country's deadliest Ebola outbreak; the WHO counted 10,668 cases and 5,198 deaths as of 3 November. (Associated Press; WHO)
5. UN Secretary-General Antonio Guterres told leaders opening the COP31 summit in Antalya, Turkey, that slow climate action had put the world "on a path to destruction". (United Nations)
6. Saudi air defenses intercepted seven Houthi missiles and drones aimed at Riyadh, Mecca and other regions, the Saudi-led coalition said; the Houthis denied targeting Mecca. (Reuters)
7. The US House voted 211-204 to send eight impeachment articles against Defense Secretary Pete Hegseth to committee, shelving the effort; 11 Democrats missed the vote. (USA Today)
8. Democrat Scott Colom defeated Republican incumbent Cindy Hyde-Smith in Mississippi's US Senate election. (Associated Press)
9. NATO scrambled jets after at least four drones strayed into Baltic airspace during Ukrainian strikes on Russia, with alerts in Lithuania. (Just Security)
10. Wall Street rebounded on CoreWeave's earnings: the Nasdaq rose 1.6% to 25,466.19 and the S&P 500 gained 1.3%; Brent crude settled at $92.76 a barrel, up 1.4%. (Associated Press; Reuters)
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = SUMMARY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    written = os.path.getsize(path)
    if written != len(data):
        raise SystemExit("short write: %d of %d bytes" % (written, len(data)))
    print("wrote %s: %d characters" % (path, len(SUMMARY)))


if __name__ == "__main__":
    main()
