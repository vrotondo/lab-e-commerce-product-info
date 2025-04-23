# lab-e-commerce-product-info
Foundations I - Lab: E-commerce Product Information

Lab: E-commerce Product Information
Imagine you're a software engineer working for an e-commerce company. Your task is to write a Python script that scrapes product information (name, price, brand) from online listings. These listings often come in various formats, and you need to extract the relevant details using string manipulation techniques.

Tools and Resources
The tools or resources needed to complete this lab include: 

Strings content, technical lesson, and lab from this topic.
Python IDE, Visual Studio Code.
Instructions
Step 1: Settings
Create a new script file (e.g., product_parser.py)
Import the necessary libraries (if needed for scraping).
Step 2: Sample Listings
Create a list of sample product listings with different formats (e.g., brand and name combined, price at the end, varying delimiters).

listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6 Pro - 512GB @ $890"
]
Step 3: Extracting Information
Write a loop to iterate through each listing in the listings list. Inside the loop, create a new variable to store the extracted product information (e.g., a dictionary).

Name: Use string slicing or splitting (based on format) to isolate the product name.
name = listing.split()[0]  # Extract first word(s)
Price: Find the position of the price symbol ($) using find(). Extract the price substring using slicing or splitting.
price_index = listing.find("$")
price_str = listing[price_index+1:]  # Extract price after symbol
price = float(price_str.split()[0])  # Extract first word (assuming price)
Brand (Optional): If the brand is not readily available, you might need to use external APIs or manual configuration based on specific websites.
Step 4: Handling Variation (Conditional Statements)
Create a series of if statements to handle different listing formats.

For example:

if "-" in listing:
    # Extract name and price based on hyphen delimiter
elif "," in listing:
    # Extract name and price based on comma delimiter
else:
    # Handle other formats or potential errors (optional)
Step 5: Storing and Printing Results
Append the extracted information dictionary to a results list.
After the loop, print the entire results list, containing dictionaries for each product.
Submission
Make sure you have saved the file asproduct_parser.py
Click the Load Lab: E-commerce Product Information button below to launch this assignment in CodeGrade.
Upload your Python file to the click here or add files to upload field. 
For additional information on submitting assignments in CodeGrade: Getting Started in CanvasLinks to an external site..
Grading Criteria
Use the rubric below as a guide for how this lab is graded.
You submission will be automatically scored in CodeGrade.
You can review your submission in CodeGrade and see your final score in your Canvas grades.
