function validation(){
    const donor_name  = document.getElementById("name").value
    const number = document.getElementById("number").value
    const address = document.getElementById("address").value
    const food_details = document.getElementById("food_details").value
    var number_pattern = /^[789]\d{9}$/


    if(donor_name == ""){
        alert("Please Enter Your Name")
        return false
    }

    if(number == ""){
        alert("Please Enter Your Phone Number")
        return false
    }
    if (number.match(number_pattern) == null) {
        alert("Not a Valid Number")
        return false
    }

    if(address == ""){
        alert("Please Enter Your Address")
        return false
    }

    if(food_details == ""){
        alert("Please Enter the Details of the Food")
        return false
    }
}