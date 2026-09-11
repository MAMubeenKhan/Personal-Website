# mamubeenkhan.github.io — personal site

Static site. No build step, no framework, no dependencies. Open
`index.html` in a browser and it works.

## Layout

```
index.html          home — hero, products (B2B), also-shipped grid, services, about, contact
style.css           the entire design system, mobile first
work/*.html         one case study per product
images/apps/        app icons and screenshots
images/mubeen.png   portrait
build-cases.py      one-off generator that produced work/*.html
```

## Editing

Edit the HTML directly. `build-cases.py` created the case-study pages so they
started out identical; it is not a build step and you do not need to run it
again. If you do run it, it **overwrites** everything in `work/`.

To add a product, copy an existing file in `work/`, then add a card to the grid
in `index.html`.

## Things that are deliberate

- **Mobile first.** Every base rule in `style.css` targets a phone. Media
  queries only ever add — `min-width`, never `max-width`. Check any change at
  360px wide before anything else.
- **A sticky action bar on phones only.** WhatsApp and email, always reachable,
  hidden above 760px where the header is already visible.
- **Dark mode follows the system**, via `prefers-color-scheme`. Every colour is
  a custom property at the top of `style.css`; nothing is hard-coded except the
  hero, which is dark in both themes on purpose.
- **48px minimum touch targets** on every button and link in the bar.
- **Products with no artwork get a monogram tile** (`.app-icon.mono`), rather
  than borrowing another app's icon.

## Positioning

The site leads with **indie B2B tools** — Screenshotline for developers,
AdLib for marketers — because two tools for people at work are a stronger
identity than a list of unrelated consumer apps. Those two are featured in
`#products`; everything else lives in `#work` as the track record. Keep new
B2B products in `#products` and consumer apps in `#work`.

`work/screenshotline.html` was written by hand, not by `build-cases.py`, and
the hero image `images/apps/screenshotline-home.png` was captured by
Screenshotline itself. Re-capture it when the screenshotline.com home page
changes: `curl -o images/apps/screenshotline-home.png
"https://screenshotline.com/demo?url=https%3A%2F%2Fscreenshotline.com"`.

## To update

- **Contact details** appear in `index.html` and in every `work/*.html` (the
  mailto and the `wa.me` link). Change them everywhere, or edit
  `build-cases.py` and regenerate.
- **A custom domain**: add a `CNAME` file containing the bare domain, point the
  DNS at GitHub Pages, then update the `canonical` and `og:url` tags in
  `index.html`.
- **Riverside Files** currently uses a monogram and has no store link. When it
  passes review, add the icon to `images/apps/` and the Play link to both the
  card and `work/riverside-files.html`.
- **Screenshotline's repo goes public on launch day.** Once
  github.com/MAMubeenKhan/screenshotline is public, add it as a link in
  `work/screenshotline.html` (facts strip and "Where it is now").
- **The gym client is anonymous** at their request. If they agree to be named,
  update `work/gym-management.html`.
