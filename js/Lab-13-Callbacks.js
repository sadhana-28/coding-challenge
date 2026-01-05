// Lab 13: Callbacks

function completeBilling(callback) {
  let invoiceData = { total: 2500 };
  callback(invoiceData);
}

completeBilling(function (invoice) {
  console.log("Invoice Generated:", invoice);
});
