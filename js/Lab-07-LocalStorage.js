// Lab 7: LocalStorage (Run in Browser Console)

let cartItems = [{ item: "Book", price: 300 }];
let invoiceData = { total: 300 };

localStorage.setItem("cart", JSON.stringify(cartItems));
localStorage.setItem("invoice", JSON.stringify(invoiceData));

console.log("Stored Cart:", JSON.parse(localStorage.getItem("cart")));
