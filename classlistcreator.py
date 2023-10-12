import requests
from bs4 import BeautifulSoup
import json

majorLinks = ['arctic.html', 'hnrs.html', 'lead.html', 'academ.html', 'afamst.html', 'aes.html', 'asamst.html', 'chist.html', 'swa.html', 'taglg.html', 'ais.html', 'anthro.html', 'archeo.html', 'bioanth.html', 'appmath.html', 'cfrm.html', 'art.html', 'arthis.html', 'design.html', 'artsci.html', 'arts.html', 'asianll.html', 'beng.html', 'chinese.html', 'hindi.html', 'indian.html', 'indo.html', 'japanese.html', 'korean.html', 'sanskrit.html', 'sasian.html', 'urdu.html', 'viet.html', 'astro.html', 'astbio.html', 'biology.html', 'cs&ss.html', 'csde.html', 'centhum.html', 'chem.html', 'cms.html', 'complit.html', 'clarch.html', 'cling.html', 'clas.html', 'greek.html', 'latin.html', 'com.html', 'commld.html', 'chid.html', 'dance.html', 'dxarts.html', 'disst.html', 'drama.html', 'econ.html', 'engl.html', 'french.html', 'italian.html', 'txtds.html', 'gwss.html', 'genst.html', 'gis.html', 'indiv.html', 'geog.html', 'germ.html', 'jsise.html', 'ancmedh.html', 'hstcmp.html', 'hstafm.html', 'histasia.html', 'hstlac.html', 'modeuro.html', 'histam.html', 'hstry.html', 'centhum.html', 'intsci.html', 'religion.html', 'jsis.html', 'jsisa.html', 'jsisb.html', 'jsisc.html', 'jsisd.html', 'jsise.html', 'jewst.html', 'labor.html', 'lsj.html', 'asl.html', 'ling.html', 'lit.html', 'math.html', 'arabic.html', 'aramic.html', 'coptic.html', 'egypt.html', 'geez.html', 'hebrew.html', 'bibheb.html', 'modheb.html', 'melc.html', 'persian.html', 'turkc.html', 'chgtai.html', 'kazakh.html', 'kyrgyz.html', 'uygur.html', 'uzbek.html', 'turkish.html', 'ugarit.html', 'music.html', 'appmus.html', 'mused.html', 'musensem.html', 'mushist.html', 'musicp.html', 'nbio.html', 'neusci.html', 'ethics.html', 'hps.html', 'phil.html', 'phys.html', 'polisci.html', '95psycap.html', 'psycln.html', 'psych.html', 'danish.html', 'eston.html', 'finnish.html', 'icel.html', 'latvian.html', 'lith.html', 'norweg.html', 'scand.html', 'swedish.html', 'bcms.html', 'bulgar.html', 'czech.html', 'georg.html', 'glits.html', 'polish.html', 'romanian.html', 'russian.html', 'slavic.html', 'slvn.html', 'ukrain.html', 'socsci.html', 'soc.html', 'port.html', 'spanish.html', 'spanlin.html', 'sphsc.html', 'stat.html', 'archit.html', 'be.html', 'constmgmt.html', 'landscape.html', 're.html', 'commenv.html', 'ipm.html', 'urbdes.html', 'acctg.html', 'admin.html', 'ba.html', 'barm.html', 'busan.html', 'buscomm.html', 'busecon.html', 'bpol.html', 'ebiz.html', 'entre.html', 'finance.html', 'hrmob.html', 'infosys.html', 'msis.html', 'intlbus.html', 'mgmt.html', 'mktg.html', 'opmgmt.html', 'orgenv.html', 'qmeth.html', 'stratm.html', 'scm.html', 'dentcl.html', 'dentel.html', 'dentfn.html', 'dentgp.html', 'denthy.html', 'dentpc.html', 'dentsl.html', 'dphs.html', 'dent.html', 'endo.html', 'oralbio.html', 'ohs.html', 'oralm.html', 'os.html', 'orthod.html', 'pedodon.html', 'perio.html', 'pros.html', 'restor.html', 'edci.html', 'indsrf.html', 'ece.html', 'ecfs.html', 'teached.html', 'edlp.html', 'edpsy.html', 'sped.html', 'aa.html', 'ae.html', 'cheng.html', 'nme.html', 'cee.html', 'cesi.html', 'cewa.html', 'cesg.html', 'cet.html', 'cse.html', 'csed.html', 'ee.html', 'engr.html', 'hcde.html', 'inde.html', 'mse.html', 'meche.html', 'meie.html', 'fish.html', 'atmos.html', 'cenv.html', 'scit.html', 'ess.html', 'envst.html', 'bse.html', 'esrm.html', 'sefs.html', 'fhl.html', 'smea.html', 'marbio.html', 'ocean.html', 'quantsci.html', 'quante.html', 'qrc.html', 'info.html', 'insc.html', 'imt.html', 'lis.html', 'museum.html', 'bpsd.html', 'data.html', 'grad.html', 'hcid.html', 'hdd.html', 'iphd.html', 'mcb.html', 'moleng.html', 'nearmide.html', 'neuro.html', 'pubsch.html', 'stss.html', 'techin.html', 'bioeng.html', 'medeng.html', 'pharbe.html', 'gh.html', 'uconjoint.html', 'law.html', 'lawa.html', 'lawb.html', 'lawc.html', 'lawe.html', 'lawh.html', 'lawp.html', 'lawt.html', 'anest.html', 'bioch.html', 'bh.html', 'biostruct.html', 'bime.html', 'compmed.html', 'conj.html', 'famed.html', 'medlic.html', 'genome.html', 'hms.html', 'humbio.html', 'immun.html', 'labmed.html', 'patho.html', 'medsci.html', 'medem.html', 'gcnsl.html', 'medicine.html', 'medeck.html', 'medrck.html', 'microbio.html', 'molmed.html', 'neurosurg.html', 'neurl.html', 'obgyn.html', 'ophthal.html', 'orthop.html', 'otol.html', 'pediat.html', 'pharma.html', 'physiolbio.html', 'psychbehav.html', 'radonc.html', 'radiol.html', 'rhbpo.html', 'rehab.html', 'surg.html', 'uro.html', 'iecmh.html', 'nsg.html', 'nursing.html', 'nursingcl.html', 'nursingmeth.html', 'heor.html', 'medchem.html', 'pharmceu.html', 'pharmacy.html', 'phrmcy.html', 'pharmp.html', 'phrmpr.html', 'phrmra.html', 'pubpol.html', 'ppm.html', 'biostat.html', 'envh.html', 'epidem.html', '95hihim.html', 'hlthsvcs.html', 'hsmgmt.html', 'nutrit.html', 'pathobio.html', 'phg.html', 'phi.html', 'sph.html', '88aerosci.html', '88milsci.html', '88navsci.html', 'socwlbasw.html', 'socwl.html', 'socwk.html']

prefix = "https://www.washington.edu/students/timeschd/AUT2023/"
overall = []

for suffix in majorLinks:
    print(suffix)
    current = []

    r = requests.get("https://www.washington.edu/students/timeschd/AUT2023/" + suffix)
    soup = BeautifulSoup(r.content, features="html.parser")

    tables = soup.body.find_all('table')
    del tables[0:3]
    for table in tables:
        children = [child.string for child in table.descendants if child.name == None]
        children.pop(0)
        if 'pre' in [child.name for child in table.descendants]:
            links = table.find_all("a")
            if len(links) == 1:
                continue
            obj = {}
            if children[1].split()[2] == "to":
                continue
            obj["sln"] = int(links[0].contents[0])
            links.pop(0)
            obj["letter"] = children[1].split()[0]
            obj["credits"] = (children[1].split()[1])
            obj["locations"] = [{"days": children[1].split()[2], "time": children[1].split()[3], "building": links[0].contents[0], "room": children[3].split()[0]}]
            links.pop(0)
            additional = 0
            while len(links) > 0:
                times = children[3 + (2*additional)].split("\n")[1].split()
                extra = {}
                extra["days"] = times[0]
                extra["time"] = times[1]
                extra["building"] = links[0].contents[0]
                extra["room"] = children[5 + (2*additional)].split()[0]
                obj["locations"].append(extra)
                links.pop(0)
            current[-1]["classes"].append(obj)
        else:
            current.append({"name": " ".join(children[0].split()), "classes":[]})

    overall.append({"suffix": suffix, "items": current})

with open('result.json', 'w') as f:
    json.dump(overall, f)
# for c in current:
#     print(c["name"], [d for d in c["classes"]])