import os
import datetime
os.makedirs('./docs', exist_ok=True)
now = datetime.datetime.now()
with open('docs/index.html', mode='w') as f:
    f.write(now.strftime('%Y-%m-%d %H:%M:%S'))
