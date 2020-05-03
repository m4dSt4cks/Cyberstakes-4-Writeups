function getTransactionsByAccount(myaccount, startBlockNumber, endBlockNumber) {
  if (endBlockNumber == null) {
    endBlockNumber = eth.blockNumber;
    console.log("Using endBlockNumber: " + endBlockNumber);
  }
  if (startBlockNumber == null) {
    startBlockNumber = endBlockNumber - 1000;
    console.log("Using startBlockNumber: " + startBlockNumber);
  }
  console.log("Searching for transactions to/from account \"" + myaccount + "\" within blocks "  + startBlockNumber + " and " + endBlockNumber);
  
  result = "";
  sum = 0;
  for (var i = startBlockNumber; i <= endBlockNumber; i++) {
    var block = eth.getBlock(i, true);
    if (block != null && block.transactions != null) {
		for (e = 0; e < block.transactions.length; e++){
         if (myaccount == block.transactions[e].from) {
			if (block.transactions[e].value <= 2500000000000000000) {
				result = block.transactions[e].to;
				sum += parseInt(block.transactions[e].value);
				if (block.transactions[e].value == 2500000000000000000){
					console.log(block.transactions[e].input); // read the hints
					return result;
				}
				else if (sum == 2500000000000000000){
					console.log("\ntest\n" + block.transactions[e].input); // read the hints
					return result;
				}
			}
		}
		}
    }
  }
}

addr = "0xb4ba4b90df51d42a7c6093e92e1c7d22874c14f2"
while(addr) {
	addr = getTransactionsByAccount(addr, 1, 1000);
	console.log("----------------------------------------------------------")
	console.log(addr)
}
 // 1
// getTransactionsByAccount("0xae5165d3d0c9aa682557fe964c6da645b84e9e1d", 1, 1000); // 4
// https://ethereum.stackexchange.com/questions/2531/common-useful-javascript-snippets-for-geth/3478#3478

// last block is in the input, don't know why it doesn't work in this script


/*
function getTransactionsByAccount(myaccount, startBlockNumber, endBlockNumber) {
  if (endBlockNumber == null) {
    endBlockNumber = eth.blockNumber;
    console.log("Using endBlockNumber: " + endBlockNumber);
  }
  if (startBlockNumber == null) {
    startBlockNumber = endBlockNumber - 1000;
    console.log("Using startBlockNumber: " + startBlockNumber);
  }
  console.log("Searching for transactions to/from account \"" + myaccount + "\" within blocks "  + startBlockNumber + " and " + endBlockNumber);

  for (var i = startBlockNumber; i <= endBlockNumber; i++) {
    if (i % 1000 == 0) {
      console.log("Searching block " + i);
    }
    var block = eth.getBlock(i, true);
    if (block != null && block.transactions != null) {
      block.transactions.forEach( function(e) {
//         if (myaccount == "*" || myaccount == e.from || myaccount == e.to) {
         if (myaccount == e.from) {

          console.log("  tx hash          : " + e.hash + "\n"
            + "   nonce           : " + e.nonce + "\n"
            + "   blockHash       : " + e.blockHash + "\n"
            + "   blockNumber     : " + e.blockNumber + "\n"
            + "   transactionIndex: " + e.transactionIndex + "\n"
            + "   from            : " + e.from + "\n" 
            + "   to              : " + e.to + "\n"
            + "   value           : " + e.value + "\n"
            + "   gasPrice        : " + e.gasPrice + "\n"
            + "   gas             : " + e.gas + "\n"
            + "   input           : " + e.input);

        }
      })
    }
  }
}

console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0xb4ba4b90df51d42a7c6093e92e1c7d22874c14f2", 1, 1000); // 1
console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0xae5165d3d0c9aa682557fe964c6da645b84e9e1d", 1, 1000); // 1
console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0xf387f84b74e05416679ebbdbc79b509f7f2caa47", 1, 1000); // 1
console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0x3ec2a3d11e177ea8bff7d6cd9df360ebcc52d584", 1, 1000); // 1
console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0x4da56f7f58bc14c785cee861d25b2c417fe6853f", 1, 1000); // 1
console.log("----------------------------------------------------------------------------------------------");
getTransactionsByAccount("0x167f7969ae2ecf157306f798f63929903a02d771", 1, 1000); // 1
*/
