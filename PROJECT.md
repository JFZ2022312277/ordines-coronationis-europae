# Project Documentation

## Project Title

Ordines Coronationis Europae: A Digital Atlas of Medieval Coronation Ordines, Manuscripts, and Ritual Transmission

## Description

This project structures medieval coronation ordines as linked research data. It combines TEI/XML-inspired textual records, manuscript witnesses, repository places, ritual traditions, IIIF image resources, and OpenAtlas-style entity relations. The current public version focuses on French coronation ordines (OCF), Holy Roman imperial coronation ordines (HRE), English coronation records (ECR), and selected pontifical materials.

## Data Model

The site organizes evidence around six research entities:

- Text / Ordo: individual ritual texts such as OCF-XV, HRE-I, or ECR-XIII.
- Manuscript: codicological witnesses with shelfmarks, folios, dates, repositories, and digital links.
- Place: repository locations, liturgical centers, origins, and transmission contexts.
- Actor / Institution: editors, abbeys, cathedrals, libraries, royal or ecclesiastical institutions.
- Event / Movement: copying, use, transmission, edition, and movement events where documented.
- Tradition / Type: OCF, HRE, ECR, PRG, Pontifical, and related controlled groupings.

## Technical Approach

The interface is a static web application using Leaflet for spatial visualization, a local IIIF viewer for manuscript images, and JSON/CSV datasets exported in an OpenAtlas-style structure. The data model is designed to be compatible with a later OpenAtlas or CIDOC CRM implementation, while remaining deployable as a static public site.

## Review Scope

For a review submission, the recommended showcase paths are:

- `#/map` — map of manuscripts, repositories, and selected OpenAtlas-style data layers.
- `#/detail/OCF-XV` — Ratold Ordo case study with manuscript witnesses and network/dispersal data.
- `#/detail/ECR-XIII` — Liber Regalis case study with Latin proofread JSON and IIIF viewer.
- `iiif/viewer.html?manifest=ECR-XIII-LIBER-REGALIS` — local IIIF viewer demonstration.

## Data and Rights Notes

The site contains scholarly metadata, normalized or proofread textual data, and links to external manuscript repositories. Local images and IIIF derivatives should be reviewed for rights and redistribution status before public release. Where public IIIF services exist, external manifests are preferred.
