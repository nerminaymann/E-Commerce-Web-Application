var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function (){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('ProductID:',productID, 'Action:',action)

        console.log('USER:',user)
        if (user=='AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            updateUserOrder(productID,action)
        }
    })
}

function updateUserOrder(productId,action){
    console.log('User is logged in, sending data.. ')

    var url = '/update_item/'

    fetch(url, {method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({'productId':productId,'action':action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:',data)
        })
}