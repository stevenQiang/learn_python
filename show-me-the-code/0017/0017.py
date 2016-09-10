# -*- coding: utf-8 -*-

from xml.dom.minidom import Document


def xml_list():
    xml_body = Document()
    root_child = xml_body.createElement('root')
    xml_body.appendChild(root_child)
    student_child = xml_body.createElement('students')
    book_author_value = xml_body.createTextNode("{1:2,3:3}")
    student_child.appendChild(book_author_value)
    root_child.appendChild(student_child)
    f = open("students.xml", "w")
    f.write(xml_body.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
    f.close()


if __name__ == "__main__":
    xml_list()
