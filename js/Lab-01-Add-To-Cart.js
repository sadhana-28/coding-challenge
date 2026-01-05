// Lab 1: Add Items to Cart

let cart = [];

cart.push({
  itemCode: "IT001",
  description: "Notebook",
  quantity: 2,
  pricePerUnit: 100,
  totalPrice: 2 * 100
});

cart.push({
  itemCode: "IT002",
  description: "Pen",
  quantity: 5,
  pricePerUnit: 20,
  totalPrice: 5 * 20
});

let grandTotal = 0;
for (let item of cart) {
  grandTotal += item.totalPrice;
}

console.log("Cart Items:", cart);
console.log("Grand Total:", grandTotal);
