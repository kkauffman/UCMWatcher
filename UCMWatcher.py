import os
import re
import smtplib
import datetime
import requests
from bs4 import BeautifulSoup
import cPickle as pickle

URL = 'https://pbanssb.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule'
PAYLOAD = {'openclasses':'N', 'subjcode':'BIO', 'validterm':'201510'}

username = os.environ.get('UCMWUser')
password = os.environ.get('UCMWPass')

SMTP_SERVER = "smtp.gmail.com"

def send_email(user, password, subject, msg):
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (user, ", ".join(user), subject, msg)
            try:
	        server = smtplib.SMTP(SMTP_SERVER, 587) 
                server.ehlo()
                server.starttls()
                server.login(user, password)
                server.sendmail(user, user, message)
                server.close()
		return True
            except:
                pass
	    return False

if not username or not password:
    print 'username or password environmental variable not set'
    print 'set "UCMWUser" and "UCMWPass" and rerun the program'
    quit()

r = requests.post(URL, data=PAYLOAD, headers={'host':'pbanssb.ucmerced.edu'})

if r.status_code != requests.codes.ok:
    quit('Error: Could not load class catalog (' + str(r.status_code) + ')')

parsed = BeautifulSoup(r.text)

courseRE = re.compile(r'BIO-(\d{,3})-(\w{,3})')

courses = {}

msgs = []

try:
    courses = pickle.load(open('courses', 'rb'))
except IOError:
    pass

for row in parsed.find_all(bgcolor=re.compile('#(FFFFFF|DDDDDD)')):
    
    entries = row.find_all('td')

    if len(entries) == 13:
        course = courseRE.match(entries[1].text)
        if course:
            classNum = course.group(1)
            sectionNum = course.group(2)

            if classNum in courses:                                
                if sectionNum in courses[classNum]:
                    is_open = entries[-1].text.isdigit()
                    
                    if is_open != courses[classNum][sectionNum]:
                        msg = 'Class Bio-' + classNum + '-' + sectionNum + ' is now '
			if is_open:
			    msg += 'open'
			else:
			    msg += 'closed'
 
                        msgs.append(msg)

			courses[classNum][sectionNum] = is_open
                else:
                    courses[classNum][sectionNum] = not(entries[-1].text.isdigit())
            else:
                courses[classNum] = {sectionNum : not(entries[-1].text.isdigit())}

pickle.dump(courses, open('courses', 'wb'))            
            

now = datetime.datetime.now()

if msgs:
    if not send_email(username, password, 'Courses Changed', '\n'.join(msgs)):
        print 'Failed to send email!', now.isoformat()
	for msg in msgs:
	    print '\t', msg
else:
    print 'Nothing to report!', now.isoformat()

