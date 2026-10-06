from pyscript import document, display

def create_order(e):
    # for deleting the previous receipt
    document.getElementById("show").innerHTML = ""
    
    # Retrieve input elements from HTML
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    
    # Calculate item totals
    val1 = float(prod1.value) * prod1.checked
    val2 = float(prod2.value) * prod2.checked
    val3 = float(prod3.value) * prod3.checked
    
    # Calculate Subtotalllll
    subtotal = val1 + val2 + val3
    vat = subtotal * 0.12
    total_amount = subtotal + vat
    
    # Generate and display the receipt breakdown
    display("=== OFFICIAL RECEIPT ===", target="show")
    display("Subtotal: ₱" + str(subtotal), target="show")
    display("VAT (12%): ₱" + str(vat), target="show")
    display("Total Amount: ₱" + str(total_amount), target="show")