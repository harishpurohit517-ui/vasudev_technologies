from flask import Flask, render_template_string, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# ============================================================
# VASUDEV TECHNOLOGIES - PRODUCTS
# ============================================================

products = [
    {
        "id": 1,
        "name": "1.8 GB RAM",
        "price": 3000,
        "category": "RAM",
        "description": "1.8 GB laptop RAM",
        "image": "ram.jfif"
    },
    {
        "id": 2,
        "name": "Dell Keyboard + Mouse Combo",
        "price": 1000,
        "category": "Keyboard & Mouse",
        "description": "Dell keyboard and mouse combo",
        "image": "dell_combo.jfif"
    },
    {
        "id": 3,
        "name": "o",
        "price": 700,
        "category": "Battery",
        "description": "HS04 laptop battery",
        "image": "hs04_battery.jfif"
    },
    {
        "id": 4,
        "name": "256 GB SSD",
        "price": 2000,
        "category": "SSD",
        "description": "256 GB laptop SSD",
        "image": "ssd_256gb.jfif"
    },
    {
        "id": 5,
        "name": "Laptop Screen",
        "price": 5000,
        "category": "Screen",
        "description": "Laptop replacement screen",
        "image": "laptop_screen.jfif"
    },
    {
        "id": 6,
        "name": "Laptop Panel",
        "price": 700,
        "category": "Panel",
        "description": "Laptop replacement panel",
        "image": "laptop_panel.jfif"
    },
    {
        "id": 7,
        "name": "Laptop Touchpad",
        "price": 700,
        "category": "Touchpad",
        "description": "Laptop replacement touchpad",
        "image": "laptop_touchpad.jfif"
    }
]


# ============================================================
# PRODUCT IMAGE ROUTE
# ============================================================

@app.route("/product-image/<filename>")
def product_image(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(folder, filename)


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():
    return render_template_string(HTML, products=products)


# ============================================================
# ENQUIRY
# ============================================================

@app.route("/enquiry", methods=["POST"])
def enquiry():

    data = request.get_json()

    name = data.get("name", "").strip()
    phone = data.get("phone", "").strip()
    cart = data.get("cart", [])

    if not name:
        return jsonify({
            "success": False,
            "message": "Please enter your name."
        })

    if not phone:
        return jsonify({
            "success": False,
            "message": "Please enter your phone number."
        })

    if not cart:
        return jsonify({
            "success": False,
            "message": "Your cart is empty."
        })

    print("\n" + "=" * 60)
    print("NEW ENQUIRY - VASUDEV TECHNOLOGIES")
    print("=" * 60)

    print("Customer Name:", name)
    print("Phone Number:", phone)
    print("\nProducts:")

    total = 0

    for item in cart:

        product_id = int(item["id"])
        quantity = int(item["quantity"])

        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )

        if product:

            subtotal = product["price"] * quantity
            total += subtotal

            print(
                f"{product['name']} x {quantity} "
                f"= ₹{subtotal:,}"
            )

    print("\nTOTAL: ₹" + format(total, ","))

    print("=" * 60)

    return jsonify({
        "success": True,
        "message": "Your enquiry has been submitted successfully!"
    })


# ============================================================
# WEBSITE HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>VASUDEV TECHNOLOGIES</title>


<style>

/* ============================================================
   BASIC
   ============================================================ */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f4f6f8;
    color: #111;
}


/* ============================================================
   HEADER
   ============================================================ */

header {

    background: #101820;

    color: white;

    padding: 18px 6%;

    display: flex;

    align-items: center;

    justify-content: space-between;

    position: sticky;

    top: 0;

    z-index: 1000;
}

.logo {

    font-size: 25px;

    font-weight: bold;
}

nav {

    display: flex;

    align-items: center;

    gap: 20px;
}

nav a {

    color: white;

    text-decoration: none;

    font-weight: bold;
}

.cart-btn {

    border: none;

    background: #00c853;

    color: white;

    padding: 11px 17px;

    border-radius: 9px;

    cursor: pointer;

    font-size: 15px;

    font-weight: bold;
}

.cart-btn:hover {

    background: #00a844;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    background:
    linear-gradient(
        135deg,
        #101820,
        #273746
    );

    color: white;

    text-align: center;

    padding: 75px 20px;
}

.hero h1 {

    font-size: 48px;

    margin-bottom: 15px;
}

.hero p {

    font-size: 18px;

    margin-bottom: 30px;
}

.search {

    width: min(600px, 90%);

    padding: 16px 20px;

    border: none;

    border-radius: 30px;

    font-size: 17px;

    outline: none;
}


/* ============================================================
   SECTIONS
   ============================================================ */

.section {

    padding: 55px 6%;
}

.section-title {

    text-align: center;

    font-size: 32px;

    margin-bottom: 35px;
}


/* ============================================================
   PRODUCTS
   ============================================================ */

.products {

    display: grid;

    grid-template-columns:
    repeat(
        auto-fit,
        minmax(230px, 1fr)
    );

    gap: 25px;
}

.product {

    background: white;

    border-radius: 15px;

    overflow: hidden;

    box-shadow:
    0 5px 20px
    rgba(0,0,0,0.08);

    transition: 0.2s;
}

.product:hover {

    transform: translateY(-5px);
}

.product img {

    width: 100%;

    height: 220px;

    object-fit: contain;

    padding: 15px;

    background: #fafafa;
}

.product-info {

    padding: 20px;
}

.product-info h3 {

    margin-bottom: 8px;

    font-size: 20px;
}

.category {

    display: inline-block;

    background: #e8edf1;

    padding: 5px 9px;

    border-radius: 6px;

    font-size: 12px;

    margin-bottom: 10px;
}

.description {

    color: #666;

    margin-bottom: 15px;
}

.price {

    font-size: 23px;

    font-weight: bold;

    margin-bottom: 15px;
}

.add-btn {

    width: 100%;

    border: none;

    background: #101820;

    color: white;

    padding: 13px;

    border-radius: 9px;

    cursor: pointer;

    font-size: 15px;

    font-weight: bold;
}

.add-btn:hover {

    background: #00a844;
}


/* ============================================================
   CART PANEL
   ============================================================ */

.overlay {

    display: none;

    position: fixed;

    inset: 0;

    background:
    rgba(0,0,0,0.65);

    z-index: 2000;
}

.cart-panel {

    position: fixed;

    right: 0;

    top: 0;

    width: min(450px, 95%);

    height: 100vh;

    background: white;

    z-index: 3000;

    padding: 25px;

    overflow-y: auto;

    transform: translateX(100%);

    transition: 0.3s;
}

.cart-panel.open {

    transform: translateX(0);
}

.cart-header {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 25px;
}

.close-btn {

    border: none;

    background: #eee;

    width: 40px;

    height: 40px;

    border-radius: 50%;

    cursor: pointer;

    font-size: 20px;
}


/* ============================================================
   CART ITEM
   ============================================================ */

.cart-item {

    display: flex;

    gap: 12px;

    padding: 15px 0;

    border-bottom: 1px solid #ddd;
}

.cart-item img {

    width: 70px;

    height: 70px;

    object-fit: contain;

    background: #f5f5f5;

    border-radius: 8px;
}

.cart-info {

    flex: 1;
}

.cart-info h4 {

    margin-bottom: 5px;
}

.quantity {

    display: flex;

    align-items: center;

    gap: 8px;

    margin-top: 8px;
}

.quantity button {

    width: 28px;

    height: 28px;

    border: none;

    background: #eee;

    border-radius: 5px;

    cursor: pointer;
}

.remove {

    color: #d50000;

    border: none;

    background: none;

    cursor: pointer;

    margin-top: 7px;
}


/* ============================================================
   CART TOTAL
   ============================================================ */

.cart-total {

    font-size: 24px;

    font-weight: bold;

    margin: 25px 0;
}

.enquire-btn {

    width: 100%;

    border: none;

    background: #00a844;

    color: white;

    padding: 15px;

    border-radius: 10px;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;
}

.enquire-btn:hover {

    background: #008c38;
}


/* ============================================================
   ENQUIRY MODAL
   ============================================================ */

.modal {

    display: none;

    position: fixed;

    inset: 0;

    background:
    rgba(0,0,0,0.7);

    z-index: 4000;

    align-items: center;

    justify-content: center;

    padding: 20px;
}

.modal-box {

    width: min(450px, 100%);

    background: white;

    border-radius: 15px;

    padding: 30px;
}

.modal-box h2 {

    margin-bottom: 10px;
}

.modal-box p {

    color: #666;

    margin-bottom: 20px;
}

.form-group {

    margin-bottom: 15px;
}

.form-group label {

    display: block;

    font-weight: bold;

    margin-bottom: 6px;
}

.form-group input {

    width: 100%;

    padding: 13px;

    border: 1px solid #ccc;

    border-radius: 8px;

    font-size: 16px;
}

.submit-btn {

    width: 100%;

    border: none;

    background: #101820;

    color: white;

    padding: 14px;

    border-radius: 8px;

    cursor: pointer;

    font-size: 16px;

    font-weight: bold;
}

.cancel-btn {

    width: 100%;

    border: none;

    background: #eee;

    padding: 12px;

    border-radius: 8px;

    cursor: pointer;

    margin-top: 10px;
}

.message {

    text-align: center;

    margin-top: 15px;

    font-weight: bold;
}


/* ============================================================
   CONTACT
   ============================================================ */

.contact {

    background: #101820;

    color: white;

    text-align: center;

    padding: 55px 20px;
}

.contact h2 {

    margin-bottom: 15px;
}

.phone {

    display: inline-block;

    margin-top: 15px;

    color: white;

    font-size: 22px;

    text-decoration: none;

    font-weight: bold;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media(max-width:700px) {

    header {

        padding: 15px;
    }

    .logo {

        font-size: 19px;
    }

    nav a {

        display: none;
    }

    .hero h1 {

        font-size: 32px;
    }

    .section {

        padding: 35px 15px;
    }
}

</style>

</head>


<body>


<!-- =========================================================
     HEADER
     ========================================================= -->

<header>

<div class="logo">
VASUDEV TECHNOLOGIES
</div>

<nav>

<a href="#products">
Products
</a>

<a href="#contact">
Contact
</a>

<button
class="cart-btn"
onclick="openCart()">

🛒 Cart
<span id="cartCount">0</span>

</button>

</nav>

</header>


<!-- =========================================================
     HERO
     ========================================================= -->

<section class="hero">

<h1>
VASUDEV TECHNOLOGIES
</h1>

<p>
Laptop Parts & Accessories
</p>

<input
class="search"
id="search"
type="text"
placeholder="Search products..."
onkeyup="searchProducts()">

</section>


<!-- =========================================================
     PRODUCTS
     ========================================================= -->

<section
class="section"
id="products">

<h2 class="section-title">
Our Products
</h2>

<div class="products"
id="productContainer">


{% for product in products %}

<div
class="product"
data-name="{{ product.name }}"
data-category="{{ product.category }}">

<img
src="{{ url_for('product_image', filename=product.image) }}"
alt="{{ product.name }}">

<div class="product-info">

<span class="category">
{{ product.category }}
</span>

<h3>
{{ product.name }}
</h3>

<p class="description">
{{ product.description }}
</p>

<div class="price">
₹{{ "{:,}".format(product.price) }}
</div>

<button
class="add-btn"
onclick="addToCart({{ product.id }})">

🛒 Add to Cart

</button>

</div>

</div>

{% endfor %}


</div>

</section>


<!-- =========================================================
     CONTACT
     ========================================================= -->

<section
class="contact"
id="contact">

<h2>
Contact VASUDEV TECHNOLOGIES
</h2>

<p>
For laptop parts and accessories enquiries
</p>

<a
class="phone"
href="tel:9916648774">

📞 9916648774

</a>

</section>


<!-- =========================================================
     CART OVERLAY
     ========================================================= -->

<div
class="overlay"
id="overlay"
onclick="closeCart()">
</div>


<!-- =========================================================
     CART
     ========================================================= -->

<div
class="cart-panel"
id="cartPanel">

<div class="cart-header">

<h2>
🛒 Your Cart
</h2>

<button
class="close-btn"
onclick="closeCart()">

✕

</button>

</div>


<div id="cartItems">
</div>


<div
class="cart-total"
id="cartTotal">

Total: ₹0

</div>


<button
class="enquire-btn"
onclick="openEnquiry()">

📩 Enquire About These Products

</button>

</div>


<!-- =========================================================
     ENQUIRY MODAL
     ========================================================= -->

<div
class="modal"
id="enquiryModal">

<div class="modal-box">

<h2>
📩 Product Enquiry
</h2>

<p>
Enter your details and we will contact you.
</p>


<div class="form-group">

<label>
Name
</label>

<input
id="customerName"
type="text"
placeholder="Enter your name">

</div>


<div class="form-group">

<label>
Phone Number
</label>

<input
id="customerPhone"
type="tel"
placeholder="Enter your phone number">

</div>


<button
class="submit-btn"
onclick="submitEnquiry()">

Submit Enquiry

</button>


<button
class="cancel-btn"
onclick="closeEnquiry()">

Cancel

</button>


<div
class="message"
id="message">
</div>

</div>

</div>


<!-- =========================================================
     JAVASCRIPT
     ========================================================= -->

<script>


// ============================================================
// PRODUCTS
// ============================================================

const products = {{ products | tojson }};


// ============================================================
// CART
// ============================================================

let cart = [];


// ============================================================
// ADD TO CART
// ============================================================

function addToCart(productId) {

    let existing = cart.find(
        item => item.id === productId
    );

    if (existing) {

        existing.quantity++;

    } else {

        cart.push({

            id: productId,

            quantity: 1

        });

    }

    updateCart();

    openCart();
}


// ============================================================
// UPDATE CART
// ============================================================

function updateCart() {

    const cartItems =
        document.getElementById("cartItems");

    const cartCount =
        document.getElementById("cartCount");

    const cartTotal =
        document.getElementById("cartTotal");


    cartItems.innerHTML = "";


    let total = 0;

    let itemCount = 0;


    if (cart.length === 0) {

        cartItems.innerHTML = `
            <div class="empty-cart">
                🛒 Your cart is empty.
                <br><br>
                Add some products!
            </div>
        `;

        cartTotal.innerText = "Total: ₹0";

        cartCount.innerText = "0";

        return;
    }


    cart.forEach(item => {

        const product = products.find(
            p => p.id === item.id
        );

        if (!product) return;


        const subtotal =
            product.price * item.quantity;


        total += subtotal;

        itemCount += item.quantity;


        cartItems.innerHTML += `

        <div class="cart-item">

            <img
            src="/product-image/${product.image}">

            <div class="cart-info">

                <h4>
                    ${product.name}
                </h4>

                <div>
                    ₹${product.price.toLocaleString("en-IN")}
                </div>

                <div class="quantity">

                    <button
                    onclick="changeQuantity(
                        ${product.id},
                        -1
                    )">

                    −

                    </button>

                    <strong>
                    ${item.quantity}
                    </strong>

                    <button
                    onclick="changeQuantity(
                        ${product.id},
                        1
                    )">

                    +

                    </button>

                </div>

                <button
                class="remove"
                onclick="removeFromCart(
                    ${product.id}
                )">

                Remove

                </button>

            </div>

        </div>

        `;

    });


    cartTotal.innerText =
        "Total: ₹" +
        total.toLocaleString("en-IN");


    cartCount.innerText =
        itemCount;
}


// ============================================================
// CHANGE QUANTITY
// ============================================================

function changeQuantity(productId, amount) {

    const item = cart.find(
        item => item.id === productId
    );

    if (!item) return;


    item.quantity += amount;


    if (item.quantity <= 0) {

        cart = cart.filter(
            item => item.id !== productId
        );

    }


    updateCart();
}


// ============================================================
// REMOVE
// ============================================================

function removeFromCart(productId) {

    cart = cart.filter(
        item => item.id !== productId
    );

    updateCart();
}


// ============================================================
// OPEN CART
// ============================================================

function openCart() {

    document
        .getElementById("cartPanel")
        .classList.add("open");

    document
        .getElementById("overlay")
        .style.display = "block";
}


// ============================================================
// CLOSE CART
// ============================================================

function closeCart() {

    document
        .getElementById("cartPanel")
        .classList.remove("open");

    document
        .getElementById("overlay")
        .style.display = "none";
}


// ============================================================
// OPEN ENQUIRY
// ============================================================

function openEnquiry() {

    if (cart.length === 0) {

        alert(
            "Please add at least one product to your cart."
        );

        return;
    }


    document
        .getElementById("enquiryModal")
        .style.display = "flex";
}


// ============================================================
// CLOSE ENQUIRY
// ============================================================

function closeEnquiry() {

    document
        .getElementById("enquiryModal")
        .style.display = "none";

    document
        .getElementById("message")
        .innerText = "";
}


// ============================================================
// SUBMIT ENQUIRY
// ============================================================

async function submitEnquiry() {

    const name =
        document
        .getElementById("customerName")
        .value
        .trim();


    const phone =
        document
        .getElementById("customerPhone")
        .value
        .trim();


    const message =
        document.getElementById("message");


    if (!name) {

        message.innerText =
            "Please enter your name.";

        return;
    }


    if (!phone) {

        message.innerText =
            "Please enter your phone number.";

        return;
    }


    message.innerText =
        "Sending enquiry...";


    try {

        const response =
            await fetch(
                "/enquiry",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({

                        name: name,

                        phone: phone,

                        cart: cart

                    })

                }
            );


        const result =
            await response.json();


        if (result.success) {

            message.innerText =
                "✅ " + result.message;


            cart = [];

            updateCart();


            document
                .getElementById("customerName")
                .value = "";


            document
                .getElementById("customerPhone")
                .value = "";


            setTimeout(() => {

                closeEnquiry();

                closeCart();

            }, 2000);

        } else {

            message.innerText =
                "❌ " + result.message;

        }

    } catch (error) {

        message.innerText =
            "❌ Could not submit enquiry.";

        console.error(error);

    }

}


// ============================================================
// SEARCH
// ============================================================

function searchProducts() {

    const search =
        document
        .getElementById("search")
        .value
        .toLowerCase();


    const productCards =
        document.querySelectorAll(
            ".product"
        );


    productCards.forEach(card => {

        const name =
            card
            .getAttribute("data-name")
            .toLowerCase();


        const category =
            card
            .getAttribute("data-category")
            .toLowerCase();


        if (
            name.includes(search) ||
            category.includes(search)
        ) {

            card.style.display = "";

        } else {

            card.style.display = "none";

        }

    });

}


// ============================================================
// START
// ============================================================

updateCart();

</script>


</body>

</html>
"""


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )