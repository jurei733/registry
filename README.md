# Verona Registry

This repository is a generated catalog of Verona-related repositories.

- Scanned owners: `iqb-berlin`
- Sync triggers: daily schedule, manual dispatch, and `repository_dispatch` with `event_type=registry-sync`
- Generated files: `README.md` and `registry.json`
- Metadata precedence: release asset HTML, then matching release/tag ref HTML, then GitHub release/tag metadata

## Repositories

### [verona-data-specifications](https://github.com/iqb-berlin/verona-data-specifications)
- Description: This repo contains of all iqb data specifications related to verona-interfaces.
- Default branch: `main`
- Last pushed: 2022-11-07
- Latest release: [0.1.0](https://github.com/iqb-berlin/verona-data-specifications/releases/tag/0.1.0) (2022-11-07)

### [verona-editor-dan](https://github.com/iqb-berlin/verona-editor-dan)
- Description: No repository description.
- Default branch: `master`
- Last pushed: 2021-05-03
- Latest release: [v3.1.0](https://github.com/iqb-berlin/verona-editor-dan/releases/tag/v3.1.0) (2021-05-03)
- Module metadata: `json-ld` extracted from release asset `iqb-editor-dan@3.1.0.html`

```json
{
  "@context": "https://w3id.org/iqb/verona-modules",
  "@id": "iqb-editor-dan",
  "@type": "editor",
  "apiVersion": "2.0",
  "description": {
    "de": "Dieser Editor verarbeitet Aufgabendefinitionen in einem eigenen, undokumentierten Format. Anzeige- und Interaktionselemente können frei positioniert werden auf einer oder über mehreren Seiten.",
    "en": "This Verona Editor uses a specific undocumented unit definition format. You can place elements for display or interaction purposes freely on one or more pages."
  },
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": {
      "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
      "en": "IQB - Institute for Educational Quality Improvement"
    },
    "url": "https://www.iqb.hu-berlin.de"
  },
  "name": {
    "de": "IQB-Editor für komplexe Testaufgaben (Dan)",
    "en": "IQB editor for complex test units (Dan)"
  },
  "notSupportedFeatures": [
    "report-eager"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/iqb-berlin/verona-editor-plaintext"
  },
  "version": "3.1.0"
}
```

### [verona-editor-plaintext](https://github.com/iqb-berlin/verona-editor-plaintext)
- Description: Provides one big text input element to edit script based unit definitions or to hack others.
- Default branch: `master`
- Last pushed: 2021-05-03
- Latest release: [v1.0.1](https://github.com/iqb-berlin/verona-editor-plaintext/releases/tag/v1.0.1) (2021-05-03)
- Module metadata: `json-ld` extracted from release asset `iqb-editor-plaintext@1.0.1.html`

```json
{
  "@context": "https://w3id.org/iqb/verona-modules",
  "@id": "iqb-editor-plaintext",
  "@type": "editor",
  "apiVersion": "2.0",
  "description": {
    "de": "Dieser Editor verarbeitet Aufgaben-/Seitendefinitionen als Text. Dies ist sinnvoll z. B. für Xml-, Html- oder scriptbasierte Formate, für die kein separater Editor bereitgestellt wird.\n\nAchtung: Für binäre oder JSON-Formate sollten andere Editoren genutzt werden, die die Konsistenz der Daten sicherstellen. Eine Bearbeitung dieser Formate mit diesem Text-Editor kann die Aufgaben-/Seitendefinitionen unbrauchbar machen.",
    "en": "You can use this Verona Editor for all unit definitions, because the data format of unit definitions is technically always string/text. But be careful: improper changes may damage the definition so it's not usable anymore."
  },
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": {
      "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
      "en": "IQB - Institute for Educational Quality Improvement"
    },
    "url": "https://www.iqb.hu-berlin.de"
  },
  "name": {
    "de": "IQB-Editor für Text",
    "en": "IQB editor for plain text"
  },
  "notSupportedFeatures": [
    "report-eager"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/iqb-berlin/verona-editor-plaintext"
  },
  "version": "1.0.1"
}
```

### [verona-modules-aspect](https://github.com/iqb-berlin/verona-modules-aspect)
- Description: No repository description.
- Default branch: `develop`
- Last pushed: 2026-06-24
- Latest release: [editor/2.12.5+player/2.12.5](https://github.com/iqb-berlin/verona-modules-aspect/releases/tag/editor/2.12.5%2Bplayer/2.12.5) (2026-05-12)

### [verona-modules-ib](https://github.com/iqb-berlin/verona-modules-ib)
- Description: No repository description.
- Default branch: `master`
- Last pushed: 2025-05-26
- Latest release: none

### [verona-modules-speedtest](https://github.com/iqb-berlin/verona-modules-speedtest)
- Description: No repository description.
- Default branch: `master`
- Last pushed: 2026-01-16
- Latest release: [3.3.0](https://github.com/iqb-berlin/verona-modules-speedtest/releases/tag/3.3.0) (2026-01-16)

### [verona-modules-stars](https://github.com/iqb-berlin/verona-modules-stars)
- Description: No repository description.
- Default branch: `develop`
- Last pushed: 2026-06-26
- Latest release: [0.6.40](https://github.com/iqb-berlin/verona-modules-stars/releases/tag/0.6.40) (2026-06-24)

### [verona-player-abi](https://github.com/iqb-berlin/verona-player-abi)
- Description: A programmable item-player for surveys. Contains: Player-Plugin, Editor-Plugin
- Default branch: `master`
- Last pushed: 2026-02-07
- Latest release: [5.0.0](https://github.com/iqb-berlin/verona-player-abi/releases/tag/5.0.0) (2025-03-11)
- Module metadata: `json-ld` extracted from release asset `verona-player-abi-5.0.0.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://opensource.org/licenses/MIT",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-abi"
  },
  "description": [
    {
      "lang": "de",
      "value": "Dieser Player interpretiert eine Script-Sprache, die speziell für die effiziente Erstellung umfangreicher Befragungen entwickelt wurde. Über die gängigen Frageformate hinaus werden bedingte Formularblöcke, dynamische Wiederholungen von Blöcken und Likert-skalen unterstützt."
    },
    {
      "lang": "en",
      "value": "You can use this Verona Player for surveys where you need a large number of questions. By interpreting it's own script language, the player just need one line per control definition. You can setup conditional blocks, repeating blocks or likert scale tables."
    }
  ],
  "id": "iqb-player-abi",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "en",
        "value": "IQB - Institute for Educational Quality Improvement."
      },
      {
        "lang": "de",
        "value": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen."
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "2.0",
  "name": [
    {
      "lang": "en",
      "value": "IQB player for script language"
    },
    {
      "lang": "de",
      "value": "IQB-Player für Skripte (Abi)"
    }
  ],
  "notSupportedFeatures": [
    "log-policy",
    "paging-mode"
  ],
  "specVersion": "5.0",
  "type": "player",
  "version": "5.0.0"
}
```

### [verona-player-dan](https://github.com/iqb-berlin/verona-player-dan)
- Description: The IQB Verona Item Player and Editor until 2021.
- Default branch: `master`
- Last pushed: 2023-01-03
- Latest release: [3.1.0](https://github.com/iqb-berlin/verona-player-dan/releases/tag/3.1.0) (2023-01-03)
- Module metadata: `json-ld` extracted from release asset `iqb-player-dan@3.1.0.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://opensource.org/licenses/MIT",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-dan"
  },
  "description": [
    {
      "lang": "de",
      "value": "Dieser Player interpretiert Aufgabendefinitionen in einem eigenen, undokumentierten Format. Anzeige- und Interaktionselemente können frei positioniert werden auf einer oder über mehreren Seiten."
    },
    {
      "lang": "en",
      "value": "This Verona Player uses a specific undocumented unit definition format. You can place elements for display or interaction purposes freely on one or more pages."
    }
  ],
  "id": "iqb-player-dan",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "en",
        "value": "IQB - Institute for Educational Quality Improvement."
      },
      {
        "lang": "de",
        "value": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen."
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "2.0",
  "name": [
    {
      "lang": "en",
      "value": "IQB player for static assessment units (dan)"
    },
    {
      "lang": "de",
      "value": "IQB-Player für statische Testaufgaben (Dan)"
    }
  ],
  "notSupportedFeatures": [
    "log-policy",
    "paging-mode"
  ],
  "specVersion": "5.0",
  "type": "player",
  "version": "3.1.0-beta"
}
```

### [verona-player-lottie](https://github.com/iqb-berlin/verona-player-lottie)
- Description: player for lottie animations implementing verona specs
- Default branch: `develop`
- Last pushed: 2026-06-22
- Latest release: [1.0.6](https://github.com/iqb-berlin/verona-player-lottie/releases/tag/1.0.6) (2026-05-08)
- Module metadata: `json-ld` extracted from release asset `iqb-player-lottie-1.0.6.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://opensource.org/licenses/MIT",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-lottie"
  },
  "description": [
    {
      "lang": "de",
      "value": "Todo"
    }
  ],
  "id": "iqb-player-lottie",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "de",
        "value": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen"
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "3.1",
  "name": [
    {
      "lang": "de",
      "value": "IQB-Player für Lottie Animationen"
    }
  ],
  "notSupportedFeatures": [
    "log-policy"
  ],
  "specVersion": "6.0",
  "type": "PLAYER",
  "version": "1.0.6"
}
```

### [verona-player-simple](https://github.com/iqb-berlin/verona-player-simple)
- Description: A dependency-free, vanilla-js Verona-Player which can run HTML-forms as Units
- Default branch: `main`
- Last pushed: 2026-04-22
- Latest release: [6.0.4](https://github.com/iqb-berlin/verona-player-simple/releases/tag/6.0.4) (2024-11-06)
- Module metadata: `json-ld` extracted from release asset `verona-player-simple-6.0.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://raw.githubusercontent.com/iqb-berlin/verona-player-simple/main/LICENSE",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-simple"
  },
  "description": [
    {
      "lang": "en",
      "value": "This is a simple, dependency-less, vanilla-js-written, but full-featured unit player, mainly as showcase for developers and for software-testing. It does implement the Verona 4.0.0-Standard and can be used for units containing simple any content in HTML-format. Unit Description ist the <code>form</code>-content as HTML. Just give some names to the form element, and the player does the rest. Use some special Ids for some special buttons."
    }
  ],
  "id": "verona-player-simple",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "en",
        "value": "IQB - Institute for Educational Quality Improvement"
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "2.0",
  "name": [
    {
      "lang": "en",
      "value": "Simple HTML Player"
    }
  ],
  "specVersion": "6.0",
  "type": "player",
  "version": "6.0.4"
}
```

### [verona-player-speedtest](https://github.com/iqb-berlin/verona-player-speedtest)
- Description: verona-player-speedtest
- Default branch: `master`
- Last pushed: 2024-04-10
- Latest release: [1.2.0](https://github.com/iqb-berlin/verona-player-speedtest/releases/tag/1.2.0) (2022-12-21)
- Module metadata: `json-ld` extracted from release asset `verona-player-speedtest-1.2.0.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://opensource.org/licenses/MIT",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-speedtest"
  },
  "description": [
    {
      "lang": "de",
      "value": "The Speed-Test-Player is a Verona-player for reading speed tests. It's units are just strings - mostly simple sentences. The player shows the sentence and two buttons. Clicking one button submits response data (for first button `A` or for second button `B`) and requests the host to navigate to the next unit/page."
    }
  ],
  "id": "verona-player-speedtest",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "en",
        "value": "IQB - Institute for Educational Quality Improvement. It has been developed in behalf of the Institut für Bildungsanalysen Baden-Württemberg (IBBW)."
      },
      {
        "lang": "de",
        "value": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen. Der Player wurde ursprünglich im Auftrag des Instituts für Bildungsanalysen Baden-Württemberg entwickelt."
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "2.0",
  "name": [
    {
      "lang": "en",
      "value": "Speed-Test-Player"
    },
    {
      "lang": "de",
      "value": "Speed-Test-Player"
    }
  ],
  "notSupportedFeatures": [
    "log-policy",
    "paging-mode",
    "navigation-denied"
  ],
  "specVersion": "5.0",
  "type": "player",
  "version": "1.2.0"
}
```

### [verona-player-testbed](https://github.com/iqb-berlin/verona-player-testbed)
- Description: web application to test offline player and unit definition
- Default branch: `develop`
- Last pushed: 2026-01-28
- Latest release: [3.2.1](https://github.com/iqb-berlin/verona-player-testbed/releases/tag/3.2.1) (2026-01-27)
- Module metadata: `html-meta` extracted from release asset `verona-player-testbed-3.2.1.html`

```json
{
  "content": "width=device-width, initial-scale=1"
}
```

### [verona-player-widget](https://github.com/iqb-berlin/verona-player-widget)
- Description: demo player for verona widget calls
- Default branch: `develop`
- Last pushed: 2026-01-28
- Latest release: [0.3.0](https://github.com/iqb-berlin/verona-player-widget/releases/tag/0.3.0) (2026-01-28)
- Module metadata: `json-ld` extracted from release asset `verona-player-widget-0.3.0.html`

```json
{
  "$schema": "https://raw.githubusercontent.com/verona-interfaces/metadata/master/verona-module-metadata.json",
  "code": {
    "licenseType": "MIT",
    "licenseUrl": "https://opensource.org/licenses/MIT",
    "repositoryType": "git",
    "repositoryUrl": "https://github.com/iqb-berlin/verona-player-dummy"
  },
  "description": [
    {
      "lang": "de",
      "value": "IQB-Player zum Aufruf eines Widgets"
    }
  ],
  "id": "verona-player-widget",
  "maintainer": {
    "email": "iqb-tbadev@hu-berlin.de",
    "name": [
      {
        "lang": "de",
        "value": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen"
      }
    ],
    "url": "https://www.iqb.hu-berlin.de"
  },
  "metadataVersion": "3.0",
  "name": [
    {
      "lang": "de",
      "value": "IQB-Player zum Aufruf eines Widgets"
    }
  ],
  "notSupportedFeatures": [
    "log-policy"
  ],
  "specVersion": "6.1",
  "type": "player",
  "version": "0.3.0"
}
```

### [verona-registry](https://github.com/iqb-berlin/verona-registry)
- Description: This registry helps applications for online assessment to find players, editors and other verona-interfaces related modules.
- Default branch: `master`
- Last pushed: 2020-12-11
- Latest release: none

### [verona-widget-calc](https://github.com/iqb-berlin/verona-widget-calc)
- Description: simple calculator widget implementing verona specs
- Default branch: `master`
- Last pushed: 2026-01-28
- Latest release: [0.1.3](https://github.com/iqb-berlin/verona-widget-calc/releases/tag/0.1.3) (2026-01-28)

### [verona-widgets-chemistry](https://github.com/iqb-berlin/verona-widgets-chemistry)
- Description: Chemistry widgets for verona integration
- Default branch: `develop`
- Last pushed: 2026-06-23
- Latest release: [1.0.0](https://github.com/iqb-berlin/verona-widgets-chemistry/releases/tag/1.0.0) (2026-06-23)
