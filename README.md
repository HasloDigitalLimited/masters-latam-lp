# Transform Trauma México — LatAm fast landing pages

Two static Spanish landing pages for paid traffic from Latin America. Pure HTML and CSS,
no JavaScript libraries, no third-party requests, no cookies, no tracking.

| URL | Mirrors | File |
|-----|---------|------|
| `/` | mexico.mastersevents.com/es/ | `index.html` |
| `/descuento/` | mexico.mastersevents.com/es/latam-concession/ | `descuento/index.html` |

## Weight

Each page is about 58 KB on disk, 37 KB gzipped, in a single request. That includes the only
two images used: the Transform Trauma México 2027 logo (inline SVG) and the speakers photo
(inline WebP, 29 KB). One optional extra request fetches the Plus Jakarta Sans subset
(`assets/pjs.woff2`, 20 KB). It is declared with `font-display: swap`, so the page renders
straight away in the system font and upgrades to the brand font only once it arrives. On a
bad connection, or if the file is missing, the visitor simply sees the system font.

## Editing

Do not edit the two HTML files by hand. Everything lives in `build.py`: the CSS, the
template, and two content dictionaries (`HOME` and `DESC`) holding the copy, prices and links.
After a change, run:

```bash
python3 build.py
```

Things copied from the live site on 10 September 2026 that will not update themselves:

- Home page early-bird prices (`$990` / `$1090` in-person, `$225` / `$295` virtual)
- Discount page prices (`US$495` / `US$1090` in-person, `US$95` / `US$295` virtual) and the eligibility wording
- Event dates and venue
- Speaker photo (`assets/speakers.webp`, 640px wide)
- WhatsApp number and pre-filled message (`WA_NUMBER`, `WA_MSG` at the top of `build.py`)

## Ad tracking

**Meta Pixel** `1640052390439143` (the same pixel as mexico.mastersevents.com) fires on both
pages. It is the only third-party request and loads async, so it never blocks rendering.
Events:

| Event | When |
|-------|------|
| `PageView` | page load |
| `InitiateCheckout` | any "Comprar entradas" button |
| `Contact` | the WhatsApp button |
| `ClickToSite` (custom) | any other link to the main site |

Every event carries `page` (`home` or `descuento`), the button `label` and the target `href`.
Change the ID via `META_PIXEL_ID` at the top of `build.py`.

**Query string pass-through:** any `utm_*`, `fbclid` or `gclid` on the landing URL is
appended to every outbound link and to the link between the two pages, so the main site's
own pixel and analytics still see the source.

## What to upload to Cloudflare

Only `index.html`, `descuento/index.html` and the `assets/` folder. `build.py`, this README
and `_headers` are optional (`_headers` just adds caching if present).

## Deploy on Cloudflare Pages

1. Push this folder to a Git repo, or use direct upload in the Cloudflare dashboard.
2. Workers & Pages → Create → Pages → connect the repo.
3. Framework preset **None**, build command **empty**, output directory **/**.
4. Project → Custom domains → add the subdomain. Cloudflare creates the DNS record if the
   zone is already there.

`_headers` sets a short cache on the pages and a long immutable cache on `assets/`.

## Local preview

```bash
python3 -m http.server 8765
```

Then open http://localhost:8765/ and http://localhost:8765/descuento/.
