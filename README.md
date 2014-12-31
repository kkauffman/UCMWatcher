UCMWatcher
========== 
This program polls UC Merced's server to check if any class in a specified department has either opened or closed. If any course(s) have opened or closed the script send an email list what has changed.

# Usage
To use first you need to set the environmental variables 'UCMWUser' and 'UCMWPass'

```bash
export UCMWUser='Your email username'
export UCMWPass='You email password'
```

If your email provider isn't gmail change the SMTP_SERVER variable in the script to your email provider's smtp server.
Then set up the script to be run as often as you want using any job scheduler such as cron.
