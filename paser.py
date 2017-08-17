# -*- coding: utf-8 -*- 

import xml.dom.minidom

if __name__ == "__main__":

    dom = xml.dom.minidom.parse("sample.xml")

    print dom.documentElement.tagName
    for node in dom.documentElement.childNodes:
        if node.nodeType == node.ELEMENT_NODE:
            print "  " + node.tagName

            for node2 in node.childNodes:
                if node2.nodeType == node2.ELEMENT_NODE:
                    print "    " + node2.tagName

                    for node3 in node2.childNodes:
                        if node3.nodeType == node3.TEXT_NODE:
                            print "      " + node3.data

    print "-------------------------------------"
    
    for url in dom.getElementsByTagName("url"):
        print url.firstChild.data