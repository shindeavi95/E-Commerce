var updatebtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updatebtns.length; i++) {
    updatebtns[i].addEventListener('click',function () {
        var productId = this.dataset.product
        var action = this.dataset,action
        console.log('productId:', productId, 'action:',action)

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else {
           updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is logged in , Sending Data..')

    var url = '/update_item'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken                  //start from here
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
        return response.json()

     })
     .then((data) =>{
         console.log('data',data)

     })
}