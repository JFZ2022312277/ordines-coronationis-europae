# OCR 错误核查报告
**文件：** 英国9-10世纪加冕礼仪书（2023年最新版！）.xml  
**底本：** Pratt 2023 PDF（逐页核对）  
**核查范围：** ENG-ORDO-I（第一礼仪书）全文 + ENG-ORDO-IIA（第二礼仪书A版）全文  
**核查说明：** ENG-ORDO-I已经过逐页人工校对；ENG-ORDO-IIA（原标注为"globally cleaned and selectively reproofread on the most OCR-damaged pages"）错误最多，本报告重点列出此部分。

---

## 一、错误类型概述

1. **行首字母截断**：OCR扫描双栏排版时，正文栏左边缘被裁切，造成大量词首字母丢失（集中于parallel n="5"，即PDF第88页）
2. **字符误读**：单个字母被OCR识别错误（m/in、e/c、o/a、l/i等混淆）
3. **脚注文字混入正文**：脚注编号（上标字母a/b/c/d及数字）和脚注全文被OCR误纳入正文
4. **拼版OCR垃圾**：英文译文列内容破损严重（"andeaz1h"、"uc:1"、"~fis of • '· •••,."等）
5. **词间距丢失或错误断行**：两词拼合（"thathe"）或词中多余空格（"REG INAM"）
6. **大写字母行首缺失**：标题/大写正文段首字母丢失（"ENEDICTIO"、"hristus"等）

---

## 二、逐条错误列表

### ENG-ORDO-IIA · Parallel n="4"（PDF第87页）— 英文译文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `andeaz1h` | `and earth` | 'rth'被OCR误读 |
| 2 | `mak:er` | `maker` | 冒号为OCR噪点 |
| 3 | `ange]s` | `angels` | ']'误读为'l' |
| 4 | `and ve him from the lion's mouth and from the band of the beastandof uc:1` | `and save him from the lion's mouth and from the hand of the beast and of Goliath` | "sa"截断；band→hand；"uc:1"为"Goliath"严重误读 |
| 5 | `multiply the ~fis of • '· •••,. blessings over this your servant` | `multiply the gifts of [your] blessings over this your servant` | 中间系排版OCR垃圾，对应拉丁文"benedictionum tuarum dona multiplica" |
| 6 | `we do. et to the kingdom` | `we do elect to the kingdom`（或`we do...elect`） | "et"为"elect"残字 |

---

### ENG-ORDO-IIA · Parallel n="5"（PDF第88页）— 拉丁正文（行首截断最严重）

> **注：** 该页正文栏左边缘被OCR裁切，大量词首字母丢失，已对照PDF右栏（Second Ordo A edited text）逐一核查。

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `firrnatus` | `firmatus` | 多余'r' |
| 2 | `mansue- udine` | `mansuetudine` | 断行OCR错误 |
| 3 | `ap1entia` | `sapientia` | 词首's'截断；'1'误读'i' |
| 4 | `omplaceat` | `complaceat` | 词首'c'截断 |
| 5 | `noffenso` | `inoffenso` | 词首'i'截断 |
| 6 | `otius albionis ecclesiamc` | `totius albionis ecclesiam` | 词首't'截断；上标'c'为脚注标记，非正文 |
| 7 | `um plebibus` | `cum plebibus` | 词首'c'截断 |
| 8 | `c doceat` | `ac doceat` | 词首'a'截断 |
| 9 | `contraque mnes uisibiles et inuisibiles hastes` | `contraque omnes uisibiles et inuisibiles hostes` | mnes→omnes；hastes→hostes（a/o误读） |
| 10 | `dem patenter` | `idem patenter` | 词首'i'截断 |
| 11 | `tuae uirtutis egimen arnministret` | `tuae uirtutis regimen administret` | "egimen"词首'r'截断；"arnministret"中'rn'为'dm'误读（应为"administret"） |
| 12 | `idelicet francorum sceptrad` | `uidelicet francorum sceptra` | 词首'u'截断；末尾'd'为脚注标记 |
| 13 | `ed ad pristine` | `sed ad pristinae` | 词首's'截断 |
| 14 | `orum animas` | `eorum animas` | 词首'e'截断 |
| 15 | `trorumque horum` | `utrorumque horum` | 词首'u'截断 |
| 16 | `ubiectione fultus` | `subiectione fultus` | 词首's'截断 |
| 17 | `lorificatus` | `glorificatus` | 词首'g'截断 |
| 18 | `aternae apicem gloriae` | `paternae apicem gloriae` | 词首'p'截断 |
| 19 | `protectlonis` | `protectionis` | 'l'误读为'i' |
| 20 | `iugiter rotectus` | `iugiter protectus` | 词首'p'截断 |
| 21 | `circum- atus` | `circumdatus` | 断行OCR错误，缺'd' |
| 22 | `obtabilis` | `optabilis` | 'b'误读'p' |
| 23 | `de ostibus` | `de hostibus` | 词首'h'截断 |
| 24 | `suae otentiae` | `suae potentiae` | 词首'p'截断 |

---

### ENG-ORDO-IIA · Parallel n="5"（PDF第88页）— 英文译文（行间距/拼写）

| # | XML现有文本 | 应更正为 |
|---|---|---|
| 1 | `thathe, baving been` | `that he, having been` |
| 2 | `aforementionedAbraham` | `aforementioned Abraham` |
| 3 | `hein turn` | `he in turn` |
| 4 | `patemal glory` | `paternal glory` |
| 5 | `ofboth these peoples` | `of both these peoples` |
| 6 | `ofyour power` | `of your power` |

---

### ENG-ORDO-IIA · Parallel n="6"（PDF第89页）— 英文译文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `adomed your aforemeu tioned` | `adorned your aforementioned` | 'd'脱落；断字错误 |
| 2 | `set him o high` | `set him on high` | 'n'脱落（PDF原文为"oo"，亦系错误，正确应为"on"） |
| 3 | `tlow upon his head` | `flow upon his head` | 't'误读'f' |
| 4 | `a pnest by the anointing` | `a priest by the anointing` | 'ri'缩为'n'（OCR常见错误） |
| 5 | `unguentrnade kings` | `unguent made kings` | 两词拼合，'r'为噪点 |
| 6 | `finally attam fellowship` | `finally attain fellowship` | 'm'误读'in' |
| 7 | `the dernons of the air` | `the demons of the air` | 'r'噪点插入 |
| 8 | `ascended victonous` | `ascended victorious` | 'n'误读'ri' |

---

### ENG-ORDO-IIA · Parallel n="7"（PDF第90页）— 英文译文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `hwnble` | `humble` | 'wn'误读'um' |
| 2 | `whointhe beginning` | `who in the beginning` | 词间距丢失 |
| 3 | `a &lt;love carrying` | `a dove carrying` | XML中'&lt;'（即'<'）为'd'的OCR误读；两处均如此（第二处"in the likeness of a &lt;love"同） |
| 4 | `a pnest by the anointing` | `a priest by the anointing` | 同第89页 |
| 5 | `unguentrnade` | `unguent made` | 同第89页 |

---

### ENG-ORDO-IIA · Parallel n="8"（PDF第91页）— 拉丁正文 & 英文译文

**拉丁文：**

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `inuisibilia perc1pere et temporalia regnab_` | `inuisibilia percipere et temporali regno` | '1'误读'i'；'b_'为脚注标记混入（参见PDF脚注b）；"temporalia regna"→"temporali regno" |

**英文译文：**

| # | XML现有文本 | 应更正为 |
|---|---|---|
| 1 | `withlhe oil of gladness` | `with the oil of gladness` |
| 2 | `fue holy unguent` | `the holy unguent` |
| 3 | `the Holy Spin!` | `the Holy Spirit`（'!'为't'误读） |
| 4 | `perceive bofu invisible` | `perceive both invisible`（'fu'误读'th'） |
| 5 | `with hîm` | `with him`（î为OCR噪点） |
| 6 | `may Iearn` | `may learn`（大写'I'误作小写'l'） |
| 7 | `backyour` | `back your` |

---

### ENG-ORDO-IIA · Parallel n="9"（PDF第92页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `eicere ornnes inimicos` | `eicere omnes inimicos` | 'rn'误读'm' |
| 2 | `sancte dei ecc!esiae` | `sancte dei ecclesiae` | '!'误读'l' |
| 3 | `regnumque tibi comm1ssum` | `regnumque tibi commissum` | '1'误读'i' |
| 4 | `per auxilium muictissimi` | `per auxilium inuictissimi` | 'm'误读'in'（PDF右栏核实为"inuictissimi"） |
| 5 | `me CORONETVR` | `HIC CORONETVR` | 'me'为'HIC'截断后的残字 |
| 6 | `corona glorie atque iust1tiae` | `corona gloriae atque iustitiae` | '1'误读'i' |
| 7 | `ornnis hostium suorum` | `omnis hostium suorum` | 'rn'误读'm' |

---

### ENG-ORDO-IIA · Parallel n="10"（PDF第93页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `diuitias gratiae ttiae` | `diuitias gratiae tuae` | 'tt'误读'tu'（PDF右栏核实） |
| 2 | `rectos paciflces` | `rectos pacifices` | 'fl'误读'fi' |
| 3 | `et"` | `et` | 引号为脚注标记（对应脚注a） |

---

### ENG-ORDO-IIA · Parallel n="11"（PDF第94页）— 拉丁正文 & 英文译文

**拉丁文（脚注标记混入正文）：**

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `prestiturn•` | `prestitum` | 'n'为OCR噪点；'•'为脚注标记 |
| 2 | `prolixitatemb` | `prolixitatem` | 末尾'b'为脚注标记（上标b） |
| 3 | `disperdasque•` | `disperdasque` | '•'为脚注标记 |
| 4 | `sceptrumb` | `sceptrum` | 末尾'b'为脚注标记（上标b） |

**英文译文：**

| # | XML现有文本 | 应更正为 |
|---|---|---|
| 1 | `stretch out the band to the lapsed` | `stretch out the hand to the lapsed` |
| 2 | `lift up the iowiy` | `lift up the lowly`（'iow'误读'low'） |
| 3 | `who says of himseif` | `who says of himself`（'if'误读'lf'） |
| 4 | `pro• uet David sang` | `prophet David sang`（"pro• uet"为"prophet"严重误读） |
| 5 | `Therod of -;:rr kmgdom is a rod of equity` | `The rod of [your] kingdom is a rod of equity`（"-;:rr kmgdom"为严重OCR垃圾） |

---

### ENG-ORDO-IIA · Parallel n="12"（PDF第95页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `donum uae protectionis` | `donum suae protectionis` | 词首's'截断 |
| 2 | `muro elicitatis` | `muro felicitatis` | 词首'f'截断（PDF右栏核实） |
| 3 | `anctae manae` | `sanctae Mariae` | 词首's'截断；"manae"为"Mariae"误读 |
| 4 | `sanctique gregorü anglorum apostolici O •` | `sanctique gregorii anglorum apostolici` | 'ü'误读'ii'；"O •"为脚注标记（对应脚注a）混入 |
| 5 | `ntercedentibus meritis` | `intercedentibus meritis` | 词首'i'截断 |
| 6 | `ndulgeat tibi do minus` | `Indulgeat tibi dominus` | 词首'I'截断；"do minus"应为"dominus"（空格错误） |
| 7 | `Angel os suos bonos` | `Angelos suos bonos` | 词中误插空格 |
| 8 | `qui e precedant` | `qui te precedant` | 'te'缩为'e'（PDF右栏核实） |
| 9 | `d custodiam tui ponat` | `ad custodiam tui ponat` | 词首'a'截断 |
| 10 | `a peccato eu gladio` | `a peccato seu gladio` | 词首's'截断（"eu"→"seu"） |
| 11 | `nimicos tuos` | `Inimicos tuos` | 词首'I'截断 |
| 12 | `et amabilem facial` | `et amabilem faciat` | 'l'误读't'（字尾） |
| 13 | `super te autem anctificatio` | `super te autem sanctificatio` | 词首's'截断 |
| 14 | `de nuisibilibus atque uisibilibus` | `de inuisibilibus atque uisibilibus` | 词首'i'截断（nuisibilibus→inuisibilibus） |

---

### ENG-ORDO-IIA · Parallel n="13"（PDF第96页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `Da ei a tuo spirarnine` | `Da ei a tuo spiramine` | 多余'r'（spirarnine→spiramine） |
| 2 | `ommum scilicet episcoporum` | `omnium scilicet episcoporum` | 'mm'误读'mn'，'u'截断 |
| 3 | `irnpendere memmeris` | `impendere memineris` | 'rn'误读'm'；"memmeris"→"memineris" |
| 4 | `statum] standard form of doxology: 'Quod ipse praestare tu sancto uiuis et regnas deus per omnia saecula`（段末） | **全段删除** | 脚注内容（脚注3的全文）被OCR误纳入正文 |

---

### ENG-ORDO-IIA · Parallel n="14"（PDF第97页）— 拉丁正文（行首截断 + 大写字母行缺失）

**正文部分（与PDF右栏核对）：**

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `ctitudo regis` | `Rectitudo regis` | 词首'Re'截断 |
| 2 | `et solium sublimati` | `et in solium sublimati` | 介词'in'丢失 |
| 3 | `pulo christiano` | `populo christiano` | 词首'po'截断 |
| 4 | `primis ut` | `in primis ut` | 词首'in '截断 |
| 5 | `mnnis populus` | `omnis populus` | 'mn'误读'm'，词首'o'截断 |
| 6 | `ristianus` | `christianus` | 词首'ch'截断 |
| 7 | `seruens in mni tempore` | `seruens in omni tempore` | 'mni'→'omni'（词首'o'截断） |
| 8 | `mnes iniqui tates` | `omnes iniquitates` | 词首'o'截断；词内错误断开 |
| 9 | `terdicat` | `interdicat` | 词首'in'截断 |
| 10 | `diciis` | `iudiciis` | 词首'iu'截断 |
| 11 | `aecipiat` | `praecipiat` | 词首'pr'截断 |
| 12 | `sericordiam•` | `misericordiam` | 词首'mi'截断；'•'为脚注标记 |
| 13 | `misericors us` | `misericors deus` | 'us'→'deus'（词首'd'截断） |

**大写正文/礼仪指示部分（rubrics）：**

| # | XML现有文本 | 应更正为 |
|---|---|---|
| 1 | `dia MS; suam misericordiam et SMN' 1 •`（段首） | **删除**（脚注内容混入） |
| 2 | `T TVNC DEOSCVLETVR` | `ET TVNC DEOSCVLETVR` |
| 3 | `OMNES' LERVM` | `OMNES' CLERVM` |
| 4 | `ET ICAT VNJVSQVJSQVE` | `ET DICAT VNJVSQVJSQVE` |
| 5 | `VIVAT REX ELICITER` | `VIVAT REX FELICITER` |
| 6 | `RIBVS VICIBVS VIVAT REX VT VPRA` | `TRIBVS VICIBVS VIVAT REX VT SVPRA` |
| 7 | `ET OST EVANGELIVM` | `ET POST EVANGELIVM` |
| 8 | `OFFERAT EX AD MANJ/S` | `OFFERAT REX AD MANJ/S` |
| 9 | `BLATIONEM ET VINVM` | `OBLATIONEM ET VINVM` |
| 10 | `ET SIC ERAGATVR MISSA` | `ET SIC PERAGATVR MISSA` |
| 11 | `EINDE COMMVNICETVR` | `DEINDE COMMVNICETVR` |
| 12 | `AB RCHIEPISCOPO CORPORE T SANGVINE` | `AB ARCHIEPISCOPO CORPORE ET SANGVINE` |
| 13 | `ET SIC EFERANT DEO GRATIAS` | `ET SIC REFERANT DEO GRATIAS` |
| 14 | `POST ERGANT AD MENSAM` | `POST PERGANT AD MENSAM` |
| 15 | `llows the likelihood...` 及以下整段 | **删除**（脚注6全文混入正文） |

---

### ENG-ORDO-IIA · Parallel n="15"（PDF第98页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `ITEM AD REG INAM BENEDICENDAM DEBETENIMADDVCIINECCLESIAM` | `ITEM AD REGINAM BENEDICENDAM DEBET ENIM ADDUCI IN ECCLESIAM` | 词中错误插入空格（REG INAM）；多词拼合 |

---

### ENG-ORDO-IIA · Parallel n="17"（PDF第100页）— 拉丁正文

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `WSSA PRO REGIBVS` | `MISSA PRO REGIBVS` | 'W'误读'M'（PDF右栏同误，为PDF原有OCR错误） |
| 2 | `e et in protectione` | `et in protectione` | 行首多余'e' |
| 3 | `ut m superatis•` | `ut superatis` | 'm'为OCR噪点；'•'为脚注标记 |

---

### ENG-ORDO-IIA · Parallel n="18"（PDF第101页）— 拉丁正文（INFRA ACTIONEM段）

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `et exoratus nostra obseruatione concede` | `et exoratus nostra obsecratione concede` | "obseruatione"→"obsecratione"（'ru'误读'cr'；PDF右栏核实） |

> **另注：** parallel n="18"的PRAEFATIO段（"Vere dignum eterne deus. Qui es fons inaccessibilis lucis..."）与PDF右栏编辑本（Second Ordo A）文本有较大差异，疑似OCR取自PDF中间栏（源文本对照列）而非A版编辑正文列。具体差异包括：
> - XML: `fons inaccessibilis lucis` → PDF右栏: `fons inmarcessibilis lucis`
> - XML: `exoram` → PDF右栏: `exoramus`
> - XML: `quem regalibus insignitum uirtutibus ornare placuit` → PDF右栏: `quem regalis dignitatis fastigio uoluisti sublimari`
> - XML缺失: `Honorum hominum adtributor. dignitatumque largitor`（取为"honorum largitor"）
> 建议人工对照PDF第101页右栏重新录入PRAEFATIO段。

---

### ENG-ORDO-IIA · Parallel n="19"（PDF第102页）— 拉丁正文（脚注混入）

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `BENEDJCTIO` | `BENEDICTIO` | 'J'误读'I' |
| 2 | `am' was suggested as a possible reconstruction by 52.`（段末） | **删除** | 脚注12内容混入 |
| 3 | `e standard form of doxology: 'Quod ipse pruestare ritu sancto uiuis et regnas deus per omnia saecula`（段末） | **删除** | 脚注13内容混入 |

---

### ENG-ORDO-IIA · Parallel n="20"（PDF第103页）— 拉丁正文（脚注混入）

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | 段末 `the Preface of the Mass: 'Vere dignum et iustum est atias agere...mal God').` | **删除** | 脚注14全文混入正文 |

---

### ENG-ORDO-IIA · Parallel n="21"（PDF第104页）— 拉丁正文 & 英文译文

**拉丁文：**

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `ENEDICTIO` | `BENEDICTIO` | 词首'B'截断 |
| 2 | `hristus rex regum` | `Christus rex regum` | 词首'C'截断 |
| 3 | `qui regnat aeuum` | `qui regnat in aeuum` | 介词'in'丢失（PDF右栏核实） |
| 4 | `sua ra tuentem` | `sua iura tuentem` | "ra"为"iura"中'iu'截断 |
| 5 | `ilium compsit tauorum stemate` | `illum compsit tritauorum stemate` | 'l'缺失；"tauorum"词首"tri"截断（PDF右栏："tritauorum"） |
| 6 | `Praesidium buat reuerenter` | `Praesidium tribuat reuerenter` | "buat"为"tribuat"词首"tri"截断（PDF右栏核实） |
| 7 | `uictus quo hic cuncta agatisque suisque deles` | `Inuictus quo hic cuncta agatisque suisque fideles` | 词首'In'截断；"deles"→"fideles"词首'fi'截断（PDF右栏核实） |
| 8 | `D COMPLENDVM` | `AD COMPLENDVM` | 词首'A'截断 |
| 9 | `standard fonn of doxology: 'Quod ipse praestare ritu sancto uluis et regnas deus per omnia saecula`（段末） | **删除** | 脚注16全文混入 |

**英文译文：**

（该页英文译文相对完整，但注意中文用户需知）对应"ancestral"一词来自"tritauorum"（tri+avorum，三代以上祖先）。

---

### ENG-ORDO-IIA · Parallel n="22"（PDF第105页）— 标题

| # | XML现有文本 | 应更正为 | 说明 |
|---|---|---|---|
| 1 | `BENEDICTIOVEXILLL` | `BENEDICTIO VEXILLI` | 两词未分开；词尾多一个'L'（"VEXILLI"误读为"VEXILLL"） |

---

## 三、系统性问题总结

### 3.1 脚注文字混入正文（需全文排查）
以下parallel均发现脚注全文或部分内容被误纳入正文，需逐一清除：
- n="13"（p.96）：脚注3
- n="14"（p.97）：脚注6
- n="19"（p.102）：脚注12、13
- n="20"（p.103）：脚注14
- n="21"（p.104）：脚注16

### 3.2 上标脚注字母混入拉丁正文
以下位置有上标脚注字母（a/b/c/d）被误读为正文字符，需删除或改为XML脚注引用：
`ecclesiamc`（p.88）、`sceptrad`（p.88）、`apostolici0`（p.95）、`prestiturn•`（p.94）、`prolixitatemb`（p.94）、`sceptrumb`（p.94）、`disperdasque•`（p.94）、`superatis•`（p.100）、`ceterarumque•`（p.101，如纳入）等

### 3.3 Parallel n="18" PRAEFATIO 段来源疑误
建议专项人工校对，确认是从哪一栏取文。

### 3.4 英文译文OCR质量
英文译文（`xml:lang="en"`段落）的OCR质量整体较差（主要源于PDF原始扫描层），大量词间距丢失、字符误读。ENG-ORDO-I的英文译文已经过逐页人工校对，较为可靠；ENG-ORDO-IIA的英文译文仍有上述各节所列错误，建议对照Pratt 2023打印本重校。

---

*报告生成日期：2026年5月17日*  
*核查工具：pdfplumber文本提取 + 人工逐段比对*
