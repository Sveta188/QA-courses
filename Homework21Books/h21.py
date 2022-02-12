import xml.etree.cElementTree as ET

tree = ET.parse('home_task_xml.xml')
root = tree.getroot()
for i in root:
    print(f'This book called "{i[1].text}" has "id"', i.attrib['id'])

print(f'We have {len(root)} books')

sort_price = sorted(root, key=lambda i: float(i[3].text))
for i in sort_price:
    print(f'This book called "{i[1].text}" costs {i[3].text} dollars')

sort_date = sorted(root, key=lambda i: i[4].text)
for i in sort_date:
    print(f'This book called "{i[1].text}" published in {i[4].text} year')

sort_year = sorted(root, key=lambda i: i[4].text)
for i in sort_year:
    if '2000' in i[4].text:
        print(f'This book called "{i[1].text}" published in {i[4].text} year')

sort_genre = sorted(root, key=lambda i: i[2].text)
for i in sort_genre:
    if 'Computer' in i[2].text:
        print(f'This book called "{i[1].text}" is in {i[2].text} genre. Author is {i[0].text}. '
              f'This book was published in {i[4].text} year')
