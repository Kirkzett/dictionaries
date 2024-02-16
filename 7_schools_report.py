"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open('school_data.json')

schools = json.load(infile)

print(type(schools))

conference_schools = [372,108,107,130]

for detials in schools:
    if detials["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if detials["Graduation rate  women (DRVGR2020)"] > 75:
            print(f"University: {detials['instnm']}")
            print(f'Graduation rate for women: {detials["Graduation rate  women (DRVGR2020)"]}%\n')

for detials in schools:
    if detials["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if detials["Total price for in-state students living on campus 2020-21 (DRVIC2020)"] > 50000:
            print(f"University: {detials['instnm']}")
            print(f'Universities that have a total price for in-state students living off campus over $50,000: {detials["Total price for in-state students living on campus 2020-21 (DRVIC2020)"]}%\n')
