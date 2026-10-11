# HSN and SAC codes for Indian shops and service businesses (JSON + CSV)

A curated, searchable list of **446 HSN codes** for goods commonly sold by Indian shops, traders and distributors (grocery, FMCG, dairy, pharma, garments, footwear, hardware, electricals, mobiles, stationery, building material …) and **203 SAC codes** for services – each with a plain-language "common items" line and Hindi/Hinglish search words (atta, chawal, chappal, sariya …).

Try it online, no install: **[billingbazaar.in/tools/hsn-code-finder/](https://billingbazaar.in/tools/hsn-code-finder/)**

## Files

| File | What |
|---|---|
| `hsn.json` / `hsn.csv` | HSN codes (mostly 4-digit headings, some 6-digit codes) with description, common items and search words |
| `sac.json` / `sac.csv` | SAC codes (chapter 99 headings and common 6-digit codes) with examples |
| `search.py` | `python3 search.py chawal` – quick search from the command line |

Example entry:

```json
{
  "code": "0105",
  "description": "Live poultry (fowls, ducks, geese, turkeys and guinea fowls)",
  "common_items": "Live chickens, ducks, day-old chicks",
  "chapter": "Live animals",
  "search_words": "murgi chicken live bird poultry"
}
```

## Important

- **GST rates are not included on purpose.** Rates changed in September 2025 and can differ within one heading. Check the current rate on the CBIC/GST rate finder: https://cbic-gst.gov.in/gst-goods-services-rates.html
- HSN at 4-digit level is what most small businesses need on invoices (turnover up to ₹5 crore); larger businesses need 6 digits. Confirm the exact code for your product with your CA.

## Save the HSN code once, print it on every invoice

Look the code up here once, then store it with the item in your billing app. In **Vyapar** the HSN code saved on an item
prints on every invoice and builds the HSN-wise summary needed in GSTR-1
([adding HSN codes in Vyapar](https://billingbazaar.in/guides/how-to-add-hsn-code-in-vyapar/),
[importing items with HSN from Excel](https://billingbazaar.in/guides/how-to-import-items-from-excel-in-vyapar/)).

Starting with Vyapar? Sign up with referral code **`NXW3QY`** as a new user, or get it set up for you with a [free demo and installation](https://billingbazaar.in/vyapar-referral-code/) in Hindi or English.

---

Made by [Billing Bazaar](https://billingbazaar.in) – billing software demos, setup and free GST tools for Indian shops and traders.
[All free tools](https://billingbazaar.in/tools/) · [Vyapar guides](https://billingbazaar.in/guides/)

*Not affiliated with the GST Network (GSTN), CBIC or NPCI. Vyapar is a trademark of Simply Vyapar Apps Pvt. Ltd.;
Billing Bazaar is a Vyapar partner. Always confirm GST rates and rules on the official GST portal.*
