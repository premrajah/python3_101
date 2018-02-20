#
# Parsing XML files
#
import xml.dom.minidom

def main():
    # use the parse() function
    doc = xml.dom.minidom.parse("sample.xml")

    ## print document node name and name of first child
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    ## list of xml tags
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))

    
    ## create new xml tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "JQuery")
    doc.firstChild.appendChild(newSkill)

    print("---")

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()