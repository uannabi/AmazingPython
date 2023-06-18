
from datetime import datetime

now = datetime.now()

print(f"{now: %D-%M-%Y}")
print(f"{now: %DD-%MM-%YYYY}")
print(f"{now: %D-%M-%Y  %H-%M-%S}")
