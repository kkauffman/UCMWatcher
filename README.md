UCMWatcher
========== 
This program polls UC Merced's server to check if any class in a specified department has either opened or closed. If any course(s) have opened or closed the script send an email list what has changed.

# Usage
To use first you need to set the environmental variables 'UCMWUser', 'UCMWPass', and 'UCMWDept'

```bash
export UCMWUser='Your email username'
export UCMWPass='You email password'
export UCMWDept='Department code'
```

If your email provider isn't gmail change the SMTP_SERVER variable in the script to your email provider's smtp server.
Then set up the script to be run as often as you want using any job scheduler such as cron.

# Department codes
* ALL -> All Subjects
* ANTH -> Anthropology
* ARTS -> Art
* BEST -> Bio Engin Small Scale Tech
* BIOE -> Bioengineering
* BIO -> Biological Sciences
* CHEM -> Chemistry
* CCST -> Chicano Chicana Studies
* CHN -> Chinese
* COGS -> Cognitive Science
* CSE -> Computer Science & Engineering
* CORE -> Core
* ESS -> Earth Systems Science
* ECON -> Economics
* EDUC -> Education
* EECS -> Elect. Engr. & Comp. Sci.
* ENGR -> Engineering
* ENG -> English
* ENVE -> Environmental Engineering
* ES -> Environmental Systems (GR)
* FRE -> French
* GEOG -> Geography
* GASP -> Global Arts Studies Program
* HIST -> History
* HBIO -> Human Biology
* IH -> Interdisciplinary Humanities
* JPN -> Japanese
* MGMT -> Management
* MSE -> Materials Science & Engr
* MATH -> Mathematics
* ME -> Mechanical Engineering
* NSED -> Natural Sciences Education
* PHIL -> Philosophy
* PHYS -> Physics
* POLI -> Political Science
* PSY -> Psychology
* PH -> Public Health
* PUBP -> Public Policy
* QSB -> Quantitative & Systems Biology
* SCS -> Social Sciences
* SOC -> Sociology
* SPAN -> Spanish
* USTU -> Undergraduate Studies
* WCH -> World Cultures & History
* WH -> World Heritage
* WRI -> Writing

