'''
Pseudocode:
FUNCTION ProductParserSystem
    // Define sample product listings
    CREATE LIST listings with various product listing formats
    
    // Define function to parse the listings
    FUNCTION parse_listings(product_listings)
        INITIALIZE empty results list
        
        FOR EACH listing IN product_listings
            INITIALIZE product_info dictionary with raw_listing
            
            // Extract price information
            FIND index of "$" symbol in listing
            IF "$" symbol is found THEN
                EXTRACT text after "$" symbol
                FILTER out non-numeric characters (except decimal points)
                IF valid price string exists THEN
                    CONVERT to float and store in product_info["price"]
                ELSE
                    SET product_info["price"] to None
                END IF
            ELSE
                SET product_info["price"] to None
            END IF
            
            // Extract brand and name based on different formats
            // Format 1: Using hyphen separator
            IF " - " exists in listing THEN
                SPLIT listing by " - "
                EXTRACT name_part as first segment
                
                IF "(" exists in name_part THEN
                    SPLIT by parenthesis
                ELSE IF "," exists in name_part THEN
                    SPLIT by comma
                END IF
                
                EXTRACT first word as brand
                EXTRACT remaining words as name
            
            // Format 2: Using colon separator
            ELSE IF ":" exists in listing THEN
                SIMILAR processing to extract brand and name
            
            // Format 3: Using pipe separator
            ELSE IF "|" exists in listing THEN
                SIMILAR processing to extract brand and name
            
            // Format 4: Using @ symbol
            ELSE IF "@" exists in listing THEN
                SIMILAR processing to extract brand and name
            
            // Default case
            ELSE
                FIND earliest marker ("$", ",", "(", "-")
                EXTRACT text before marker
                EXTRACT first word as brand
                EXTRACT remaining words as name
            END IF
            
            // Extract additional information (e.g., storage)
            IF "GB" exists in listing THEN
                EXTRACT digits before "GB"
                STORE as product_info["storage"]
            END IF
            
            APPEND product_info to results list
        END FOR
        
        RETURN results list
    END FUNCTION
    
    // Define function to display results
    FUNCTION print_results(parsed_results)
        DISPLAY header
        
        FOR EACH product IN parsed_results
            DISPLAY product number
            DISPLAY raw listing
            DISPLAY brand
            DISPLAY name
            
            IF storage information exists THEN
                DISPLAY storage
            END IF
            
            IF price exists THEN
                DISPLAY formatted price
            ELSE
                DISPLAY "Price not found"
            END IF
            
            DISPLAY newline
        END FOR
    END FUNCTION
    
    // Main execution
    SET parsed_products to result of parse_listings(listings)
    CALL print_results(parsed_products)
END FUNCTION

CALL ProductParserSystem

'''

listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6 Pro - 512GB @ $890",
    "OnePlus 10 Pro: 5G, 256GB, $899",
    "Sony WH-1000XM4 Wireless Headphones | $348",
    "Bose QuietComfort 45 Headphones - $329",
    "Dell XPS 15 Laptop - i7, 16GB RAM, 512GB SSD for $1499"
]

def parse_listings(product_listings):
    results = []
    
    for listing in product_listings:
        product_info = {"raw_listing": listing}
        
        price_index = listing.find("$")
        if price_index != -1:
            price_text = listing[price_index + 1:]
            
            price_str = ""
            for char in price_text:
                if char.isdigit() or char == '.':
                    price_str += char
                else:
                    
                    if price_str:  
                        break
            
            if price_str:
                product_info["price"] = float(price_str)
            else:
                product_info["price"] = None
        else:
            product_info["price"] = None
        
        if " - " in listing:
            parts = listing.split(" - ")
            name_part = parts[0]
            
            if "(" in name_part: 
                brand_model = name_part.split("(")[0].strip()
            elif "," in name_part:  
                brand_model = name_part.split(",")[0].strip()
            else:
                brand_model = name_part.strip()
            
            words = brand_model.split()
            product_info["brand"] = words[0]
            product_info["name"] = " ".join(words[1:]) if len(words) > 1 else brand_model
            
        elif ":" in listing:
            parts = listing.split(":")
            brand_model = parts[0].strip()
            
            words = brand_model.split()
            product_info["brand"] = words[0]
            product_info["name"] = " ".join(words[1:]) if len(words) > 1 else brand_model
            
        elif "|" in listing:
            parts = listing.split("|")
            brand_model = parts[0].strip()
            
            words = brand_model.split()
            product_info["brand"] = words[0]
            product_info["name"] = " ".join(words[1:]) if len(words) > 1 else brand_model
            
        elif "@" in listing:
            parts = listing.split("@")
            brand_model = parts[0].strip()
            
            words = brand_model.split()
            product_info["brand"] = words[0]
            product_info["name"] = " ".join(words[1:]) if len(words) > 1 else brand_model
            
        else:
            cutoff_indices = []
            for marker in ["$", ",", "(", "-"]:
                idx = listing.find(marker)
                if idx != -1:
                    cutoff_indices.append(idx)
            
            if cutoff_indices:
                cutoff = min(cutoff_indices)
                brand_model = listing[:cutoff].strip()
            else:
                brand_model = listing.strip()
            
            words = brand_model.split()
            product_info["brand"] = words[0]
            product_info["name"] = " ".join(words[1:]) if len(words) > 1 else brand_model
        
        if "GB" in listing:
            gb_index = listing.find("GB")
            for i in range(gb_index-1, max(0, gb_index-5), -1):
                if not listing[i].isdigit() and listing[i] != ' ':
                    storage_start = i + 1
                    storage_size = listing[storage_start:gb_index+2]
                    product_info["storage"] = storage_size
                    break
            else:
                digits = ""
                for i in range(gb_index-1, max(0, gb_index-5), -1):
                    if listing[i].isdigit():
                        digits = listing[i] + digits
                    elif digits:  
                        break
                if digits:
                    product_info["storage"] = f"{digits}GB"
        
        results.append(product_info)
    
    return results

def print_results(parsed_results):
    print("\n===== PARSED PRODUCT INFORMATION =====\n")
    
    for i, product in enumerate(parsed_results, 1):
        print(f"Product {i}:")
        print(f"  Raw listing: {product['raw_listing']}")
        print(f"  Brand: {product['brand']}")
        print(f"  Name: {product['name']}")
        
        if "storage" in product:
            print(f"  Storage: {product['storage']}")
            
        if product['price'] is not None:
            print(f"  Price: ${product['price']:.2f}")
        else:
            print(f"  Price: Not found")
        print()

if __name__ == "__main__":
    parsed_products = parse_listings(listings)
    print_results(parsed_products)