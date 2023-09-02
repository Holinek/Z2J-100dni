# Zadanie na dzisiaj:
# Proste zadanko. Wylicz, ile dni już żyjesz :)))

from datetime import datetime

date1 = datetime.now()
date2 = datetime(1994, 2, 21)
diff = date1 - date2

print(diff.days)
