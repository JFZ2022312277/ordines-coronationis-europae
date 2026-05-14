# Ordines Coronationis Europae

A digital research platform and TEI/IIIF-linked dataset for the comparative
study of medieval coronation ordines, manuscript witnesses, ritual
traditions, and the spatial transmission of inauguration ritual across
Latin Christendom and Byzantium.

Release: `2026.05.12` — first public release prepared for the *Speculum*
Digital Medieval Studies Reviews call.

## Quick start

### Option 1 — open the live site (recommended)

After deployment, open the public URL of this repository:

```
https://jfz2022312277.github.io/ordines-coronationis-europae/
```

(Replace `YOUR-USER` with the GitHub account that hosts this repository.)

### Option 2 — run locally from this directory

The application loads its data via `fetch()`, so it **must be served over
HTTP**, not opened directly with `file:///`.

The repository ships a zero-dependency Python helper:

```bash
python serve.py
```

On Windows you can double-click `serve.bat`.
On macOS / Linux you can run `bash serve.sh`.

A browser tab will open at <http://localhost:8765/index.html>.

### Recommended reviewer entry points

- `index.html#/map` — map of manuscript witnesses, repositories, and
  the OpenAtlas-style relational data layers.
- `index.html#/detail/OCF-XV` — Ratold Ordo case study with the
  manuscript ego-network and dispersal data.
- `index.html#/detail/ECR-XIII` — Liber Regalis case study with
  proofread Latin JSON and the embedded IIIF viewer.
- `iiif/viewer.html?manifest=ECR-XIII-LIBER-REGALIS` — standalone IIIF
  viewer demonstration.

## Catalogued / archived version

For review submission, this repository is also archived on Zenodo (or an
institutional repository) with a permanent DOI. Reviewers should be given
both the **live URL** (above) and the **DOI of the archived release**.

## Contents

- `index.html` — main application (single-file static web app).
- `serve.py` / `serve.bat` / `serve.sh` — local development server
  helpers (no third-party dependencies).
- `404.html` — fallback page for static hosting.
- `data/` — OpenAtlas-style JSON/CSV data, manuscript dispersal datasets,
  and proofread Latin data.
- `iiif/` — IIIF manifests authored by the project plus a lightweight
  viewer (`iiif/viewer.html`).
- `iiif-source/` — local image source files used by the Liber Regalis
  demonstration manifest, where licence permits.
- `assets/` — bundled JavaScript/CSS dependencies and public image assets.
- `PROJECT.md` — project description and reviewer-facing documentation.
- `SUBMISSION_NOTES.md` — notes specific to the *Speculum* DMSR submission.
- `CHANGELOG.md` — release history.
- `CITATION.cff` — citation metadata.
- `LICENSE`, `LICENSE-content.md` — see "Licence" below.

## Deployment to GitHub Pages

```bash
git init
git add .
git commit -m "Initial public release: Ordines Coronationis Europae 2026.05.12"
git branch -M main
git remote add origin https://github.com/YOUR-USER/ordines-coronationis-europae.git
git push -u origin main
```

Then on the GitHub web interface go to **Settings → Pages**, choose
**Deploy from a branch**, select **main** and **/ (root)**, and click
**Save**. After 2–3 minutes the URL above will be live.

A `.nojekyll` file is already present, so Pages will serve the directory
verbatim without Jekyll processing.

For a permanent DOI, link the GitHub repository to Zenodo
(**Settings → Integrations** on Zenodo), create a release on GitHub,
and Zenodo will automatically archive it and issue a DOI.

## Licence

- Application code is released under the **MIT License** — see `LICENSE`.
- Scholarly content (TEI, JSON, CSV, IIIF manifests, documentation) is
  released under **CC BY 4.0** — see `LICENSE-content.md`.
- Digital reproductions of medieval manuscripts retain the rights
  statements of the holding institutions and are NOT relicensed.

## Citation

Please cite the archived Zenodo release. See `CITATION.cff` for the
recommended format. The foundational critical edition for the French
material is Richard A. Jackson, *Ordines Coronationis Franciae*
(2 vols., University of Pennsylvania Press, 1995–2000), which should be
cited alongside any use of OCF-tagged entries.
