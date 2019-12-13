import os 
import sys

# Function to rename multiple files 
def main(): 
    i = 0

    for filename in os.listdir("Candida_albicans"): 
        print(filename)
        dst ="Candida_albicans" + str(i) + ".png"
        src ="Candida_albicans/" + filename 
        dst = "Candida_albicans/" + dst 
        os.rename(src, dst) 
        i += 1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
