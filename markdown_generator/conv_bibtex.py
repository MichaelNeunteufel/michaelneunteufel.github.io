import bibtexparser
import pandas as pd

# Load the .bib file
with open('my_bib.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

    # Convert entries to a DataFrame
entries = bib_database.entries
df = pd.DataFrame(entries)

# remove the following entries of the dataframe file,keywords,archiveprefix,abstract,urldate, ENTRYTYPE,ID,langid,issn,collaborator,annotation,copyright,type,primaryclass
df = df.drop(columns=['file', 'keywords', 'archiveprefix', 'abstract', 'urldate', 'ENTRYTYPE', 'ID', 'langid', 'issn', 'collaborator', 'annotation', 'copyright', 'type', 'primaryclass'], errors='ignore')

# Save to CSV
df.to_csv('citations.csv', index=False)

#doi,publisher,eprint,number,month,year,author,title,journal,pages,volume,school,address

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime

parser = bibtex.Parser()
bibdata = parser.parse_file('my_bib.bib')

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    "`": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def CleanUpEntry(bib_entry):
    """
    Clean up a bibtex entry by removing unnecessary fields and formatting.
    """
    # Remove unnecessary fields
    for field in ['file', 'keywords', 'archiveprefix', 'abstract', 'urldate', 'ENTRYTYPE', 'ID', 'langid', 'issn', 'collaborator', 'annotation', 'copyright', 'type', 'primaryclass']:
        if field in bib_entry.keys():
            bib_entry.pop(field, None)


    return bib_entry

for i, bib_id in enumerate(bibdata.entries):
    # if i < 17:
    #     continue
    b = bibdata.entries[bib_id].fields
    if "abstract" in b.keys(): 
        abstract = b["abstract"]
    else:
        abstract = None
    b = CleanUpEntry(b)
    bibdata.entries[bib_id].fields=b
    #print(bibdata.entries[bib_id].type)
    #print(b)


    
    if bibdata.entries[bib_id].type == "article":
        category = "manuscripts"
        if "journal" in b.keys():
            venue = b["journal"]
        else:
            raise ValueError("Journal not found in article entry.")
    elif bibdata.entries[bib_id].type == "misc":
        category = "preprints"
        if "eprint" in b.keys():
            venue = b["eprint"]
        else:
            raise ValueError("Eprint not found in misc entry.")
    elif bibdata.entries[bib_id].type == "phdthesis":
        category = "thesis"
        if "school" in b.keys():
            venue = b["school"]
        else:
            raise ValueError("School not found in thesis entry.")
    elif bibdata.entries[bib_id].type == "conference":
        category = "reports"
        if "booktitle" in b.keys():
            venue = b["booktitle"]
        else:
            raise ValueError("Booktitle not found in conference entry.")
    elif bibdata.entries[bib_id].type == "inproceedings":
        category = "proceedings"
        if "booktitle" in b.keys():
            venue = b["booktitle"]
        else:
            raise ValueError("Booktitle not found in inproceedings entry.")
    else:
        raise ValueError("Entry type " + bibdata.entries[bib_id].type + " not recognized. Please check the bibtex file.")
    if "month" in b.keys(): 
        if(len(b["month"])<3):
            pub_month = "0"+b["month"]
            pub_month = pub_month[-2:]
        elif(b["month"] not in range(12)):
            tmnth = strptime(b["month"][:3],'%b').tm_mon   
            pub_month = "{:02d}".format(tmnth) 
        else:
            pub_month = str(b["month"])
    else:
        pub_month = "01"
    pub_day = "01"
    pub_date = str(b["year"]) + "-" + pub_month + "-" + pub_day

    #strip out {} as needed (some bibtex entries that maintain formatting)
    clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-").replace("(","").replace(")","").replace("$","").replace("'","")
    #print(clean_title)
    md_filename = str(b["year"])+"-"
    authors = ""
    citation = ""
    for author in bibdata.entries[bib_id].persons["author"]:
        md_filename += author.last_names[0][0]
        authors += author.last_names[0] + ", "
        citation += " "+author.first_names[0]+" "+author.last_names[0]+", "
    authors = html_escape(authors[:-2]).replace("{\\&quot;o}", "&ouml;").replace("{\\&quot;u}", "&uuml;").replace("\\&amp;", "&amp;")
    # add first 10 characters of title to filename. if has less than 10 characters, add all available
    if len(clean_title) > 10:
        clean_title = clean_title[:10]
    md_filename += "-" + clean_title

    # save bib entry as .bib file
    #with open("../_publications/
    with open( "../files/bibtex/" + bib_id + ".bib", "w") as bibfile:
        bibfile.write(bibdata.entries[bib_id].to_string("bibtex"))

    html_filename = (md_filename).replace("--","-")
    md_filename = (md_filename + ".md").replace("--","-")

    citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""
    #print(citation)
    #print(md_filename)

    title = b["title"].replace("{\\textasciicircum}", "^").replace("{\\textbackslash}textrm", "").replace("{\\textbackslash}mathrm", "").replace("{\\textbackslash}times", "$$x$$").replace("\\{\\vphantom\\}","").replace("\\vphantom","").replace("\\$","$$").replace("\\{", "{").replace("\\}", "}")
    #print(title)
    ## YAML variables
    md = "---\ntitle: \""   + html_escape(title.replace("{{", "").replace("}}","").replace("\\","")).replace("v{s}","&scaron;") + '"'
    md += """\nauthors: """ +  "'" + authors + "'"
    
    md += """\ncollection: """ +  "publications"
    md += """\ncategory: """ +  category

    md += """\npermalink: """ + "/publication/"  + html_filename
    
    note = False
    if "note" in b.keys():
        if len(str(b["note"])) > 5:
            md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
            note = True

    md += "\ndate: " + str(pub_date) 

    md += "\nvenue: '" + html_escape(venue).replace("\\&amp;", "&amp;") + "'"
    
    url = False
    if  category == "manuscripts":
        pre = "paperurl" 
    elif category == "preprints":
        pre = "arxivurl"
    elif category == "thesis":
        pre = "thesisurl"
    elif category == "reports":
        pre = "reporturl"
    elif category == "proceedings":
        pre = "proceedingurl"
    else:
        raise ValueError("Category " + category + "not recognized.")
    
    if "url" in b.keys():
        if len(str(b["url"])) > 5:
            md += "\n"+pre+": '" + b["url"] + "'"
            url = True
    elif "doi" in b.keys():
        if len(str(b["doi"])) > 5:
            md += "\n"+pre+": 'https://doi.org/" + b["doi"] + "'"
            url = True

    md += "\nbibtexurl: '" + "http://michaelneunteufel.github.io/files/bibtex/" + bib_id + ".bib" + "'"

    if category == "manuscripts" and "arxivurl" in b.keys():
        if len(str(b["arxivurl"])) > 5:
            md += "\narxivurl: '" + b["arxivurl"] + "'"
    md += "\n---\n"
    if abstract:
        abstract = abstract.replace("\\$", "$$").replace("{\\textbackslash}", "\\").replace("\\_", "_").replace("\\{", "{").replace("\\}", "}").replace("{\\textasciicircum}", "^").replace(" .", ".")
        abstract = html_escape(abstract)
        abstract = abstract.replace("{\\&apos;e}","&eacute;").replace("{\\&quot;o}", "&ouml;").replace("\\&quot;o", "&ouml;").replace("{\\&quot;a}", "&auml;").replace("{\\&quot;u}", "&uuml;").replace("\\&amp;", "&amp;").replace("\\v{s}","&scaron;").replace("{\\ss}","&szlig;")
        md += abstract

    if "code" in b.keys():
        md += "\n\n[Supplementary code]("+ b["code"] + ")"
    # md += "\ncitation: '" + html_escape(citation) + "'"

    # md += "\n---"

    
    # ## Markdown description for individual page
    # if note:
    #     md += "\n" + html_escape(b["note"]) + "\n"

    #if url:
    #    md += "\n[Access paper here](" + b["url"] + "){:target=\"_blank\"}\n" 
    # else:
    #     md += "\nUse [Google Scholar](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"} for full citation"
    #print(md)
    with open("../_publications/" + md_filename, 'w', encoding="utf-8") as f:
        f.write(md)
    # if i > 30:
    #     break