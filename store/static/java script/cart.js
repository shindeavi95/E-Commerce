var updatebtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updatebtns.length; i++) {
    updatebtns[i].addEventListener('click',function () {
        var productId = this.dataset.product               // this is representing globle object here 
        var action = this.dataset.action                     
        console.log('productId:', productId, 'action:',action)

        console.log('USER', user)
        if(user == 'AnonymousUser'){
            addCookieItem(productId, action)
            console.log('Not logged in')
        }
        else {
           updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged in')
    if (action == 'add'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity': 1}
        }
        else{
            cart[productId]['quantity'] += 1
        }
    }
    if (action == 'remove'){
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity']<= 0){
            console.log("Item is Removed")
            delete cart[productId]
        }
    }
    console.log('Cart:',cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";doman=;path=/"
    location.reload()
}


function updateUserOrder(productId, action) {
    console.log('User is logged in , Sending Data..')

    var url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,                  //start from here
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
        return response.json()

     })
     .then((data) =>{
         console.log('data:',data)
         location.reload()

     })
}