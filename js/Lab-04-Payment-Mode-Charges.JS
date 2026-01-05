// Lab 4: Apply Payment Mode Charges

let totalWithTax = 950;
let paymentMode = "Card";

let surcharge = 0;
let convenienceFee = 0;

if (paymentMode === "Card" && totalWithTax < 1000) {
  surcharge = totalWithTax * 0.025;
} else {
  convenienceFee = totalWithTax * 0.01;
}

let finalTotal = totalWithTax + surcharge + convenienceFee;

console.log("Payment Mode:", paymentMode);
console.log("Final Amount:", finalTotal);
