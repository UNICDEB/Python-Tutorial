# To delete a file, you must import the OS module, and run its os.remove() function.

# Remove the file "demofile.txt":
# import os
# os.remove("demofile.txt")

# Check if file exists, then delete it:

import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")
  
  
  
# # Remove the folder "myfolder":
# import os
# os.rmdir("myfolder")