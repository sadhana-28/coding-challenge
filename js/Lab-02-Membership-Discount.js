// Lab 2: Apply Membership Discount

let grandTotal = 5000;
let membershipType = "Gold";

let discountRate = 0;

if (membershipType === "Silver") discountRate = 0.05;
else if (membershipType === "Gold") discountRate = 0.10;
else if (membershipType === "Platinum") discountRate = 0.15;

let discountAmount = grandTotal * discountRate;
let discountedTotal = grandTotal - discountAmount;

console.log("Membership Type:", membershipType);
console.log("Discount Amount:", discountAmount);
console.log("Total After Discount:", discountedTotal);
