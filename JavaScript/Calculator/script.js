function load() {
    var btns = document.querySelectorAll('#calculator span');



    var operators = ['+', '-', 'x', '÷'];
    var inputScreen = document.querySelector('#screen');
    var btnValue;
    var input;


    for (var i = 0; i < btns.length; i++) {
        var decimalAdded = false;  //flag to check if decimal is added
        btns[i].addEventListener('click', function (e) {
            btnValue = this.innerHTML;
            input = inputScreen.innerHTML;

            switch (btnValue) {

                case 'C':
                    inputScreen.innerHTML = '';
                    decimalAdded = false; // reset flag when clearing
                    break;

                case '=':
                    if (input !== '') {
                        // Replace 'x' with '*' and '÷' with '/' for evaluation
                        input = input.replace(/x/g, '*').replace(/÷/g, '/');
                        inputScreen.innerHTML = eval(input);
                        decimalAdded = false; // reset flag after evaluation
                    }
                    break;

                case '.':
                    if (!decimalAdded) { // check if decimal is already added
                        inputScreen.innerHTML += btnValue;
                        decimalAdded = true; // set flag to true after adding decimal
                    }
                    break;


                default:
                    inputScreen.innerHTML += btnValue;
                    break

            }
        }
    )

}}