import platform
import system

dist = platform.dist()

print(dist)

# If statements.
if "debian" in dist:
  system(apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get full-upgrade -y)
  print("Has")
