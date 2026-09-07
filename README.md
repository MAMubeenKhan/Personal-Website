# mamubeenkhan.github.io — personal site

Static site. No build step, no framework, no dependencies. Open
`index.html` in a browser and it works.

## Layout

```
index.html          home — hero, work grid, services, about, contact
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
- **The gym client is anonymous** at their request. If they agree to be named,
  update `work/gym-management.html`.
