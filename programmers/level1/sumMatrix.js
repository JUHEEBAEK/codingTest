function sumMatrix(arr1, arr2) {
    var answer = [[]];
    for(let i = 0; i < arr1.length; i++) {
        answer[i] = [];
        for(let j = 0; j <arr1[0].length; j++) {
            const number = Number(arr1[i][j]) + Number(arr2[i][j]);
            answer[i].push(number);
        }
    }
    return answer;
}