function getDominantSet(data){

	//take all keys except for id
	var allKeys = Object.keys(data[0]);

	keys = []

	allKeys.map(function(key){
		if (key !== "id"){
			keys.push(key);
		}
	})

	function compare(a,b){

		for (var i = 0; i < keys.length; i++) {
			fac = keys[i].indexOf("[min]") * 2 + 1
			a_val = parseFloat(a[keys[i]]) * fac
			b_val = parseFloat(b[keys[i]]) * fac
			if ( a_val < b_val){
				return -1;
			} else if (a_val > b_val) {
				return 1;
			}
		}

		return 0;
	}

	P = data.sort(compare);

	// if (keys[0].indexOf("[min]") == -1){
	// 	P.reverse()
	// }

	return front(P, keys)
}

function front(P, keys){

	if (P.length == 1){
		return P
	}else{

		var T = front(P.slice(0, Math.ceil(parseFloat(P.length)/2)), keys);
		var B = front(P.slice(Math.ceil(parseFloat(P.length)/2), P.length), keys);
		var M = [];
		
		for (var i = 0; i < B.length; i++) {
			// var keys = Object.keys(B[i]);
			var dominated = true;
			for (var j = 0; j < T.length; j++) {
				dominated = true;
				for (var k = 0; k < keys.length; k++) {
					// if target is not min, fac is -1 (reverse dominance criteria for maximization objective)
					fac = keys[k].indexOf("[min]") * 2 + 1
					if ((fac * parseFloat(B[i][keys[k]])) < (fac * parseFloat(T[j][keys[k]])) ){
						// console.log(parseFloat(B[i][keys[k]]))
						// console.log(parseFloat(T[j][keys[k]]))
						dominated = false;
						break;
					}
				}
				if (dominated){
					break;
				}
			}
			if (!dominated){
				M.push(B[i]);
			}
		}
		return T.concat(M);
	}
}