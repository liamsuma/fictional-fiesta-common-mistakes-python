# When using Selenium for web crawling, path not found issue often comes on top whether you are using Java or Python for programming 

# Solution 1: remember to give a path of your Chromedriver

driver = webdriver.Chrome(executable_path='/path/to/where/you/saved/your/driver'

# Solution 2: CL terminal command if you're facing Chromedriver cannot be opened because the developer cannot be verified issue
# Step 1: open terminal and navigate to path where your chromedriver file is located
# Step 2: execute xattr -d com.apple.quarantine chromedriver 
# Step 3: re-run your program and it should be fine 
