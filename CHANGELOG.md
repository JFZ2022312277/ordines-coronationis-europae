# Changelog

All notable changes to *Ordines Coronationis Europae* (OCE) are recorded
in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project loosely follows date-based versioning (`YYYY.MM.DD`).

## [Unreleased]

Planned for the next release:

- Server-side architecture replacing the single-file HTML bundle.
- Embedded IIIF image rendering (current build links out to upstream
  manifests only).
- Versioned data releases with schema validation on ingest.
- Inter-annotator agreement reporting on the formula stratum.
- Extension of the corpus into papal pontifical (Avignon, Pontificale
  Romanum), Polish, and Nordic traditions.

## [2026.05.12] — 2026-05-12

First public release prepared for the *Speculum* Digital Medieval Studies
Reviews call for projects (Medieval Academy of America). This is the
"lean" submission package separated from the working development folder.

### Added

- Static-site distribution package with `.nojekyll` for GitHub Pages.
- `README.md`, `PROJECT.md`, `SUBMISSION_NOTES.md` describing the
  project, recommended reviewer entry points, and submission workflow.
- `CITATION.cff` with author metadata and reference to Richard A.
  Jackson's *Ordines Coronationis Franciae*.
- `metadata.json` listing entry points (`#/map`, `#/detail/OCF-XV`,
  `#/detail/ECR-XIII`).
- `data/` — OpenAtlas-style JSON/CSV datasets for OCF (28 entries),
  HRE (32 entries), ECR (29 entries), PRG (pontifical materials), and
  the proofread Latin transcription of the Liber Regalis (ECR-XIII).
- `iiif/` — local IIIF manifests for BNF-BALUZE1, BNF-LAT9430,
  ECR-XIII Liber Regalis, OCF-XIII, OCF-XVI, RECUEIL-MINIATURES, plus
  a lightweight viewer (`iiif/viewer.html`).
- `assets/vendor/` — bundled Leaflet, MarkerCluster, and React for
  resilience against CDN outage.
- `assets/charles-v/` — high-resolution PNG scans of the Charles V
  ordo (OCF-XXIII) coronation illustrations.

### Changed (relative to internal development build)

- Page title corrected from a development codename to
  `Ordines Coronationis Europae`.
- TEI export footer and internal `app_version` constant updated to
  the public project name.
- Project name normalized from "Ordines Coronationis Europa" to the
  scholarly form "Ordines Coronationis Europae".

### Excluded from this submission package

- Large local manuscript image cache `assets/gcf-fr2813/`
  (Grandes Chroniques de France) — kept in the working folder; not
  redistributed here. References to this cache are explicitly
  disabled in the interactive site (paths prefixed `_disabled_`).
- Local image cache `assets/recueil_miniatures/` — same treatment.
- OCR working files, backups, and development scratch outputs.

### Known issues

- Single-file `index.html` (~22 MB) is large; splitting into
  modular bundles is planned for the next release.
- The image stratum currently provides linked metadata only;
  embedded image rendering inside the platform is deferred.
- The formula stratum reflects a specific set of editorial
  decisions and would benefit from a second-coder validation pass.
- Three traditions (French, Holy Roman, English) are at manuscript-
  witness granularity; Byzantine records are aligned bilingual text
  with a single Constantinople geographical anchor — the geographic
  visualization treats these layers differently.

## Licensing

Application code is released under the **MIT License** (see `LICENSE`).
Scholarly content (TEI, JSON, CSV, manifests, documentation) is released
under **CC BY 4.0** (see `LICENSE-content.md`). Manuscript reproductions
remain governed by the rights statements of the holding institutions.
