# 方法地图

> 本文件由 `method-recipes.json` 自动生成。

| 方法 | 名称 | 状态 | 来源 | 事实接入 | 允许执行 |
|---|---|---|---|---|---|
| `ch08-v1-3-movable-rashi-drishti` | 活动星座的相照：相照 3 个固定星座，略去与它相邻的那个固定星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v1-3-fixed-rashi-drishti` | 固定星座的相照：相照 3 个活动星座，略去相邻的那个活动星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v1-3-common-rashi-drishti` | 共同星座的相照：相照其余三个共同星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v1-3-graha-follows-its-rashi-drishti` | 落某星座的行星，其相照与该星座相同 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v4-5-graha-in-movable-rashi-drishti` | 行星落活动星座：相照其余 3 个固定星座，略去紧邻的那个固定星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v4-5-graha-in-fixed-rashi-drishti` | 行星落固定星座：不照紧邻的活动星座，相照其余 3 个活动星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v4-5-graha-in-common-rashi-drishti` | 行星落共同星座：相照其余 3 个共同星座 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch08-v4-5-graha-in-drishtied-rashi-also-receives` | 落在受照星座里的行星，同时也受该相照 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v1-evils-first-then-bhava-effects` | 断十二宫之前，先经上升估量凶象与其化解因素 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v2-no-life-span-calculation-till-24` | 24 岁之前不做确定的寿命推算 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon` | 月亮落六、八、十二宫并受凶星相照：孩子很快去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight` | 同一情形中另有吉星相照：可活到 8 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month` | 吉星逆行落六、八、十二宫受凶星相照：出生一个月内死亡（限上升未被吉星占据） | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v3-6-putr-bhava-shani-mangal-surya-mother-and-brother-die` | 五宫被土星、火星、太阳共同占据：母亲与兄弟去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death` | 火星落一宫或八宫、与土星或太阳同宫或受凶照且无吉照：当即死亡之源 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v7-11-shani-mangal-drishti-lagna-luminaries-with-rahu-fortnight` | 土星与火星相照上升、二曜与罗睺同宫：孩子只活半个月 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v7-11-shani-karm-chandra-ari-mangal-yuvati-death-with-mother` | 土星落十宫、月亮落六宫、火星落七宫：孩子与母亲当即去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v7-11-shani-tanu-chandra-randhr-guru-sahaj-immediate-death` | 土星落一宫、月亮与木星依次落八宫与三宫：当即身故 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v7-11-surya-dharm-mangal-yuvati-guru-shukra-labh-one-month` | 太阳落九宫、火星落七宫、木星与金星落十一宫：寿命只有一个月 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v7-11-any-graha-in-vyaya-short-life` | 十二宫有行星即主短寿，尤以二曜、金星与罗睺为甚；这四星相照十二宫则化解 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic` | 月亮与凶星同落七宫、八宫或一宫且与吉星无关联：致早终 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics` | 生于晨昏交界、月亮的 Horā 或 Gandanta，且月亮与凶星占据自上升起的角宫：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v14-definition-of-sandhya` | 晨昏交界（Sandhya）的界定：日出前 3 Ghati 与日落后同样长的一段 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v15-malefics-oriental-benefics-occidental-vrischik-early-death` | 凶星尽在东半、吉星尽在西半：生于天蝎座（Vrischik）者早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v16-malefics-in-vyaya-ari-or-randhr-dhan-with-lagna-hemmed` | 凶星落十二宫与六宫、或落八宫与二宫，且上升被凶星夹：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v17-malefics-in-tanu-yuvati-chandra-with-malefic-no-relief` | 凶星占据一宫与七宫、月亮与凶星同宫且无吉星救助：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v18-decreasing-chandra-tanu-malefics-randhr-and-kendra` | 渐亏的月亮落一宫，凶星占据八宫与一个角宫：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics` | 月亮落一、八、十二或七宫并被凶星夹：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v20-chandra-tanu-hemmed-with-malefic-in-yuvati-or-randhr` | 月亮落一宫被凶星夹，且七宫或八宫有凶星：连同母亲当即去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v21-shani-vyaya-surya-dharm-mangal-randhr-without-benefic-drishti` | 土星落十二宫、太阳落九宫、火星落八宫且无吉星相照：当即身亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v22-malefic-in-yuvati-or-rising-dreshkan-decreasing-chandra-in-tanu` | 凶星落七宫或上升所在三分盘，渐亏的月亮落一宫：早亡 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v23-all-weak-grahas-in-apoklima-two-or-six-months` | 所有行星无力且都落 Apoklima 宫：寿命只有 2 个月或 6 个月 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v24-chandra-drishtied-by-three-malefics-mother-evil` | 月亮受三颗凶星相照：母亲遭遇凶事（会很快去世） | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v24-benefics-drishti-chandra-good-to-mother` | 吉星相照月亮：给母亲带来好处 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v25-dhan-bhava-five-grahas-posthumous-birth-mother-early-death` | 二宫聚罗睺、水星、金星、太阳与土星：命主生于父亲去世之后，母亲也早去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v26-chandra-seventh-or-eighth-from-malefic-mother-early-end` | 月亮在某凶星的第 7 或第 8 位、自身与凶星同宫又受有力凶星相照：母亲早终 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v27-surya-exalted-or-debilitated-in-yuvati-goat-milk` | 太阳落七宫且入旺或落陷：孩子不吃母乳而吃羊奶 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v28-malefic-in-fourth-from-chandra-inimical-rasi-no-benefic-in-kendra` | 自月亮起第 4 位为敌星座且有凶星、角宫无吉星：孩子早失母亲 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v29-malefics-in-ari-and-vyaya-evils-to-mother` | 凶星落六宫与十二宫：给母亲带来凶事 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v29-malefics-in-bandhu-and-karm-evils-to-father` | 凶星占据四宫与十宫：父亲得到同样的（凶）效果 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v30-budh-in-dhan-malefics-in-tanu-and-vyaya-destroys-family` | 水星落二宫、凶星占一宫与十二宫：此瑜伽毁掉整个家族 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v31-guru-shani-rahu-in-tanu-dhan-sahaj-mother-early-death` | 木星、土星、罗睺依次落一宫、二宫、三宫：母亲早去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v32-malefics-in-konas-from-decreasing-chandra-mother-gives-up-child` | 自渐亏月亮起的三角宫有凶星且不与吉星同宫：母亲会舍弃孩子 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v33-mangal-shani-in-kendra-from-chandra-same-navamsa-two-mothers` | 火星与土星同处自月亮起的角宫且同一九分盘分段：命主有两位母亲，且短寿 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v34-shani-mangal-chandra-in-tanu-yuvati-ari-father-early-death` | 土星、火星、月亮依次落一宫、七宫、六宫：父亲早去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v35-guru-in-tanu-four-grahas-in-dhan-father-lost-at-marriage` | 木星落一宫、土日火水聚二宫：命主结婚之时失去父亲 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v36-surya-with-or-hemmed-by-malefics-and-malefic-in-seventh` | 太阳与凶星同宫或被凶星夹，且自太阳起第 7 位另有凶星：早年失父 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v37-surya-yuvati-mangal-karm-rahu-vyaya-father-not-sustaining` | 太阳落七宫、火星落十宫、罗睺落十二宫：父亲存续的可能极小 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v38-mangal-in-karm-in-enemy-rasi-father-troubled-death` | 火星落十宫且该处为其敌星座：父亲之死既早且多苦 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v39-chandra-ari-shani-tanu-mangal-yuvati-father-not-long-lived` | 月亮落六宫、土星落一宫、火星落七宫：父亲难有长寿 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v40-surya-drishtied-by-shani-in-mesh-or-vrischik-navamsa-father-gone` | 太阳受土星相照且落白羊或天蝎九分盘：父亲在命主出生前已离家或已去世 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v41-malefics-in-bandhu-karm-vyaya-parents-abandon-child` | 四宫、十宫与十二宫都被凶星占据：父母双方都把孩子丢给它自己的命运 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v42-rahu-guru-in-inimical-rasi-in-tanu-or-bandhu-father-absent` | 罗睺与木星同落敌星座且该宫为一宫或四宫：父亲到命主 23 岁才见到他 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v43-45-surya-drishtied-or-hemmed-by-malefics-evils-to-father` | 太阳为父亲的指示星：太阳受凶星相照或被凶星夹，主父亲有凶事 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v43-45-chandra-considered-likewise-for-mother` | 月亮为母亲的指示星：月亮就母亲一事照太阳的同一办法考量 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v43-45-malefics-in-sixth-eighth-fourth-from-surya-father-inauspicious` | 凶星落自太阳起算的第 6、第 8 或第 4 位：父亲之事不吉 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse` | 凶星落自月亮起算的同样位次：对母亲不利 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |
| `ch09-v43-45-estimate-strength-of-occupants` | 对相关占据行星的强弱要作适当估量 | `pilot_candidate` | `single_explicit_source` | `unmapped` | 否 |

方法摘要和查询词不是原文证据；正式回答必须重新取回原文。
